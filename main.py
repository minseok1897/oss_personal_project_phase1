import pygame, random, sys
from pygame.locals import *

FPS=13
WIDTH = 640
HEIGHT = 640

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
SKYBLUE   = (153, 255, 255)
DARKBLUE  = (  0,  51, 255)

BGCOLOR = BLACK

done= False

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('Flying an airplane')

    showStartScreen()
    while True:
        runGame()
        pygame.quit()


def runGame():
    global done
    while not done:
        FPSCLOCK.tick(10)
        DISPLAYSURF.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()


def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WIDTH - 200, HEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
    

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 50)
    titleSurf1 = titleFont.render('Flying an airplane!', True, WHITE, DARKBLUE)
    titleSurf2 = titleFont.render('Flying an airplane!', True, SKYBLUE)

    degrees1 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WIDTH / 2, HEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        titleRect2 = titleSurf2.get_rect()
        titleRect2.center = (WIDTH / 2, HEIGHT / 2)
        DISPLAYSURF.blit(titleSurf2, titleRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 4
    

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
