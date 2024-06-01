import pygame, random, sys
from pygame.locals import *

FPS=13
WIDTH = 640
HEIGHT = 640

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
SKYBLUE   = (153, 255, 255)
DARKBLUE  = (  0,  51, 255)


done= False
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

airplane1 = pygame.image.load('./images/airplane1.png')
airplane2 = pygame.image.load('./images/airplane2.png')
airplane3 = pygame.image.load('./images/airplane3.png')
airplane4 = pygame.image.load('./images/airplane4.png')
airplane = pygame.transform.scale(airplane1, (100, 100))


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
    global airplane1, airplane2, airplane3, airplane4, airplane
    x=270
    y= HEIGHT-120

    while not done:
        FPSCLOCK.tick(50)
        DISPLAYSURF.fill(SKYBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    airplane = pygame.transform.scale(airplane1, (100, 100))
                    y-=20
                elif event.key ==pygame.K_DOWN:
                    airplane = pygame.transform.scale(airplane3, (100, 100))
                    y+=20
                elif event.key ==pygame.K_RIGHT:
                    airplane = pygame.transform.scale(airplane2, (100, 100))
                    x+=20
                elif event.key ==pygame.K_LEFT:
                    airplane = pygame.transform.scale(airplane4, (100, 100))
                    x-=20
        DISPLAYSURF.blit(airplane,(x,y))
        pygame.display.update()


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
        DISPLAYSURF.fill(BLACK)
        
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
