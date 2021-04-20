import pygame
import sys
import math
import random
import ai
import gui
import tic_tac_toe as ttt


PLAYER_TOKEN = 1
AI_TOKEN = 2
ROW_NUM = 3
COL_NUM = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
RED = (245, 64, 64)
GREY = (160, 160, 160)


pygame.init()
SQUARE_SIZE = 200
width = SQUARE_SIZE * COL_NUM
height = SQUARE_SIZE * ROW_NUM
size = (width - 5, height - 5)
screen = pygame.display.set_mode(size)
board = ttt.create_board()
print("\n")
print(board)
gui.draw_board(board)
gameOver = False

pygame.mixer.music.load("./resources/audio/GameMusic001.mp3")
pygame.mixer.music.play(-1)
click_sound = pygame.mixer.Sound("./resources/audio/GameClickSound.wav")
beep_sound = pygame.mixer.Sound("./resources/audio/BeepingSoundEffect.wav")
easy_wins = 0
medium_wins = 0
hard_wins = 0
impossible_wins = 0
player_colour = BLUE

while True:

    game_mode = gui.menu_screen(easy_wins, medium_wins, hard_wins, impossible_wins)
    turn_choice = gui.turn_select_screen()
    if turn_choice == 1:
        turn = 0
    elif turn_choice == 2:
        turn = 1
    elif turn_choice == 3:
        turn = random.randint(0, 1)
    board = ttt.create_board()
    screen.fill(BLACK)
    gui.draw_board(board)
    pygame.display.update()
    gameOver = False
    while not gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if turn == 0 and not gameOver:

                    posX = event.pos[0]
                    posY = event.pos[1]
                    move_row = int(math.floor(posY / SQUARE_SIZE))
                    move_col = int(math.floor(posX / SQUARE_SIZE))
                    if ttt.check_valid_move(board, move_row, move_col):
                        click_sound.play()
                        pygame.time.wait(200)
                        board[move_row][move_col] = PLAYER_TOKEN
                        print("\nplayer 1 move:\n")
                        print(board)
                        print("\n")
                        gui.draw_board(board)
                        pygame.display.update()

                        if ttt.win_state(board, 1):
                            print("Player 1 wins!")
                            if game_mode == 1:
                                easy_wins = easy_wins + 1
                            if game_mode == 2:
                                medium_wins = medium_wins + 1
                            if game_mode == 3:
                                hard_wins = hard_wins + 1
                            if game_mode == 4:
                                impossible_wins = impossible_wins + 1
                            gameOver = True
                        if ai.is_terminal_node(board):
                            print("Game Over")
                            gameOver = True
                        turn += 1
                        turn = turn % 2
        # AI Move
        if turn == 1 and not gameOver:
            while True:
                if game_mode == 1:
                    posX = random.randint(0, ROW_NUM - 1)
                    posY = random.randint(0, COL_NUM - 1)
                elif game_mode != 1:
                    if game_mode == 2:
                        posX = ai.choose_ai_move(board, AI_TOKEN)[0]
                        posY = ai.choose_ai_move(board, AI_TOKEN)[1]
                    elif game_mode != 2:
                        if game_mode == 3:
                            depth = 2
                        elif game_mode == 4:
                            depth = 4
                        posX = ai.minimax(board, depth, True)[0]
                        posY = ai.minimax(board, depth, True)[1]
                move_row = posX
                move_col = posY
                if ttt.check_valid_move(board, move_row, move_col):
                    break
            pygame.time.wait(500)
            click_sound.play()
            pygame.time.wait(200)
            board[move_row][move_col] = AI_TOKEN
            print("\nplayer 2 move:\n")
            print(board)
            print("\n")
            gui.draw_board(board)
            pygame.display.update()

            if ttt.win_state(board, 2):
                print("Player 2 wins!")
                gameOver = True
            if ai.is_terminal_node(board):
                print("Game Over")
                gameOver = True
            turn += 1
            turn = turn % 2
        if gameOver:
            pygame.time.wait(3000)
            break
