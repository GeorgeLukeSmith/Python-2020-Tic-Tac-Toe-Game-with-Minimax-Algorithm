import pygame
import sys


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

pygame.mixer.music.load("./resources/audio/GameMusic001.mp3")
pygame.mixer.music.play(-1)
click_sound = pygame.mixer.Sound("./resources/audio/GameClickSound.wav")
beep_sound = pygame.mixer.Sound("./resources/audio/BeepingSoundEffect.wav")
easy_wins = 0
medium_wins = 0
hard_wins = 0
impossible_wins = 0
player_colour = BLUE


def display_text(text, xOffset, yPos):
    my_font = pygame.font.Font('./resources/font/Minecraftia.ttf', 20)
    label = my_font.render(text, False, BLACK)
    screen.blit(label, (int(width/2) - xOffset, yPos))


def menu_screen(easy_wins, medium_wins, hard_wins, impossible_wins):
    menu = True
    while menu:

        screen.fill(WHITE)
        title = pygame.image.load("./resources/images/TitleImage.png")
        title = pygame.transform.scale(title, (width, 162))
        background = pygame.image.load('./resources/images/MenuBackground.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        screen.blit(title, (0, 20))

        # Options Menu Button
        question_symbol = pygame.image.load("./resources/images/QuestionMark.png")
        draw_button(40, 490, 80, 80, '', -215, 220)
        question_symbol = pygame.transform.scale(question_symbol, (60, 60))
        screen.blit(question_symbol, (50, 500))

        # Difficulty buttons
        draw_button(int(width / 4), 190, int(width / 2), 80, 'Easy', 25, 220)
        draw_button(int(width / 4), 290, int(width / 2), 80, 'Medium', 40, 320)
        draw_button(int(width / 4), 390, int(width / 2), 80, 'Hard', 27, 420)
        draw_button(int(width / 4), 490, int(width / 2), 80, 'Impossible!', 60, 520)

        # Score boxes
        if easy_wins < 10:
            draw_button(int(width/2) + 180, 190, 80, 80, str(easy_wins), -215, 220)
        elif easy_wins >= 10:
            draw_button(int(width / 2) + 180, 190, 80, 80, str(easy_wins), -205, 220)

        if medium_wins < 10:
            draw_button(int(width / 2) + 180, 290, 80, 80, str(medium_wins), -215, 320)
        elif medium_wins >= 10:
            draw_button(int(width / 2) + 180, 290, 80, 80, str(medium_wins), -205, 320)

        if hard_wins < 10:
            draw_button(int(width / 2) + 180, 390, 80, 80, str(hard_wins), -215, 420)
        elif hard_wins >= 10:
            draw_button(int(width / 2) + 180, 390, 80, 80, str(hard_wins), -205, 420)

        if impossible_wins < 10:
            draw_button(int(width / 2) + 180, 490, 80, 80, str(impossible_wins), -215, 520)
        elif impossible_wins >= 10:
            draw_button(int(width / 2) + 180, 490, 80, 80, str(impossible_wins), -205, 520)

        pygame.display.update()
        for menu_event in pygame.event.get():
            if menu_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if menu_event.type == pygame.MOUSEBUTTONDOWN:
                posX = menu_event.pos[0]
                posY = menu_event.pos[1]
                if posX in range(int(width/4), (int(width/4) + int(width / 2))):
                    if posY in range(190, 270):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 1
                    elif posY in range(290, 370):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 2
                    elif posY in range(390, 470):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 3
                    elif posY in range(490, 570):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 4
                elif posX in range(40, (40 + 80)):
                    if posY in range(490, (490 + 80)):
                        instruction_menu()


def draw_button(rectLeft, rectTop, rectWidth, rectHeight, text, textXOfset, textYPos):
    pygame.draw.rect(screen, GREY, [rectLeft, rectTop, rectWidth, rectHeight])
    pygame.draw.rect(screen, BLACK, [rectLeft, rectTop, rectWidth, rectHeight], 5)
    display_text(text, textXOfset, textYPos)


def turn_select_screen():
    while True:

        screen.fill(WHITE)
        title = pygame.image.load("./resources/images/TitleImage.png")
        title = pygame.transform.scale(title, (width, 162))
        background = pygame.image.load('./resources/images/MenuBackground.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        screen.blit(title, (0, 20))
        draw_button(int(width / 4), 190, int(width / 2), 80, 'I want to go 1st', 90, 220)
        draw_button(int(width / 4), 290, int(width / 2), 80, 'I want to go 2nd', 90, 320)
        draw_button(int(width / 4), 390, int(width / 2), 80, 'Surprise me (random)', 130, 420)
        pygame.display.update()
        for menu_event in pygame.event.get():
            if menu_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if menu_event.type == pygame.MOUSEBUTTONDOWN:
                posX = menu_event.pos[0]
                posY = menu_event.pos[1]
                if posX in range(int(width/4), (int(width/4) + int(width / 2))):
                    if posY in range(190, 270):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 1
                    elif posY in range(290, 370):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 2
                    elif posY in range(390, 470):
                        click_sound.play()
                        pygame.time.wait(300)
                        return 3


def instruction_menu():
    running = True
    while running:
        screen.fill(WHITE)
        title = pygame.image.load("./resources/images/TitleImage.png")
        title = pygame.transform.scale(title, (width, 162))
        background = pygame.image.load('./resources/images/MenuBackground.png').convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        screen.blit(title, (0, 20))
        draw_button(int(width / 7), 190, int(width / 1.4), 250, '', 190, 210)
        display_text('Welcome to Tic Tac Toe!', 200, 200)
        display_text('Line up 3 squares to win, but', 200, 235)
        display_text('remember the computer is also ', 200, 260)
        display_text('vying for victory!', 200, 285)
        display_text('let them line up 3 squares', 200, 315)
        display_text('and it is GAME OVER!', 200, 340)
        display_text('You = BLUE', 200, 380)
        display_text('Computer = RED', 200, 405)
        draw_button(int(width / 4), 490, int(width / 2), 80, 'Return to Main Menu', 110, 520)
        pygame.display.update()
        for menu_event in pygame.event.get():
            if menu_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if menu_event.type == pygame.MOUSEBUTTONDOWN:
                posX = menu_event.pos[0]
                posY = menu_event.pos[1]
                if posX in range(int(width / 4), (int(width / 4) + int(width / 2))):
                    if posY in range(490, 570):
                        click_sound.play()
                        pygame.time.wait(300)
                        return


def draw_board(matrix):
    for c in range(COL_NUM):
        for r in range(ROW_NUM):
            if matrix[r][c] == 0:
                pygame.draw.rect(screen, WHITE, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE-5, SQUARE_SIZE-5))
            if matrix[r][c] == 1:
                pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE-5, SQUARE_SIZE-5))
            if matrix[r][c] == 2:
                pygame.draw.rect(screen, RED, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE-5, SQUARE_SIZE-5))
