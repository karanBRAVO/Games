# import statements
import sys
import pygame
from pygame.locals import *
import random

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)

# initializing pygame
pygame.init()

# Game window
SCREENWIDTH = 300
SCREENHEIGHT = 530
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Fly with Python")
SCREEN.fill(white)

# Text-Message
font1 = pygame.font.Font("freesansbold.ttf", 36)
font2 = pygame.font.Font("freesansbold.ttf", 16)
message1 = font1.render('Fly with Python', True, white, black)
message2 = font2.render('Press SPACE_KEY to START', True, black, white)
messageRect1 = message1.get_rect()
messageRect2 = message2.get_rect()
messageRect1.center = (SCREENWIDTH // 2, SCREENHEIGHT // 3)
messageRect2.center = (SCREENWIDTH // 2, SCREENHEIGHT // 1.5)

GAME_SPRITES = {
    'background': pygame.transform.scale(pygame.image.load('img/Assets/background.png'), (300, 530)),
    'bar': pygame.image.load('img/Assets/bar.png'),
    'bot': pygame.image.load('img/Assets/bot.png'),
}
FPS_Clock = pygame.time.Clock()


def hor_bars(x, y, w, h):  # rect(x?, y?, width?, height?)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x, y + 20, w, h), border_radius=2)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x + 150, y - 70, w, h), border_radius=2)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x + 29, y + 200, w, h), border_radius=2)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x + 150, y + 290, w, h), border_radius=2)


def my_bot(x, y):
    pygame.draw.aaline(surface=SCREEN, color=black, start_pos=(x, y), end_pos=(x + 8, y - 8), blend=9)
    pygame.draw.aaline(surface=SCREEN, color=black, start_pos=(x, y), end_pos=(x - 8, y - 8), blend=9)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x - 3, y, 7, 5), border_radius=1)
    pygame.draw.rect(surface=SCREEN, color=black, rect=(x - 6, y + 5, 14, 13), border_radius=2)


def welcome_screen():
    bot_x = 150
    bot_y = 265
    while True:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(message1, messageRect1)
                SCREEN.blit(message2, messageRect2)
                my_bot(bot_x, bot_y)
                hor_bars(0, 100, 150, 10)


moving_Bars_left1 = pygame.Rect(0, 0, 149, 10)
moving_Bars_left2 = pygame.Rect(0, 250, 149, 10)
moving_Bars_right1 = pygame.Rect(150, 80, 149, 10)
moving_Bars_right2 = pygame.Rect(150, 360, 149, 10)
barVel_y = 1
score = 0


def getRandomBars():
    global barVel_y, score

    moving_Bars_left1.y += barVel_y
    moving_Bars_left2.y += barVel_y
    moving_Bars_right1.y += barVel_y
    moving_Bars_right2.y += barVel_y

    if moving_Bars_left1.y >= SCREENHEIGHT:
        moving_Bars_left1.x = random.randrange(start=-15, stop=35)
        moving_Bars_left1.y = 0
        score += 1

    if moving_Bars_right1.y >= SCREENHEIGHT:
        moving_Bars_right1.x = random.randrange(start=140, stop=269)
        moving_Bars_right1.y = 0
        score += 1

    if moving_Bars_left2.y >= SCREENHEIGHT:
        moving_Bars_left2.x = random.randrange(start=-15, stop=35)
        moving_Bars_left2.y = 0
        score += 1

    if moving_Bars_right2.y >= SCREENHEIGHT:
        moving_Bars_right2.x = random.randrange(start=140, stop=269)
        moving_Bars_right2.y = 0
        score += 1

    pygame.draw.rect(SCREEN, black, moving_Bars_left1, border_radius=2)
    pygame.draw.rect(SCREEN, black, moving_Bars_left2, border_radius=2)
    pygame.draw.rect(SCREEN, black, moving_Bars_right1, border_radius=2)
    pygame.draw.rect(SCREEN, black, moving_Bars_right2, border_radius=2)


moving_bot_image = pygame.Rect(SCREENWIDTH // 2, SCREENHEIGHT // 1.2, 21, 33)


def isCollision():

    if moving_bot_image.colliderect(moving_Bars_left1):
        if moving_bot_image.top - moving_Bars_left1.bottom < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.bottom - moving_Bars_left1.top < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.left - moving_Bars_left1.right < 5:
            print('score: ', score)
            sys.exit()
    if moving_bot_image.colliderect(moving_Bars_left2):
        if moving_bot_image.top - moving_Bars_left2.bottom < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.bottom - moving_Bars_left2.top < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.left - moving_Bars_left2.right < 5:
            print('score: ', score)
            sys.exit()

    if moving_bot_image.colliderect(moving_Bars_right1):
        if moving_bot_image.top - moving_Bars_right1.bottom < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.bottom - moving_Bars_right1.top < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.right - moving_Bars_right1.left < 5:
            print('score: ', score)
            sys.exit()
    if moving_bot_image.colliderect(moving_Bars_right2):
        if moving_bot_image.top - moving_Bars_right2.bottom < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.bottom - moving_Bars_right2.top < 5:
            print('score: ', score)
            sys.exit()
        if moving_bot_image.right - moving_Bars_right2.left < 5:
            print('score: ', score)
            sys.exit()

    pygame.draw.rect(SCREEN, red, moving_bot_image)


def mainGame():
    # bot positioning
    bot_x = SCREENWIDTH // 2
    bot_y = SCREENHEIGHT // 1.2
    botMove_x = -30
    botMove_y = -30
    botJumps = 0
    FPS = 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_UP):
                if 0 < bot_y < SCREENHEIGHT:
                    bot_y += botMove_y
                    moving_bot_image.y += botMove_y
                    botJumps = 1
                else:
                    sys.exit()
            if event.type == KEYDOWN and (event.key == K_LEFT):
                if 0 < bot_x < SCREENWIDTH:
                    bot_x += botMove_x
                    moving_bot_image.x += botMove_x
                    botJumps = 1
                else:
                    sys.exit()
            if event.type == KEYDOWN and (event.key == K_RIGHT):
                if 0 < bot_x < SCREENWIDTH:
                    bot_x -= botMove_x
                    moving_bot_image.x -= botMove_x
                    botJumps = 1
                else:
                    sys.exit()

        if botJumps == 1:
            botJumps = 0
        if botJumps == 0:
            bot_y += 2
            moving_bot_image.y += 2

        # increasing FPS with time
        if bot_y <= SCREENHEIGHT:
            FPS += 0.001

        isCollision()

        # Blit the images
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['bot'], (bot_x, bot_y))

        getRandomBars()

        # Updating the display everytime
        pygame.display.update()
        # Frames per second
        FPS_Clock.tick(FPS)


while True:
    welcome_screen()
    mainGame()
