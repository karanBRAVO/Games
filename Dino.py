# import statements
import pygame
import sys
from pygame.locals import *
import random

# initializing pygame
pygame.init()
pygame.mixer.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (240, 240, 240)

# window set-up
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dino-Game with PYTHON")
clock = pygame.time.Clock()

# Text-Message
font1 = pygame.font.Font("freesansbold.ttf", 36)
font2 = pygame.font.Font("freesansbold.ttf", 16)
font3 = pygame.font.Font("freesansbold.ttf", 18)
font4 = pygame.font.SysFont('monospace', 50, True, False)

# messages on game window
message1 = font1.render('Dino_Game with Python', True, white, black)
messageRect1 = message1.get_rect()
messageRect1.center = (screen_width // 2, screen_height // 3)

message2 = font2.render('Press SPACE_KEY to START', True, black, white)
messageRect2 = message2.get_rect()
messageRect2.center = (screen_width // 2, screen_height // 1.5)

# Images
game_sprites = {
    'dino': pygame.image.load('img/Assets/dino.png'),
    'cloud1': pygame.image.load('img/Assets/bg1.png'),
    'cloud2': pygame.image.load('img/Assets/bg2.png'),
    'gameOver': pygame.image.load('img/Assets/gameOver.png'),
    'large_obstacle': pygame.image.load('img/Assets/large_obstacle.png'),
    'medium_obstacle': pygame.image.load('img/Assets/medium_obstacle.png'),
    'small_obstacle': pygame.image.load('img/Assets/small_obstacle.png'),
}


# welcome Screen
def welcomeScreen():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE):
                mainGame()
            else:
                screen.fill(white)
                screen.blit(message1, messageRect1)
                screen.blit(message2, messageRect2)
                screen.blit(game_sprites['dino'], (260, 160))


# Clouds
cloud1_x = 530
cloud2_x = 160
cloud3_x = 390
cloud1_y = 5
cloud2_y = 130
cloud3_y = 100

cloudVel_x = -2


def cloudMove():
    global cloudVel_x, cloud2_x, cloud1_x, cloud3_x, cloud3_y, cloud2_y, cloud1_y

    cloud1_x += cloudVel_x
    cloud2_x += cloudVel_x
    cloud3_x += cloudVel_x

    if cloud1_x <= 0:
        cloud1_x = 600
        cloud1_y = random.randrange(start=0, stop=130)
    if cloud2_x <= 0:
        cloud2_x = 600
        cloud2_y = 10 + random.randrange(start=0, stop=130)
    if cloud3_x <= 0:
        cloud3_x = 600
        cloud3_y = random.randrange(start=0, stop=130)

    screen.blit(game_sprites['cloud1'], (cloud1_x, cloud1_y))
    screen.blit(game_sprites['cloud2'], (cloud2_x, cloud2_y))
    screen.blit(game_sprites['cloud2'], (cloud3_x, cloud3_y))


# Sand
ele1_x = 10
ele2_x = 50
ele3_x = 90

ele4_x = 130
ele5_x = 170
ele6_x = 210

ele7_x = 250
ele8_x = 290
ele9_x = 330

ele10_x = 370
ele11_x = 410
ele12_x = 450

ele13_x = 490
ele14_x = 530
ele15_x = 570

eleVel_x = -4


def baseElements():
    global ele3_x, ele2_x, ele1_x, eleVel_x, ele4_x, ele5_x, ele6_x, ele7_x, ele8_x, ele9_x, \
        ele10_x, ele11_x, ele12_x, ele13_x, ele14_x, ele15_x

    ele1_x += eleVel_x
    ele2_x += eleVel_x
    ele3_x += eleVel_x

    ele4_x += eleVel_x
    ele5_x += eleVel_x
    ele6_x += eleVel_x

    ele7_x += eleVel_x
    ele8_x += eleVel_x
    ele9_x += eleVel_x

    ele10_x += eleVel_x
    ele11_x += eleVel_x
    ele12_x += eleVel_x

    ele13_x += eleVel_x
    ele14_x += eleVel_x
    ele15_x += eleVel_x

    if ele1_x <= 0:
        ele1_x = 600
    if ele2_x <= 0:
        ele2_x = 600
    if ele3_x <= 0:
        ele3_x = 600

    if ele4_x <= 0:
        ele4_x = 600
    if ele5_x <= 0:
        ele5_x = 600
    if ele6_x <= 0:
        ele6_x = 600

    if ele7_x <= 0:
        ele7_x = 600
    if ele8_x <= 0:
        ele8_x = 600
    if ele9_x <= 0:
        ele9_x = 600

    if ele10_x <= 0:
        ele10_x = 600
    if ele11_x <= 0:
        ele11_x = 600
    if ele12_x <= 0:
        ele12_x = 600

    if ele13_x <= 0:
        ele13_x = 600
    if ele14_x <= 0:
        ele14_x = 600
    if ele15_x <= 0:
        ele15_x = 600

    pygame.draw.aaline(screen, black, start_pos=(ele1_x, 300), end_pos=(ele1_x + 10, 302))
    pygame.draw.aaline(screen, black, start_pos=(ele2_x, 300), end_pos=(ele2_x - 5, 302))
    pygame.draw.line(screen, black, start_pos=(ele3_x, 300), end_pos=(ele3_x + 4, 305))

    pygame.draw.aaline(screen, black, start_pos=(ele4_x, 300), end_pos=(ele4_x + 10, 302))
    pygame.draw.aaline(screen, black, start_pos=(ele5_x, 300), end_pos=(ele5_x - 5, 302))
    pygame.draw.line(screen, black, start_pos=(ele6_x, 300), end_pos=(ele6_x + 4, 305))

    pygame.draw.aaline(screen, black, start_pos=(ele7_x, 300), end_pos=(ele7_x + 10, 302))
    pygame.draw.aaline(screen, black, start_pos=(ele8_x, 300), end_pos=(ele8_x - 5, 302))
    pygame.draw.line(screen, black, start_pos=(ele9_x, 300), end_pos=(ele9_x + 4, 308))
    pygame.draw.aaline(screen, black, start_pos=(ele10_x, 300), end_pos=(ele10_x + 10, 302))
    pygame.draw.aaline(screen, black, start_pos=(ele11_x, 300), end_pos=(ele11_x - 5, 302))
    pygame.draw.line(screen, black, start_pos=(ele12_x, 300), end_pos=(ele12_x + 4, 305))

    pygame.draw.aaline(screen, black, start_pos=(ele13_x, 300), end_pos=(ele13_x + 10, 302))
    pygame.draw.aaline(screen, black, start_pos=(ele14_x, 300), end_pos=(ele14_x - 5, 302))
    pygame.draw.line(screen, black, start_pos=(ele15_x, 300), end_pos=(ele15_x + 4, 305))


# Obstacles
obs_large_x = 390
obs_medium_x = 500
obs_small_x = 250

moving_obs_large = pygame.Rect(obs_large_x, 263, 25, 38)
moving_obs_medium = pygame.Rect(obs_medium_x, 270, 19, 32)
moving_obs_small = pygame.Rect(obs_small_x, 280, 19, 21)

obstacleVel_x = -4


def obstacles():
    global obstacleVel_x, obs_medium_x, obs_large_x, obs_small_x

    obs_medium_x += obstacleVel_x
    moving_obs_medium.x += obstacleVel_x
    obs_large_x += obstacleVel_x
    moving_obs_large.x += obstacleVel_x
    obs_small_x += obstacleVel_x
    moving_obs_small.x += obstacleVel_x

    if obs_small_x <= 0:
        obs_small_x = 620
        moving_obs_small.x = 620
    if obs_medium_x <= 0:
        obs_medium_x = 670
        moving_obs_medium.x = 670
    if obs_large_x <= 0:
        obs_large_x = 740
        moving_obs_large.x = 740

    pygame.draw.circle(screen, black, radius=5, center=(obs_large_x - 20, 292), width=1)
    pygame.draw.circle(screen, black, radius=4, center=(obs_medium_x - 40, 291), width=1)
    pygame.draw.circle(screen, black, radius=6, center=(obs_small_x - 90, 293), width=1)
    pygame.draw.rect(screen, red, moving_obs_large)
    pygame.draw.rect(screen, red, moving_obs_medium)
    pygame.draw.rect(screen, red, moving_obs_small)
    screen.blit(game_sprites['medium_obstacle'], (obs_medium_x, 270))
    screen.blit(game_sprites['small_obstacle'], (obs_small_x, 280))
    screen.blit(game_sprites['large_obstacle'], (obs_large_x, 263))


# My dino
moving_face = pygame.Rect(89, 263, 13, 8)
moving_head = pygame.Rect(89, 259, 5, 4)
moving_stomach = pygame.Rect(77, 280, 12, 11)
moving_leg_left = pygame.Rect(79, 291, 2, 8)
moving_leg_right = pygame.Rect(85, 291, 2, 8)
moving_foot_left = pygame.Rect(78, 299, 4, 3)
moving_foot_right = pygame.Rect(84, 299, 4, 3)
tailStart_y = 278
tailStop_y = 286
neckStart_y = 263
neckStop_y = 283


def dino():
    global tailStart_y, tailStop_y
    pygame.draw.rect(screen, black, moving_face, border_radius=2)  # face
    pygame.draw.rect(screen, black, moving_head, border_radius=1)  # head
    pygame.draw.rect(screen, black, moving_stomach, border_radius=3)  # stomach
    pygame.draw.polygon(screen, black, ((89, neckStart_y), (84, neckStop_y)), width=6)  # neck
    pygame.draw.aaline(screen, black, start_pos=(70, tailStart_y), end_pos=(80, tailStop_y))  # tail
    pygame.draw.rect(screen, black, moving_leg_left, border_radius=2)  # left leg
    pygame.draw.rect(screen, black, moving_leg_right, border_radius=2)  # right leg
    pygame.draw.rect(screen, black, moving_foot_left, border_radius=2)  # foot left
    pygame.draw.rect(screen, black, moving_foot_right, border_radius=2)  # foot right

    pygame.draw.line(screen, black, start_pos=(0, 292), end_pos=(600, 292), width=2)


dinoLegVelL_y = -3
dinoLegVelR_y = -3


def dino_legs_move():
    global dinoLegVelL_y, dinoLegVelR_y

    moving_leg_left.y += dinoLegVelL_y
    moving_foot_left.y += dinoLegVelL_y
    moving_leg_right.y += dinoLegVelR_y
    moving_foot_right.y += dinoLegVelL_y

    if moving_leg_right.top <= 288 or moving_leg_left.top <= 288:
        dinoLegVelL_y *= -1
        dinoLegVelR_y *= -1
    if moving_leg_right.bottom >= 296 or moving_leg_left.bottom >= 296:
        dinoLegVelL_y *= -1
        dinoLegVelR_y *= -1


# Main Loop
def mainGame():
    global tailStart_y, tailStop_y, neckStart_y, neckStop_y, obstacleVel_x, dinoLegVelL_y, \
        dinoLegVelR_y, eleVel_x, cloudVel_x, obs_medium_x, obs_large_x, obs_small_x

    dinoVel_y_up = -60
    dinoVel_y_down = 60
    score = 0
    obstacleNewVel_x = -90
    restart_rect = pygame.Rect(280, 200, 43, 45)
    gameOver = 0

    while True:
        # moving dino down as it jumps
        if moving_face.y != 263 and moving_head.y != 259 and moving_stomach.y != 280 and tailStart_y != 278 \
                and tailStop_y != 286 and neckStart_y != 263 and neckStop_y != 283 and \
                (moving_obs_medium.x - moving_stomach.x <= 60 or
                 moving_obs_small.x - moving_stomach.x <= 60 or
                 moving_obs_large.x - moving_stomach.x <= 60):
            moving_face.y += dinoVel_y_down
            moving_head.y += dinoVel_y_down
            moving_stomach.y += dinoVel_y_down
            moving_leg_left.y += dinoVel_y_down
            moving_leg_right.y += dinoVel_y_down
            moving_foot_right.y += dinoVel_y_down
            moving_foot_left.y += dinoVel_y_down
            tailStart_y += dinoVel_y_down
            tailStop_y += dinoVel_y_down
            neckStart_y += dinoVel_y_down
            neckStop_y += dinoVel_y_down
            if moving_obs_medium.x - moving_stomach.x <= 60:
                obs_medium_x += obstacleNewVel_x
                moving_obs_medium.x += obstacleNewVel_x
            elif moving_obs_large.x - moving_stomach.x <= 60:
                obs_large_x += obstacleNewVel_x
                moving_obs_large.x += obstacleNewVel_x
            elif moving_obs_small.x - moving_stomach.x <= 60:
                obs_small_x += obstacleNewVel_x
                moving_obs_small.x += obstacleNewVel_x
        elif moving_face.y != 263 and moving_head.y != 259 and moving_stomach.y != 280 and tailStart_y != 278 \
                and tailStop_y != 286 and neckStart_y != 263 and neckStop_y != 283 and \
                (moving_obs_medium.x - moving_stomach.x >= 60 or
                 moving_obs_small.x - moving_stomach.x >= 60 or
                 moving_obs_large.x - moving_stomach.x >= 60):
            moving_face.y += dinoVel_y_down
            moving_head.y += dinoVel_y_down
            moving_stomach.y += dinoVel_y_down
            moving_leg_left.y += dinoVel_y_down
            moving_leg_right.y += dinoVel_y_down
            moving_foot_right.y += dinoVel_y_down
            moving_foot_left.y += dinoVel_y_down
            tailStart_y += dinoVel_y_down
            tailStop_y += dinoVel_y_down
            neckStart_y += dinoVel_y_down
            neckStop_y += dinoVel_y_down
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_UP):
                pygame.mixer.music.load('img/Assets/dinoJump.wav')
                pygame.mixer.music.play()
                if moving_face.y == 263:
                    moving_face.y += dinoVel_y_up
                if moving_head.y == 259:
                    moving_head.y += dinoVel_y_up
                if moving_stomach.y == 280:
                    moving_stomach.y += dinoVel_y_up
                    moving_leg_left.y += dinoVel_y_up
                    moving_foot_left.y += dinoVel_y_up
                    moving_leg_right.y += dinoVel_y_up
                    moving_foot_right.y += dinoVel_y_up
                if tailStart_y == 278:
                    tailStart_y += dinoVel_y_up
                if tailStop_y == 286:
                    tailStop_y += dinoVel_y_up
                if neckStart_y == 263:
                    neckStart_y += dinoVel_y_up
                if neckStop_y == 283:
                    neckStop_y += dinoVel_y_up
            if event.type == KEYDOWN and (event.key == K_ESCAPE):
                exit()

        screen.fill(white)

        cloudMove()
        baseElements()
        obstacles()

        dino()
        dino_legs_move()

        # update score
        score += 1
        scoreBoard = font2.render('Score: ' + str(score), True, black, white)
        screen.blit(scoreBoard, (275, 350))

        # crash check
        if moving_obs_large.colliderect(moving_stomach):
            if (moving_obs_large.left - moving_stomach.right) <= 5:
                gameOver = 1
        if moving_obs_medium.colliderect(moving_stomach):
            if (moving_obs_medium.left - moving_stomach.right) <= 5:
                gameOver = 1
        if moving_obs_small.colliderect(moving_stomach):
            if (moving_obs_small.left - moving_stomach.right) <= 5:
                gameOver = 1

        if moving_obs_large.colliderect(moving_leg_right):
            if (moving_obs_large.left - moving_leg_right.right) <= 5 or \
                    (moving_obs_large.top - moving_leg_right.bottom) <= 5:
                gameOver = 1
        if moving_obs_medium.colliderect(moving_leg_right):
            if (moving_obs_medium.left - moving_leg_right.right) <= 5 or \
                    (moving_obs_medium.top - moving_leg_right.bottom):
                gameOver = 1
        if moving_obs_small.colliderect(moving_leg_right):
            if (moving_obs_small.left - moving_leg_right.right) <= 5 or \
                    (moving_obs_small.top - moving_leg_right.bottom):
                gameOver = 1

        if moving_obs_large.colliderect(moving_leg_left):
            if (moving_obs_large.left - moving_leg_left.right) <= 5 or \
                    (moving_obs_large.top - moving_leg_left.bottom) <= 5:
                gameOver = 1
        if moving_obs_medium.colliderect(moving_leg_left):
            if (moving_obs_medium.left - moving_leg_left.right) <= 5 or \
                    (moving_obs_medium.top - moving_leg_left.bottom) <= 5:
                gameOver = 1
        if moving_obs_small.colliderect(moving_leg_left):
            if (moving_obs_small.left - moving_leg_left.right) <= 5 or \
                    (moving_obs_small.top - moving_leg_left.bottom) <= 5:
                gameOver = 1

        if moving_obs_large.colliderect(moving_foot_right):
            if (moving_obs_large.left - moving_foot_right.right) <= 5 or \
                    (moving_obs_large.top - moving_foot_right.bottom) <= 5:
                gameOver = 1
        if moving_obs_medium.colliderect(moving_foot_right):
            if (moving_obs_medium.left - moving_foot_right.right) <= 5 or \
                    (moving_obs_medium.top - moving_foot_right.bottom) <= 5:
                gameOver = 1
        if moving_obs_small.colliderect(moving_foot_right):
            if (moving_obs_small.left - moving_foot_right.right) <= 5 or \
                    (moving_obs_small.top - moving_foot_right.bottom) <= 5:
                gameOver = 1

        if gameOver == 1:
            message = font4.render('Game Over', True, black, grey)
            messageRect = message.get_rect()
            messageRect.center = (300, 100)
            screen.blit(message, messageRect)
            pygame.draw.rect(screen, grey, restart_rect, border_radius=1)
            screen.blit(game_sprites['gameOver'], (280, 200))
            cloudVel_x = 0
            obstacleVel_x = 0
            eleVel_x = 0
            dinoVel_y_up = 0
            dinoLegVelL_y = 0
            dinoLegVelR_y = 0
            score -= 1
            pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    welcomeScreen()
