import pygame
import sys
from pygame.locals import *

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Table-Tennis with Python")
screen.fill(black)

GAME_IMAGES = {
    'paddle': pygame.image.load('img/Assets/paddle.png'),
    'ball': pygame.image.load('img/Assets/ball.png'),
}

font1 = pygame.font.Font("freesansbold.ttf", 36)
font2 = pygame.font.Font("freesansbold.ttf", 16)
message1 = font1.render('Table-Tennis with Python', True, white, red)
message2 = font2.render('Press SPACE_KEY to START', True, black, white)
messageRect1 = message1.get_rect()
messageRect2 = message2.get_rect()
messageRect1.center = (300, 150)
messageRect2.center = (300, 400)

FPS_Clock = pygame.time.Clock()
print('left_player: "a" for up and "s" for down')
print('right_player: "l" for up and "k" for down')
print("Score 5 points to win")


def circle():
    pygame.draw.circle(surface=screen, radius=30, color=red, center=(300, 270 + 65 // 2), width=1)


def square():
    pygame.draw.rect(surface=screen, border_radius=1, color=red, rect=(28, 28, 545, 545), width=1)


def welcome_screen():
    paddle1_posX = 10
    paddle1_posY = 270
    paddle2_posX = 580
    paddle2_posY = 270
    ball_posX = 290
    ball_posY = 294

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE):
                return
            else:
                circle()
                square()
                screen.blit(GAME_IMAGES['ball'], (ball_posX, ball_posY))
                screen.blit(GAME_IMAGES['paddle'], (paddle1_posX, paddle1_posY))
                screen.blit(GAME_IMAGES['paddle'], (paddle2_posX, paddle2_posY))
                screen.blit(message1, messageRect1)
                screen.blit(message2, messageRect2)
        pygame.display.update()


ball = pygame.Rect(290, 294, 20, 20)

paddle1 = pygame.Rect(11, 270, 10, 73)  # left paddle
paddle2 = pygame.Rect(580, 270, 10, 73)  # right paddle

ball_x_speed = 3
ball_y_speed = 2


def paddleDraw():
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)


def paddleMove():
    if paddle1.top < 0:
        paddle1.y = 270
    elif paddle2.top < 0:
        paddle2.y = 270
    if paddle1.bottom > 600:
        paddle1.y = 270
    elif paddle2.bottom > 600:
        paddle2.y = 270


def ballDraw():
    pygame.draw.rect(screen, white, ball, border_radius=12)


def ballMove():
    global ball_x_speed, ball_y_speed

    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_y_speed *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_x_speed *= -1


def isCollide():
    global ball_x_speed, ball_y_speed

    if ball.colliderect(paddle1):
        if paddle1.right - paddle2.left < 5:
            ball_x_speed *= -1
    if ball.colliderect(paddle2):
        if paddle1.right - paddle2.left < 5:
            ball_x_speed *= -1


score_left = [0]
score_right = [0]


def updateScore():
    if ball.right >= screen_width:
        score_left[0] += 1

    if ball.left <= 0:
        score_right[0] += 1


def endGame():
    if score_left[0] >= 5 or score_right[0] >= 5:
        print("Well Played!")
        print("Right_Player: ", score_right[0], "Left_Player: ", score_left[0])
        sys.exit()


def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # paddle movements
            if event.type == KEYDOWN and (event.key == K_s):
                paddle1.y += 20

            if event.type == KEYDOWN and (event.key == K_a):
                paddle1.y -= 20

            if event.type == KEYDOWN and (event.key == K_k):
                paddle2.y += 20

            if event.type == KEYDOWN and (event.key == K_l):
                paddle2.y -= 20

        screen.fill(black)
        circle()
        square()

        paddleDraw()
        paddleMove()

        ballDraw()
        ballMove()

        isCollide()

        updateScore()
        endGame()

        pygame.display.update()
        FPS_Clock.tick(60)


welcome_screen()
mainloop()
