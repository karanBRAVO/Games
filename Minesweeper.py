import time
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 100, 100)
blue = (100, 100, 255)
green = (100, 255, 100)

windowWidth = 500
windowHeight = 500

Assets = {
    'bomb': pygame.image.load("img/Assets/bomb.png"),  # 41x46
    'level1bg': pygame.image.load("img/Assets/level1bg.png"),  # 149x151
    'level2bg': pygame.image.load("img/Assets/level2bg.png"),  # 222x224
    'level3bg': pygame.image.load("img/Assets/level3bg.png"),  # 294x293
    'level4bg': pygame.image.load("img/Assets/level4bg.png"),  # 381x381
}

font1 = pygame.font.SysFont('monospace', 65, True, False)
message1 = font1.render('MINESWEEPER', True, white)
messageRect1 = message1.get_rect()
messageRect1.center = (windowWidth // 2, 482)

font2 = pygame.font.SysFont('fantasy', 40, True, False)
message2 = font2.render('Level 1', True, green)
message3 = font2.render('Level 2', True, green)
message4 = font2.render('Level 3', True, green)
message5 = font2.render('Level 4', True, green)
message6 = font2.render('Game Completed', True, blue, green)
messageRect2 = message2.get_rect()
messageRect3 = message6.get_rect()
messageRect2.center = (windowWidth // 2, 450)
messageRect3.center = (windowWidth // 2, windowHeight // 2)

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Minesweeper")
print("*** MINESWEEPER ***")

run = True

clickedWrongRect = 0

level1Cleared = 0
level1rect1Clicked = 0
level1rect2Clicked = 0
level1rect3Clicked = 0
level1rect4Clicked = 0
level1Bomb1Found = 0
level1Bomb2Found = 0

level2Cleared = 0
level2rect1Clicked = 0
level2rect2Clicked = 0
level2rect3Clicked = 0
level2rect4Clicked = 0
level2rect5Clicked = 0
level2rect6Clicked = 0
level2rect7Clicked = 0
level2rect8Clicked = 0
level2rect9Clicked = 0
level2Bomb1Found = 0
level2Bomb2Found = 0
level2Bomb3Found = 0
level2Bomb4Found = 0

level3Cleared = 0
level3rect1Clicked = 0
level3rect2Clicked = 0
level3rect3Clicked = 0
level3rect4Clicked = 0
level3rect5Clicked = 0
level3rect6Clicked = 0
level3rect7Clicked = 0
level3rect8Clicked = 0
level3rect9Clicked = 0
level3rect10Clicked = 0
level3rect11Clicked = 0
level3rect12Clicked = 0
level3rect13Clicked = 0
level3rect14Clicked = 0
level3rect15Clicked = 0
level3rect16Clicked = 0
level3Bomb1Found = 0
level3Bomb2Found = 0
level3Bomb3Found = 0
level3Bomb4Found = 0
level3Bomb5Found = 0
level3Bomb6Found = 0
level3Bomb7Found = 0
level3Bomb8Found = 0

level4Cleared = 0
level4rect1Clicked = 0
level4rect2Clicked = 0
level4rect3Clicked = 0
level4rect4Clicked = 0
level4rect5Clicked = 0
level4rect6Clicked = 0
level4rect7Clicked = 0
level4rect8Clicked = 0
level4rect9Clicked = 0
level4rect10Clicked = 0
level4rect11Clicked = 0
level4rect12Clicked = 0
level4rect13Clicked = 0
level4rect14Clicked = 0
level4rect15Clicked = 0
level4rect16Clicked = 0
level4rect17Clicked = 0
level4rect18Clicked = 0
level4rect19Clicked = 0
level4rect20Clicked = 0
level4rect21Clicked = 0
level4rect22Clicked = 0
level4rect23Clicked = 0
level4rect24Clicked = 0
level4rect25Clicked = 0
level4Bomb1Found = 0
level4Bomb2Found = 0
level4Bomb3Found = 0
level4Bomb4Found = 0
level4Bomb5Found = 0
level4Bomb6Found = 0
level4Bomb7Found = 0
level4Bomb8Found = 0
level4Bomb9Found = 0
level4Bomb10Found = 0
level4Bomb11Found = 0
level4Bomb12Found = 0
level4Bomb13Found = 0
level4Bomb14Found = 0

level1_rect1 = pygame.Rect(0, 0, 74, 74)
level1_rect2 = pygame.Rect(75, 0, 74, 74)
level1_rect3 = pygame.Rect(0, 75, 74, 74)
level1_rect4 = pygame.Rect(75, 75, 74, 74)

level2_rect1 = pygame.Rect(0, 0, 72, 72)
level2_rect2 = pygame.Rect(75, 0, 72, 72)
level2_rect3 = pygame.Rect(150, 0, 72, 72)
level2_rect4 = pygame.Rect(0, 75, 72, 72)
level2_rect5 = pygame.Rect(75, 75, 72, 72)
level2_rect6 = pygame.Rect(150, 75, 72, 72)
level2_rect7 = pygame.Rect(0, 150, 72, 72)
level2_rect8 = pygame.Rect(75, 150, 72, 72)
level2_rect9 = pygame.Rect(150, 150, 72, 72)

level3_rect1 = pygame.Rect(0, 0, 72, 72)
level3_rect2 = pygame.Rect(75, 0, 72, 72)
level3_rect3 = pygame.Rect(150, 0, 72, 72)
level3_rect4 = pygame.Rect(225, 0, 72, 72)
level3_rect5 = pygame.Rect(0, 75, 72, 72)
level3_rect6 = pygame.Rect(75, 75, 72, 72)
level3_rect7 = pygame.Rect(150, 75, 72, 72)
level3_rect8 = pygame.Rect(225, 75, 72, 72)
level3_rect9 = pygame.Rect(0, 150, 72, 72)
level3_rect10 = pygame.Rect(75, 150, 72, 72)
level3_rect11 = pygame.Rect(150, 150, 72, 72)
level3_rect12 = pygame.Rect(226, 150, 72, 72)
level3_rect13 = pygame.Rect(0, 225, 72, 72)
level3_rect14 = pygame.Rect(75, 225, 72, 72)
level3_rect15 = pygame.Rect(150, 225, 72, 72)
level3_rect16 = pygame.Rect(225, 225, 72, 72)

level4_rect1 = pygame.Rect(0, 0, 72, 72)
level4_rect2 = pygame.Rect(75, 0, 72, 72)
level4_rect3 = pygame.Rect(150, 0, 72, 72)
level4_rect4 = pygame.Rect(225, 0, 72, 72)
level4_rect5 = pygame.Rect(300, 0, 72, 72)
level4_rect6 = pygame.Rect(0, 75, 72, 72)
level4_rect7 = pygame.Rect(75, 75, 72, 72)
level4_rect8 = pygame.Rect(150, 75, 72, 72)
level4_rect9 = pygame.Rect(225, 75, 72, 72)
level4_rect10 = pygame.Rect(300, 75, 72, 72)
level4_rect11 = pygame.Rect(0, 150, 72, 72)
level4_rect12 = pygame.Rect(75, 150, 72, 72)
level4_rect13 = pygame.Rect(150, 150, 72, 72)
level4_rect14 = pygame.Rect(225, 150, 72, 72)
level4_rect15 = pygame.Rect(300, 150, 72, 72)
level4_rect16 = pygame.Rect(0, 225, 72, 72)
level4_rect17 = pygame.Rect(75, 225, 72, 72)
level4_rect18 = pygame.Rect(150, 225, 72, 72)
level4_rect19 = pygame.Rect(225, 225, 72, 72)
level4_rect20 = pygame.Rect(300, 225, 72, 72)
level4_rect21 = pygame.Rect(0, 300, 72, 72)
level4_rect22 = pygame.Rect(75, 300, 72, 72)
level4_rect23 = pygame.Rect(150, 300, 72, 72)
level4_rect24 = pygame.Rect(225, 300, 72, 72)
level4_rect25 = pygame.Rect(300, 300, 72, 72)


def level1():
    global level1Cleared, level1rect2Clicked, level1rect4Clicked, level1rect1Clicked, level1rect3Clicked, \
        level1Bomb1Found, level1Bomb2Found, clickedWrongRect, run

    window.blit(message2, messageRect2)

    window.blit(Assets['bomb'], (level1_rect1.x + 20, level1_rect1.y + 20))
    window.blit(Assets['bomb'], (level1_rect3.x + 20, level1_rect3.y + 20))

    window.blit(Assets['level1bg'], (0, 0))

    for mouseEvent in pygame.event.get():
        if mouseEvent.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if level1_rect1.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
                level1rect1Clicked = 1
            elif level1_rect2.collidepoint(mouse_x, mouse_y):
                level1rect2Clicked = 1
            elif level1_rect3.collidepoint(mouse_x, mouse_y):
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
                level1rect3Clicked = 1
            elif level1_rect4.collidepoint(mouse_x, mouse_y):
                level1rect4Clicked = 1

    if level1rect1Clicked == 1:
        pygame.draw.rect(window, red, level1_rect1)
        window.blit(Assets['bomb'], (level1_rect1.x + 20, level1_rect1.y + 20))
        level1Bomb1Found = 1
    if level1rect3Clicked == 1:
        pygame.mixer.music.load('img/Assets/explosion.wav')
        pygame.mixer.music.play()
        pygame.draw.rect(window, red, level1_rect3)
        window.blit(Assets['bomb'], (level1_rect3.x + 20, level1_rect3.y + 20))
        level1Bomb2Found = 1
    if level1Bomb1Found == 1 and level1Bomb2Found == 1:
        pygame.mixer.music.load('img/Assets/levelComplete.wav')
        pygame.mixer.music.play()
        print("Level 1 Cleared")
        pygame.display.flip()
        pygame.event.pump()
        time.sleep(2)
        level1Cleared = 1

    if level1rect2Clicked == 1:
        pygame.draw.rect(window, red, level1_rect2)
        clickedWrongRect = 1
    if level1rect4Clicked == 1:
        pygame.draw.rect(window, red, level1_rect4)
        clickedWrongRect = 1
    if clickedWrongRect == 1:
        pygame.mixer.music.load('img/Assets/loss.wav')
        pygame.mixer.music.play()
        pygame.display.flip()
        pygame.event.pump()
        print("Oops! Clicked at wrong place")
        time.sleep(2)
        run = False


def level2():
    global level2Cleared, level2rect1Clicked, level2rect2Clicked, level2rect3Clicked, level2rect4Clicked, \
        level2rect5Clicked, level2rect6Clicked, level2rect7Clicked, level2rect8Clicked, level2rect9Clicked, \
        level2Bomb1Found, level2Bomb2Found, level2Bomb3Found, level2Bomb4Found, clickedWrongRect, run

    window.blit(message3, messageRect2)

    window.blit(Assets['bomb'], (level2_rect1.x, level2_rect1.y))
    window.blit(Assets['bomb'], (level2_rect6.x, level2_rect6.y))
    window.blit(Assets['bomb'], (level2_rect8.x, level2_rect8.y))

    window.blit(Assets['level2bg'], (0, 0))

    for mouseEvent in pygame.event.get():
        if mouseEvent.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if level2_rect1.collidepoint(mouse_x, mouse_y):
                level2rect1Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect2.collidepoint(mouse_x, mouse_y):
                level2rect2Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect3.collidepoint(mouse_x, mouse_y):
                level2rect3Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect4.collidepoint(mouse_x, mouse_y):
                level2rect4Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect5.collidepoint(mouse_x, mouse_y):
                level2rect5Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect6.collidepoint(mouse_x, mouse_y):
                level2rect6Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect7.collidepoint(mouse_x, mouse_y):
                level2rect7Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect8.collidepoint(mouse_x, mouse_y):
                level2rect8Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level2_rect9.collidepoint(mouse_x, mouse_y):
                level2rect9Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()

    if level2rect1Clicked == 1:
        pygame.draw.rect(window, red, level2_rect1)
        window.blit(Assets['bomb'], (level2_rect1.x + 20, level2_rect1.y + 20))
        level2Bomb1Found = 1
    if level2rect4Clicked == 1:
        pygame.draw.rect(window, red, level2_rect4)
        window.blit(Assets['bomb'], (level2_rect4.x + 20, level2_rect4.y + 20))
        level2Bomb2Found = 1
    if level2rect6Clicked == 1:
        pygame.draw.rect(window, red, level2_rect6)
        window.blit(Assets['bomb'], (level2_rect6.x + 20, level2_rect6.y + 20))
        level2Bomb3Found = 1
    if level2rect8Clicked == 1:
        pygame.draw.rect(window, red, level2_rect8)
        window.blit(Assets['bomb'], (level2_rect8.x + 20, level2_rect8.y + 20))
        level2Bomb4Found = 1
    if level2Bomb1Found == 1 and level2Bomb2Found == 1 and level2Bomb3Found == 1 and level2Bomb4Found == 1:
        pygame.mixer.music.load('img/Assets/levelComplete.wav')
        pygame.mixer.music.play()
        print("Level 2 Cleared")
        pygame.display.flip()
        pygame.event.pump()
        time.sleep(1)
        level2Cleared = 1

    if level2rect2Clicked == 1:
        pygame.draw.rect(window, red, level2_rect2)
        clickedWrongRect = 1
    if level2rect3Clicked == 1:
        pygame.draw.rect(window, red, level2_rect3)
        clickedWrongRect = 1
    if level2rect5Clicked == 1:
        pygame.draw.rect(window, red, level2_rect5)
        clickedWrongRect = 1
    if level2rect7Clicked == 1:
        pygame.draw.rect(window, red, level2_rect7)
        clickedWrongRect = 1
    if level2rect9Clicked == 1:
        pygame.draw.rect(window, red, level2_rect9)
        clickedWrongRect = 1
    if clickedWrongRect == 1:
        pygame.mixer.music.load('img/Assets/loss.wav')
        pygame.mixer.music.play()
        pygame.display.flip()
        pygame.event.pump()
        print("Oops! Clicked at wrong place")
        time.sleep(2)
        run = False


def level3():
    global level3Cleared, level3rect1Clicked, level3rect2Clicked, level3rect3Clicked, level3rect4Clicked, \
        level3rect5Clicked, level3rect6Clicked, level3rect7Clicked, level3rect8Clicked, level3rect9Clicked, \
        level3rect10Clicked, level3rect11Clicked, level3rect12Clicked, level3rect13Clicked, level3rect14Clicked, \
        level3rect15Clicked, level3rect16Clicked, level3Bomb1Found, level3Bomb2Found, level3Bomb3Found, \
        level3Bomb4Found, level3Bomb5Found, level3Bomb6Found, level3Bomb7Found, level3Bomb8Found, clickedWrongRect, run

    window.blit(message4, messageRect2)

    window.blit(Assets['bomb'], (level3_rect1.x, level3_rect1.y))
    window.blit(Assets['bomb'], (level3_rect2.x, level3_rect2.y))
    window.blit(Assets['bomb'], (level3_rect4.x, level3_rect4.y))
    window.blit(Assets['bomb'], (level3_rect5.x, level3_rect5.y))
    window.blit(Assets['bomb'], (level3_rect6.x, level3_rect6.y))
    window.blit(Assets['bomb'], (level3_rect12.x, level3_rect12.y))
    window.blit(Assets['bomb'], (level3_rect15.x, level3_rect15.y))
    window.blit(Assets['bomb'], (level3_rect16.x, level3_rect16.y))

    window.blit(Assets['level3bg'], (0, 0))

    for mouseEvent in pygame.event.get():
        if mouseEvent.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if level3_rect1.collidepoint(mouse_x, mouse_y):
                level3rect1Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect2.collidepoint(mouse_x, mouse_y):
                level3rect2Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect3.collidepoint(mouse_x, mouse_y):
                level3rect3Clicked = 1
            elif level3_rect4.collidepoint(mouse_x, mouse_y):
                level3rect4Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect5.collidepoint(mouse_x, mouse_y):
                level3rect5Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect6.collidepoint(mouse_x, mouse_y):
                level3rect6Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect7.collidepoint(mouse_x, mouse_y):
                level3rect7Clicked = 1
            elif level3_rect8.collidepoint(mouse_x, mouse_y):
                level3rect8Clicked = 1
            elif level3_rect9.collidepoint(mouse_x, mouse_y):
                level3rect9Clicked = 1
            elif level3_rect10.collidepoint(mouse_x, mouse_y):
                level3rect10Clicked = 1
            elif level3_rect11.collidepoint(mouse_x, mouse_y):
                level3rect11Clicked = 1
            elif level3_rect12.collidepoint(mouse_x, mouse_y):
                level3rect12Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect13.collidepoint(mouse_x, mouse_y):
                level3rect13Clicked = 1
            elif level3_rect14.collidepoint(mouse_x, mouse_y):
                level3rect14Clicked = 1
            elif level3_rect15.collidepoint(mouse_x, mouse_y):
                level3rect15Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level3_rect16.collidepoint(mouse_x, mouse_y):
                level3rect16Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()

    if level3rect1Clicked == 1:
        pygame.draw.rect(window, red, level3_rect1)
        window.blit(Assets['bomb'], (level3_rect1.x + 18, level3_rect1.y + 18))
        level3Bomb1Found = 1
    if level3rect2Clicked == 1:
        pygame.draw.rect(window, red, level3_rect2)
        window.blit(Assets['bomb'], (level3_rect2.x + 18, level3_rect2.y + 18))
        level3Bomb2Found = 1
    if level3rect4Clicked == 1:
        pygame.draw.rect(window, red, level3_rect4)
        window.blit(Assets['bomb'], (level3_rect4.x + 18, level3_rect4.y + 18))
        level3Bomb3Found = 1
    if level3rect5Clicked == 1:
        pygame.draw.rect(window, red, level3_rect5)
        window.blit(Assets['bomb'], (level3_rect5.x + 18, level3_rect5.y + 18))
        level3Bomb4Found = 1
    if level3rect6Clicked == 1:
        pygame.draw.rect(window, red, level3_rect6)
        window.blit(Assets['bomb'], (level3_rect6.x + 18, level3_rect6.y + 18))
        level3Bomb5Found = 1
    if level3rect12Clicked == 1:
        pygame.draw.rect(window, red, level3_rect12)
        window.blit(Assets['bomb'], (level3_rect12.x + 18, level3_rect12.y + 18))
        level3Bomb6Found = 1
    if level3rect15Clicked == 1:
        pygame.draw.rect(window, red, level3_rect15)
        window.blit(Assets['bomb'], (level3_rect15.x + 18, level3_rect15.y + 18))
        level3Bomb7Found = 1
    if level3rect16Clicked == 1:
        pygame.draw.rect(window, red, level3_rect16)
        window.blit(Assets['bomb'], (level3_rect16.x + 18, level3_rect16.y + 18))
        level3Bomb8Found = 1
    if level3Bomb1Found == 1 and level3Bomb2Found == 1 and level3Bomb3Found == 1 and level3Bomb4Found == 1 \
            and level3Bomb5Found == 1 and level3Bomb6Found == 1 and level3Bomb7Found == 1 and level3Bomb8Found == 1:
        pygame.mixer.music.load('img/Assets/levelComplete.wav')
        pygame.mixer.music.play()
        print("Level 3 Cleared")
        pygame.display.flip()
        pygame.event.pump()
        time.sleep(1)
        level3Cleared = 1

    if level3rect3Clicked == 1:
        pygame.draw.rect(window, red, level3_rect3)
        clickedWrongRect = 1
    if level3rect7Clicked == 1:
        pygame.draw.rect(window, red, level3_rect7)
        clickedWrongRect = 1
    if level3rect8Clicked == 1:
        pygame.draw.rect(window, red, level3_rect8)
        clickedWrongRect = 1
    if level3rect9Clicked == 1:
        pygame.draw.rect(window, red, level3_rect9)
        clickedWrongRect = 1
    if level3rect10Clicked == 1:
        pygame.draw.rect(window, red, level3_rect10)
        clickedWrongRect = 1
    if level3rect11Clicked == 1:
        pygame.draw.rect(window, red, level3_rect11)
        clickedWrongRect = 1
    if level3rect13Clicked == 1:
        pygame.draw.rect(window, red, level3_rect13)
        clickedWrongRect = 1
    if level3rect14Clicked == 1:
        pygame.draw.rect(window, red, level3_rect14)
        clickedWrongRect = 1
    if clickedWrongRect == 1:
        pygame.mixer.music.load('img/Assets/loss.wav')
        pygame.mixer.music.play()
        pygame.display.flip()
        pygame.event.pump()
        print("Oops! Clicked at wrong place")
        time.sleep(2)
        run = False


def level4():
    global level4Cleared, level4rect1Clicked, level4rect2Clicked, level4rect3Clicked, level4rect4Clicked, \
        level4rect5Clicked, level4rect6Clicked, level4rect7Clicked, level4rect8Clicked, level4rect9Clicked, \
        level4rect10Clicked, level4rect11Clicked, level4rect12Clicked, level4rect13Clicked, level4rect14Clicked, \
        level4rect15Clicked, level4rect16Clicked, level4rect17Clicked, level4rect18Clicked, level4rect19Clicked, \
        level4rect20Clicked, level4rect21Clicked, level4rect22Clicked, level4rect23Clicked, level4rect24Clicked, \
        level4rect25Clicked, level4Bomb1Found, level4Bomb2Found, level4Bomb3Found, level4Bomb4Found, level4Bomb5Found, \
        level4Bomb6Found, level4Bomb7Found, level4Bomb8Found, level4Bomb9Found, level4Bomb10Found, level4Bomb11Found, \
        level4Bomb12Found, level4Bomb13Found, level4Bomb14Found, clickedWrongRect, run

    window.blit(message5, messageRect2)

    window.blit(Assets['bomb'], (level4_rect1.x, level4_rect1.y))
    window.blit(Assets['bomb'], (level4_rect3.x, level4_rect3.y))
    window.blit(Assets['bomb'], (level4_rect4.x, level4_rect4.y))
    window.blit(Assets['bomb'], (level4_rect6.x, level4_rect6.y))
    window.blit(Assets['bomb'], (level4_rect9.x, level4_rect9.y))
    window.blit(Assets['bomb'], (level4_rect11.x, level4_rect11.y))
    window.blit(Assets['bomb'], (level4_rect13.x, level4_rect13.y))
    window.blit(Assets['bomb'], (level4_rect15.x, level4_rect15.y))
    window.blit(Assets['bomb'], (level4_rect16.x, level4_rect16.y))
    window.blit(Assets['bomb'], (level4_rect18.x, level4_rect18.y))
    window.blit(Assets['bomb'], (level4_rect19.x, level4_rect19.y))
    window.blit(Assets['bomb'], (level4_rect21.x, level4_rect21.y))
    window.blit(Assets['bomb'], (level4_rect23.x, level4_rect23.y))
    window.blit(Assets['bomb'], (level4_rect25.x, level4_rect25.y))

    window.blit(Assets['level4bg'], (0, 0))

    for mouseEvent in pygame.event.get():
        if mouseEvent.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if level4_rect1.collidepoint(mouse_x, mouse_y):
                level4rect1Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect2.collidepoint(mouse_x, mouse_y):
                level4rect2Clicked = 1
            elif level4_rect3.collidepoint(mouse_x, mouse_y):
                level4rect3Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect4.collidepoint(mouse_x, mouse_y):
                level4rect4Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect5.collidepoint(mouse_x, mouse_y):
                level4rect5Clicked = 1
            elif level4_rect6.collidepoint(mouse_x, mouse_y):
                level4rect6Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect7.collidepoint(mouse_x, mouse_y):
                level4rect7Clicked = 1
            elif level4_rect8.collidepoint(mouse_x, mouse_y):
                level4rect8Clicked = 1
            elif level4_rect9.collidepoint(mouse_x, mouse_y):
                level4rect9Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect10.collidepoint(mouse_x, mouse_y):
                level4rect10Clicked = 1
            elif level4_rect11.collidepoint(mouse_x, mouse_y):
                level4rect11Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect12.collidepoint(mouse_x, mouse_y):
                level4rect12Clicked = 1
            elif level4_rect13.collidepoint(mouse_x, mouse_y):
                level4rect13Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect14.collidepoint(mouse_x, mouse_y):
                level4rect14Clicked = 1
            elif level4_rect15.collidepoint(mouse_x, mouse_y):
                level4rect15Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect16.collidepoint(mouse_x, mouse_y):
                level4rect16Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect17.collidepoint(mouse_x, mouse_y):
                level4rect17Clicked = 1
            elif level4_rect18.collidepoint(mouse_x, mouse_y):
                level4rect18Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect19.collidepoint(mouse_x, mouse_y):
                level4rect19Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect20.collidepoint(mouse_x, mouse_y):
                level4rect20Clicked = 1
            elif level4_rect21.collidepoint(mouse_x, mouse_y):
                level4rect21Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect22.collidepoint(mouse_x, mouse_y):
                level4rect22Clicked = 1
            elif level4_rect23.collidepoint(mouse_x, mouse_y):
                level4rect23Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()
            elif level4_rect24.collidepoint(mouse_x, mouse_y):
                level4rect24Clicked = 1
            elif level4_rect25.collidepoint(mouse_x, mouse_y):
                level4rect25Clicked = 1
                pygame.mixer.music.load('img/Assets/explosion.wav')
                pygame.mixer.music.play()

    if level4rect1Clicked == 1:
        pygame.draw.rect(window, red, level4_rect1)
        window.blit(Assets['bomb'], (level4_rect1.x + 18, level4_rect1.y + 18))
        level4Bomb1Found = 1
    if level4rect3Clicked == 1:
        pygame.draw.rect(window, red, level4_rect3)
        window.blit(Assets['bomb'], (level4_rect3.x + 18, level4_rect3.y + 18))
        level4Bomb2Found = 1
    if level4rect4Clicked == 1:
        pygame.draw.rect(window, red, level4_rect4)
        window.blit(Assets['bomb'], (level4_rect4.x + 18, level4_rect4.y + 18))
        level4Bomb3Found = 1
    if level4rect6Clicked == 1:
        pygame.draw.rect(window, red, level4_rect6)
        window.blit(Assets['bomb'], (level4_rect6.x + 18, level4_rect6.y + 18))
        level4Bomb4Found = 1
    if level4rect9Clicked == 1:
        pygame.draw.rect(window, red, level4_rect9)
        window.blit(Assets['bomb'], (level4_rect9.x + 18, level4_rect9.y + 18))
        level4Bomb5Found = 1
    if level4rect11Clicked == 1:
        pygame.draw.rect(window, red, level4_rect11)
        window.blit(Assets['bomb'], (level4_rect11.x + 18, level4_rect11.y + 18))
        level4Bomb6Found = 1
    if level4rect13Clicked == 1:
        pygame.draw.rect(window, red, level4_rect13)
        window.blit(Assets['bomb'], (level4_rect13.x + 18, level4_rect13.y + 18))
        level4Bomb7Found = 1
    if level4rect15Clicked == 1:
        pygame.draw.rect(window, red, level4_rect15)
        window.blit(Assets['bomb'], (level4_rect15.x + 18, level4_rect15.y + 18))
        level4Bomb8Found = 1
    if level4rect16Clicked == 1:
        pygame.draw.rect(window, red, level4_rect16)
        window.blit(Assets['bomb'], (level4_rect16.x + 18, level4_rect16.y + 18))
        level4Bomb9Found = 1
    if level4rect18Clicked == 1:
        pygame.draw.rect(window, red, level4_rect18)
        window.blit(Assets['bomb'], (level4_rect18.x + 18, level4_rect18.y + 18))
        level4Bomb10Found = 1
    if level4rect19Clicked == 1:
        pygame.draw.rect(window, red, level4_rect19)
        window.blit(Assets['bomb'], (level4_rect19.x + 18, level4_rect19.y + 18))
        level4Bomb11Found = 1
    if level4rect21Clicked == 1:
        pygame.draw.rect(window, red, level4_rect21)
        window.blit(Assets['bomb'], (level4_rect21.x + 18, level4_rect21.y + 18))
        level4Bomb12Found = 1
    if level4rect23Clicked == 1:
        pygame.draw.rect(window, red, level4_rect23)
        window.blit(Assets['bomb'], (level4_rect23.x + 18, level4_rect23.y + 18))
        level4Bomb13Found = 1
    if level4rect25Clicked == 1:
        pygame.draw.rect(window, red, level4_rect25)
        window.blit(Assets['bomb'], (level4_rect25.x + 18, level4_rect25.y + 18))
        level4Bomb14Found = 1
    if level4Bomb1Found == 1 and level4Bomb2Found == 1 and level4Bomb3Found == 1 and level4Bomb4Found == 1 \
            and level4Bomb5Found == 1 and level4Bomb6Found == 1 and level4Bomb7Found == 1 and level4Bomb8Found == 1 \
            and level4Bomb9Found == 1 and level4Bomb10Found == 1 and level4Bomb11Found == 1 and level4Bomb12Found == 1 \
            and level4Bomb13Found == 1 and level4Bomb14Found == 1:
        pygame.mixer.music.load('img/Assets/levelComplete.wav')
        pygame.mixer.music.play()
        print("Level 4 Cleared")
        print("Congratulations, You won")
        print("You have high concentration Power.")
        pygame.display.flip()
        pygame.event.pump()
        time.sleep(1)
        level4Cleared = 1

    if level4rect2Clicked == 1:
        pygame.draw.rect(window, red, level4_rect2)
        clickedWrongRect = 1
    if level4rect5Clicked == 1:
        pygame.draw.rect(window, red, level4_rect5)
        clickedWrongRect = 1
    if level4rect7Clicked == 1:
        pygame.draw.rect(window, red, level4_rect7)
        clickedWrongRect = 1
    if level4rect8Clicked == 1:
        pygame.draw.rect(window, red, level4_rect8)
        clickedWrongRect = 1
    if level4rect10Clicked == 1:
        pygame.draw.rect(window, red, level4_rect10)
        clickedWrongRect = 1
    if level4rect12Clicked == 1:
        pygame.draw.rect(window, red, level4_rect12)
        clickedWrongRect = 1
    if level4rect14Clicked == 1:
        pygame.draw.rect(window, red, level4_rect14)
        clickedWrongRect = 1
    if level4rect17Clicked == 1:
        pygame.draw.rect(window, red, level4_rect17)
        clickedWrongRect = 1
    if level4rect20Clicked == 1:
        pygame.draw.rect(window, red, level4_rect20)
        clickedWrongRect = 1
    if level4rect22Clicked == 1:
        pygame.draw.rect(window, red, level4_rect22)
        clickedWrongRect = 1
    if level4rect24Clicked == 1:
        pygame.draw.rect(window, red, level4_rect24)
        clickedWrongRect = 1
    if clickedWrongRect == 1:
        pygame.mixer.music.load('img/Assets/loss.wav')
        pygame.mixer.music.play()
        pygame.display.flip()
        pygame.event.pump()
        print("Oops! Clicked at wrong place")
        time.sleep(2)
        run = False


while run:
    pygame.display.update()
    window.fill(black)
    window.blit(message1, messageRect1)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN and (event.key == K_ESCAPE):
            run = False
    if level1Cleared == 0:
        level1()
    if level2Cleared == 0 and level1Cleared == 1:
        level2()
    if level3Cleared == 0 and level1Cleared == 1 and level2Cleared == 1:
        level3()
    if level4Cleared == 0 and level1Cleared == 1 and level2Cleared == 1 and level3Cleared == 1:
        level4()
    if level4Cleared == 1 and level3Cleared == 1 and level3Cleared == 1 and level1Cleared == 1:
        print("Game Completed.")
        window.blit(message6, messageRect3)
        pygame.display.flip()
        pygame.event.pump()
        time.sleep(5)
        run = False
pygame.quit()
