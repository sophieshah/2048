import pygame, sys
import math
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
bg_color = (255, 255, 245)  # background color
font_color = (0, 0, 0)  # black font and line color
box_color = (204, 229, 255)
main_font = pygame.font.Font(None, 50)
width = 400
height = 400

nums = [[0 for i in range(0,4)] for j in range(0,4)]

index_list = [0,1,2,3]

global count

def choose_random():
    count = 0
    valid = False
    while not valid:
        start_row = random.choice(index_list)
        start_col = random.choice(index_list)
        # print(start_col,start_row)
        if(nums[start_col][start_row]==0):
            nums[start_col][start_row] = 2
            valid = True
    for i in range(0, len(nums)):
        for j in range(0, len(nums[i])):
            if nums[i][j] != 0:
                count += 1
    print(count)
    if(count<16):
        return False
    else:
        return True

def draw_nums():
    square_size = 100
    text_font = pygame.font.Font(None, 50)

    for i in range(0,len(nums)):
        for j in range(0,len(nums[i])):
            erase_nums(i,j)
            if(nums[i][j]!= 0):
                letter = text_font.render(str(nums[i][j]), 0, font_color)
                letter_rect = letter.get_rect(center=(square_size * i + square_size // 2, square_size * j + square_size // 2))
                screen.blit(letter, letter_rect)

def erase_nums(col,row):
    pygame.draw.rect(screen, bg_color, [(col * 100, row * 100), (100, 100)], 100)

def check_up():
    print(nums)
    for i in range(0, 4):
        for j in range(1, 4):
            if nums[i][j - 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j - 1] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 4):
        for j in range(0, 3):
            if (nums[i][j] == nums[i][j + 1]):
                nums[i][j] *= 2
                nums[i][j + 1] = 0

    for i in range(0, 4):
        for j in range(1, 4):
            if nums[i][j - 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j - 1] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 4):
        for j in range(0, 3):
            if (nums[i][j] == nums[i][j + 1]):
                nums[i][j] *= 2
                nums[i][j + 1] = 0

    for i in range(0, 4):
        for j in range(1, 4):
            if nums[i][j - 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j - 1] = nums[i][j]
                nums[i][j] = 0

    print(nums)
    for i in range(0, 4):
        for j in range(0, 3):
            if (nums[i][j] == nums[i][j + 1]):
                nums[i][j] *= 2
                nums[i][j + 1] = 0
    print(nums)

def check_down():
    print(nums)
    for i in range(0, 4):
        for j in range(0, 3):
            if nums[i][j + 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j + 1] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 4):
        for j in range(1, 4):
            if (nums[i][j] == nums[i][j - 1]):
                nums[i][j] *= 2
                nums[i][j - 1] = 0

    for i in range(0, 4):
        for j in range(0, 3):
            if nums[i][j + 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j + 1] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 4):
        for j in range(1, 4):
            if (nums[i][j] == nums[i][j - 1]):
                nums[i][j] *= 2
                nums[i][j - 1] = 0

    for i in range(0, 4):
        for j in range(0, 3):
            if nums[i][j + 1] == 0:
                # print('valid at',i,j-1)
                nums[i][j + 1] = nums[i][j]
                nums[i][j] = 0

    print(nums)
    for i in range(0, 4):
        for j in range(1, 4):
            if (nums[i][j] == nums[i][j - 1]):
                nums[i][j] *= 2
                nums[i][j - 1] = 0
    print(nums)

def check_left():
    print(nums)
    for i in range(1, 4):
        for j in range(0, 4):
            if nums[i-1][j] == 0:
                # print('valid at',i,j-1)
                nums[i-1][j] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 3):
        for j in range(0, 4):
            if (nums[i][j] == nums[i+1][j]):
                nums[i][j] *= 2
                nums[i+1][j] = 0

    for i in range(1, 4):
        for j in range(0, 4):
            if nums[i-1][j] == 0:
                # print('valid at',i,j-1)
                nums[i-1][j] = nums[i][j]
                nums[i][j] = 0
    for i in range(0, 3):
        for j in range(0, 4):
            if (nums[i][j] == nums[i+1][j]):
                nums[i][j] *= 2
                nums[i+1][j] = 0

    for i in range(1, 4):
        for j in range(0, 4):
            if nums[i-1][j] == 0:
                # print('valid at',i,j-1)
                nums[i-1][j] = nums[i][j]
                nums[i][j] = 0

    print(nums)
    for i in range(0, 3):
        for j in range(0, 4):
            if (nums[i][j] == nums[i+1][j]):
                nums[i][j] *= 2
                nums[i+1][j] = 0
    print(nums)

def check_right():
    print(nums)
    for i in range(0, 3):
        for j in range(0, 4):
            if nums[i+1][j] == 0:
                # print('valid at',i,j-1)
                nums[i+1][j] = nums[i][j]
                nums[i][j] = 0
    for i in range(1, 4):
        for j in range(0, 4):
            if (nums[i][j] == nums[i-1][j]):
                nums[i][j] *= 2
                nums[i-1][j] = 0

    for i in range(0, 3):
        for j in range(0, 4):
            if nums[i+1][j] == 0:
                # print('valid at',i,j-1)
                nums[i+1][j] = nums[i][j]
                nums[i][j] = 0
    for i in range(1, 4):
        for j in range(0, 4):
            if (nums[i][j] == nums[i-1][j]):
                nums[i][j] *= 2
                nums[i-1][j] = 0

    for i in range(0, 3):
        for j in range(0, 4):
            if nums[i+1][j] == 0:
                # print('valid at',i,j-1)
                nums[i+1][j] = nums[i][j]
                nums[i][j] = 0

    print(nums)
    for i in range(1, 4):
        for j in range(0, 4):
            if (nums[i][j] == nums[i-1][j]):
                nums[i][j] *= 2
                nums[i-1][j] = 0
    print(nums)

def check_surrounding(col,row):
    print("before surrounding")
    print(nums)

    if(col==0 and row==0):
        if(nums[col][row]==nums[col][row+1]):
            nums[col][row] *= 2
            nums[col][row+1] = 0
            erase_nums(col,row+1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col+1][row]):
            nums[col][row] *= 2
            nums[col+1][row] = 0
            erase_nums(col+1, row)
            erase_nums(col, row)
    elif (col == 3 and row == 0):
        if (nums[col][row] == nums[col][row + 1]):
            nums[col][row] *= 2
            nums[col][row + 1] = 0
            erase_nums(col, row + 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col - 1][row]):
            nums[col][row] *= 2
            nums[col - 1][row] = 0
            erase_nums(col - 1, row)
            erase_nums(col, row)
    elif (col == 0 and row == 3):
        if (nums[col][row] == nums[col][row - 1]):
            nums[col][row] *= 2
            nums[col][row - 1] = 0
            erase_nums(col, row - 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col + 1][row]):
            nums[col][row] *= 2
            nums[col + 1][row] = 0
            erase_nums(col + 1, row)
            erase_nums(col, row)
    elif (col == 3 and row == 3):
        if (nums[col][row] == nums[col][row - 1]):
            nums[col][row] *= 2
            nums[col][row - 1] = 0
            erase_nums(col, row - 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col - 1][row]):
            nums[col][row] *= 2
            nums[col - 1][row] = 0
            erase_nums(col - 1, row)
            erase_nums(col, row)
    elif (row == 0):
        if (nums[col][row] == nums[col][row + 1]):
            nums[col][row] *= 2
            nums[col][row + 1] = 0
            erase_nums(col, row + 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col - 1][row]):
            nums[col][row] *= 2
            nums[col - 1][row] = 0
            erase_nums(col - 1, row)
            erase_nums(col, row)
        if (nums[col][row] == nums[col + 1][row]):
            nums[col][row] *= 2
            nums[col + 1][row] = 0
            erase_nums(col + 1, row)
            erase_nums(col, row)
    elif (row == 3):
        if (nums[col][row] == nums[col][row - 1]):
            nums[col][row] *= 2
            nums[col][row - 1] = 0
            erase_nums(col, row - 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col - 1][row]):
            nums[col][row] *= 2
            nums[col - 1][row] = 0
            erase_nums(col - 1, row)
            erase_nums(col, row)
        if (nums[col][row] == nums[col + 1][row]):
            nums[col][row] *= 2
            nums[col + 1][row] = 0
            erase_nums(col + 1, row)
            erase_nums(col, row)
    elif (col == 0):
        if (nums[col][row] == nums[col][row + 1]):
            nums[col][row] *= 2
            nums[col][row + 1] = 0
            erase_nums(col, row + 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col][row - 1]):
            nums[col][row] *= 2
            nums[col][row - 1] = 0
            erase_nums(col, row - 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col + 1][row]):
            nums[col][row] *= 2
            nums[col + 1][row] = 0
            erase_nums(col + 1, row)
            erase_nums(col, row)
    elif (col == 3):
        if (nums[col][row] == nums[col][row + 1]):
            nums[col][row] *= 2
            nums[col][row + 1] = 0
            erase_nums(col, row + 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col][row - 1]):
            nums[col][row] *= 2
            nums[col][row - 1] = 0
            erase_nums(col, row - 1)
            erase_nums(col, row)
        if (nums[col][row] == nums[col - 1][row]):
            nums[col][row] *= 2
            nums[col - 1][row] = 0
            erase_nums(col - 1, row)
            erase_nums(col, row)


    print("check surrounding")
    print(nums)
    print()

def draw_squares():
    line_color = (0, 0, 0)
    square_size = 100
    # draws horizontal lines
    for i in range(0, 4):
        # checks if it needs a bolded line
        pygame.draw.line(screen, line_color, (0, i * square_size), (900, i * square_size), 5)
    # draws vertical lines
    for j in range(0, 4):
        # checks if it needs a bolded line
        pygame.draw.line(screen, line_color, (j * square_size, 0), (j * square_size, 900), 5)

def lose_screen():
    game_loss_color = (255, 69, 0)
    screen.fill(game_loss_color)

    # prints out "Game Over :("
    game_won_title = main_font.render("Game Over :(", 0, font_color)
    game_won_rectangle = game_won_title.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(game_won_title, game_won_rectangle)

    quit_text = main_font.render("Restart", 0, font_color)
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(box_color)
    quit_surface.blit(quit_text, (10, 10))
    restart_rectangle = quit_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(quit_surface, restart_rectangle)

    # print correct word
    square_size = 100
    text_font = pygame.font.Font(None, 50)

def draw_game_start():
    screen.fill(bg_color)
    title = main_font.render("Welcome to 2048", 0, font_color)
    title_rectangle = title.get_rect(center=(width // 2, height // 2 - 100))
    screen.blit(title, title_rectangle)

    start_text = main_font.render("Start 2048", 0, font_color)
    start_surface = pygame.Surface((start_text.get_size()[0] + 20,
                                    start_text.get_size()[1] + 20))
    start_surface.fill(box_color)
    start_surface.blit(start_text, (10, 10))
    start_rectangle = start_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(start_surface, start_rectangle)

    # i is col
    # j is row
    # [i][j] is [col][row]

    choose_random()
    count = 0
    board_full = False
    game_start = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    print("game start")
                    game_start = True
                    screen.fill(bg_color)
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_LEFT):
                    for i in range(1,len(nums)):
                        for j in range(0,len(nums[i])):
                            if nums[i][j] != 0:
                                check_left()
                    print('left')
                if (event.key == pygame.K_RIGHT):
                    for i in range(0,len(nums)-1):
                        for j in range(0,len(nums[i])):
                            if nums[i][j] != 0:
                                check_right()
                    print('right')
                if (event.key == pygame.K_UP):
                    for i in range(0,len(nums)):
                        for j in range(1,len(nums[i])):
                            if nums[i][j] != 0:
                                check_up()
                    print('up')
                if (event.key == pygame.K_DOWN):
                    for i in range(0,len(nums)):
                        for j in range(0,len(nums[i])-1):
                            if nums[i][j] != 0:
                                check_down()
                    print('down')

                board_full = choose_random()
        if(game_start):
            draw_nums()
            draw_squares()

        if(board_full):
            lose_screen()
            game_start = False
            board_full = False
            for i in range(0,4):
                for j in range(0,4):
                    nums[i][j] = 0
            choose_random()


        pygame.display.update()


draw_game_start()
