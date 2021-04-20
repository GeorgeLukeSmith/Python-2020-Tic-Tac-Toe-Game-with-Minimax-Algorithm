import numpy as np
import pygame
import gui

ROW_NUM = 3
COL_NUM = 3
beep_sound = pygame.mixer.Sound("./resources/audio/BeepingSoundEffect.wav")


# places the token in the matrix
def place_token(matrix, x, y, piece):
    matrix[x][y] = piece


# flips the board
def print_board(matrix):
    print(np.flip(matrix, 0))


# creates a matrix in which the game is played
def create_board():
    drawn = np.zeros((ROW_NUM, COL_NUM))
    return drawn


def check_valid_move(matrix, row, col):
    if matrix[row][col].all() == 0:
        return True
    else:
        return False


# search for winning states
def win_state(matrix, token):
    # Check horizontal win states
    for r in range(3):
        if matrix[r][0] == token and matrix[r][1] == token \
             and matrix[r][2] == token:
            beep_sound.play()
            for i in range(10):
                matrix[r][0] = 0
                matrix[r][1] = 0
                matrix[r][2] = 0
                gui.draw_board(matrix)
                pygame.display.update()
                pygame.time.wait(100)
                matrix[r][0] = token
                matrix[r][1] = token
                matrix[r][2] = token
                gui.draw_board(matrix)
                pygame.display.update()
                pygame.time.wait(100)
            return True
    # check vertical win states
    for c in range(3):
        if matrix[0][c] == token and matrix[1][c] == token \
                and matrix[2][c] == token:
            beep_sound.play()
            for i in range(10):
                matrix[0][c] = 0
                matrix[1][c] = 0
                matrix[2][c] = 0
                gui.draw_board(matrix)
                pygame.display.update()
                pygame.time.wait(100)
                matrix[0][c] = token
                matrix[1][c] = token
                matrix[2][c] = token
                gui.draw_board(matrix)
                pygame.display.update()
                pygame.time.wait(100)
            return True
    # check negative gradient diagonals
    for r in range(1):
        for c in range(1):
            if matrix[r][c] == token and matrix[r + 1][c + 1] == token \
                   and matrix[r + 2][c + 2] == token:
                beep_sound.play()
                for i in range(10):
                    matrix[r][c] = 0
                    matrix[r + 1][c + 1] = 0
                    matrix[c + 2][r + 2] = 0
                    gui.draw_board(matrix)
                    pygame.display.update()
                    pygame.time.wait(100)
                    matrix[r][c] = token
                    matrix[r + 1][c + 1] = token
                    matrix[r + 2][c + 2] = token
                    gui.draw_board(matrix)
                    pygame.display.update()
                    pygame.time.wait(100)
                return True
    # check negative positive diagonals
    for r in range(1):
        for c in range(1):
            if matrix[0][2] == token and matrix[1][1] == token \
                    and matrix[2][0] == token:
                beep_sound.play()
                for i in range(10):
                    matrix[0][2] = 0
                    matrix[1][1] = 0
                    matrix[2][0] = 0
                    gui.draw_board(matrix)
                    pygame.display.update()
                    pygame.time.wait(100)
                    matrix[0][2] = token
                    matrix[1][1] = token
                    matrix[2][0] = token
                    gui.draw_board(matrix)
                    pygame.display.update()
                    pygame.time.wait(100)
                return True


# Test win states for future moves (for use in minimax)
def test_win_state(matrix, token):
    # Check horizontal win states
    for r in range(3):
        if matrix[r][0] == token and matrix[r][1] == token \
             and matrix[r][2] == token:
            return True
    # check vertical win states
    for c in range(3):
        if matrix[0][c] == token and matrix[1][c] == token \
                and matrix[2][c] == token:
            return True
    # check negative gradient diagonals
    for r in range(1):
        for c in range(1):
            if matrix[r][c] == token and matrix[r + 1][c + 1] == token \
                   and matrix[r + 2][c + 2] == token:
                return True
    # check negative positive diagonals
    for r in range(1):
        for c in range(1):
            if matrix[0][2] == token and matrix[1][1] == token \
                    and matrix[2][0] == token:
                return True
