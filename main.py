import pygame, random, sys
from pygame.locals import *

FPS=13
WIDTH = 630
HEIGHT = 630
x = 0
y = 0

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
SKYBLUE   = (153, 255, 255)
DARKBLUE  = (  0,  51, 255)

START = 0
STATUS = 0


done= False

airplane1 = pygame.image.load('./images/airplane1.png')
airplane2 = pygame.image.load('./images/airplane2.png')
airplane3 = pygame.image.load('./images/airplane3.png')
airplane4 = pygame.image.load('./images/airplane4.png')
airplane = pygame.transform.scale(airplane1, (75, 75))


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
        showGameOver()


def runGame():
    global airplane1, airplane2, airplane3, airplane4, airplane
    global direction, START, x, y
    
    direction='up'
    airplane = pygame.transform.scale(airplane1, (75, 75))
    START=1
    x=270
    y= HEIGHT-120

    while not done:
        FPSCLOCK.tick(15)
        DISPLAYSURF.fill(SKYBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    airplane = pygame.transform.scale(airplane1, (75, 75))
                    direction = 'up'
                elif event.key ==pygame.K_DOWN:
                    airplane = pygame.transform.scale(airplane3, (75, 75))
                    direction = 'down'
                elif event.key ==pygame.K_RIGHT:
                    airplane = pygame.transform.scale(airplane2, (75, 75))
                    direction = 'right'
                elif event.key ==pygame.K_LEFT:
                    airplane = pygame.transform.scale(airplane4, (75, 75))
                    direction = 'left'
        if direction == 'up':
            y-=20
        elif direction == 'down':
            y+=20
        elif direction == 'left':
            x-=20
        elif direction == 'right':
            x+=20
        
        if x>550 or x<0 or y>550 or y<0:
            return
        
        DISPLAYSURF.blit(airplane,(x,y))
        pygame.display.update()


def drawPressKeyMsg():
    if START==0:
        pressKeySurf = BASICFONT.render('Press any key to play.', True, BLACK)
    if START==1:
        pressKeySurf = BASICFONT.render('Press any key to replay.', True, BLACK)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WIDTH - 220, HEIGHT - 30)
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
    titleSurf2 = titleFont.render('Flying an airplane!', True, BLACK)

    degrees1 = 0
    while True:
        DISPLAYSURF.fill(SKYBLUE)
        
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


def showGameOver():
    gameOverFont1 = pygame.font.Font('freesansbold.ttf', 100)
    gameOverFont2 = pygame.font.Font('freesansbold.ttf', 70)
    gameOverFont3 = pygame.font.Font('freesansbold.ttf', 20)

    gameSurf = gameOverFont1.render('Game', True, BLACK)
    overSurf = gameOverFont2.render('Over', True, BLACK)
    reasonSurf = gameOverFont3.render('You hit the wall!', True, BLACK)
    if STATUS == 1:
        reasonSurf = gameOverFont3.render('You hit the wall!', True, BLACK)
        
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (WIDTH / 2, 50)
    overRect = overSurf.get_rect()
    overRect.midtop = (WIDTH/2, gameRect.height +35)
    
    reasonRect = reasonSurf.get_rect()
    reasonRect.midtop=(WIDTH/2, 350)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(reasonSurf,reasonRect)
    DISPLAYSURF.blit(overSurf, overRect)
    DISPLAYSURF.blit(airplane,(x,y))
    
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    degrees1 = 0
    while True:
        DISPLAYSURF.fill(SKYBLUE)
        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(reasonSurf,reasonRect)
        DISPLAYSURF.blit(airplane,(x,y))
        
        rotatedSurf3 = pygame.transform.rotate(overSurf, degrees1)
        rotatedRect3 = rotatedSurf3.get_rect()
        rotatedRect3.midtop = (WIDTH / 2, gameRect.height + 10 + 25)
        DISPLAYSURF.blit(rotatedSurf3, rotatedRect3)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 10
        
    

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
