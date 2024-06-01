import pygame, random, sys, math
from pygame.locals import *

FPS=20
WIDTH = 630
HEIGHT = 630
x = 0
y = 0

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
SKYBLUE   = (153, 255, 255)
DARKBLUE  = (  0,  51, 255)
RED       = ( 255,  0,   0)
YELLOW    = (255, 255,   0)

START = 0
STATUS = 0
HIGHSCORE = 0

done= False

airplane1 = pygame.image.load('./images/airplane1.png')
airplane2 = pygame.image.load('./images/airplane2.png')
airplane3 = pygame.image.load('./images/airplane3.png')
airplane4 = pygame.image.load('./images/airplane4.png')
airplane = pygame.transform.scale(airplane1, (50, 50))


enemy_airplane = pygame.transform.scale(pygame.image.load('./images/airplane11.png'), (50, 50))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()
bullets = pygame.sprite.Group()

class EnemyAirplane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_airplane
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.shooting = False
        self.bullets_fired = 0
        self.max_bullets = random.randint(5, 10)
        self.retreating = False
        self.bullet_speed = random.randint(8, 15)

    def update(self):
        if not self.shooting:
            self.rect.y += self.speed
            if self.rect.y > HEIGHT // 10:
                self.shooting = True
        else:
            if self.bullets_fired >= self.max_bullets:
                self.retreating = True
            if self.retreating:
                self.rect.y -= self.speed
                if self.rect.y < -50:
                    self.kill()

    def shoot(self):
        if self.shooting and not self.retreating:
            bullet = Bullet(self.rect.x + 20, self.rect.y + 50, self.bullet_speed)
            bullets.add(bullet)
            self.bullets_fired += 1

enemies = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

coins = pygame.sprite.Group()
            

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
    global direction, START, x, y, done, bullets, enemies, STATUS, FPS

    direction='up'
    airplane = pygame.transform.scale(airplane1, (75, 75))
    START=1
    x=270
    y= HEIGHT-120
    score = 0
    done = False
    bullets.empty()
    enemies.empty()
    coins.empty()

    bullet_timer = 0
    enemy_spawn_timer = 0
    coin_spawn_timer = 0
    
    while not done:
        FPSCLOCK.tick(FPS)
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
            STATUS = 1
            done = True


        player_rect = pygame.Rect(x, y, 50, 50)
        DISPLAYSURF.blit(airplane, (x, y))

        bullet_timer += 1
        enemy_spawn_timer += 1
        coin_spawn_timer += 1

        if bullet_timer > 20:
            for enemy in enemies:
                enemy.shoot()
            bullet_timer = 0

        if enemy_spawn_timer > random.randint(50, 150):
            if len(enemies) < 4:
                attempts = 0
                while attempts < 10 and len(enemies) < 4:
                    enemy_x = random.randint(0, WIDTH - 50)
                    enemy_y = random.randint(-100, -50)
                    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)

                    overlapping = any(enemy.rect.colliderect(enemy_rect) for enemy in enemies)
                    if not overlapping:
                        enemy = EnemyAirplane(enemy_x, enemy_y)
                        enemies.add(enemy)
                    attempts += 1
            enemy_spawn_timer = 0

        if coin_spawn_timer > random.randint(100, 300):
            coin_x = random.randint(50, WIDTH - 50)
            coin_y = random.randint(300, HEIGHT - 70)
            coin = Coin(coin_x, coin_y)
            coins.add(coin)
            coin_spawn_timer = 0

        bullets.update()
        bullets.draw(DISPLAYSURF)

        enemies.update()
        enemies.draw(DISPLAYSURF)

        coins.update()
        coins.draw(DISPLAYSURF)

        for bullet in bullets:
            if bullet.rect.colliderect(player_rect):
                STATUS = 2
                done = True

        if any(enemy.rect.colliderect(player_rect) for enemy in enemies):
            STATUS=3
            done = True

        collected_coins = [coin for coin in coins if coin.rect.colliderect(player_rect)]
        for coin in collected_coins:
            score += 1
            if score % 5 == 0:
                FPS +=1
            coin.kill()

        drawScore(score, FPS)
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
    elif STATUS == 2:
        reasonSurf = gameOverFont3.render('You were attacked by the enemy', True, BLACK)
    elif STATUS == 3:
        reasonSurf = gameOverFont3.render('You hit enemies!', True, BLACK)
        
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (WIDTH / 2, 50)
    overRect = overSurf.get_rect()
    overRect.midtop = (WIDTH/2, gameRect.height +35)
    
    reasonRect = reasonSurf.get_rect()
    reasonRect.midtop=(WIDTH/2, 350)

    DISPLAYSURF.blit(airplane, (x, y))
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(reasonSurf, reasonRect)
    DISPLAYSURF.blit(overSurf, overRect)
    
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    degrees1 = 0
    while True:
        DISPLAYSURF.fill(SKYBLUE)
        DISPLAYSURF.blit(airplane, (x, y))
        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(reasonSurf, reasonRect)
        
        rotatedSurf3 = pygame.transform.rotate(overSurf, degrees1)
        rotatedRect3 = rotatedSurf3.get_rect()
        rotatedRect3.midtop = (WIDTH / 2, gameRect.height + 10 + 25)
        DISPLAYSURF.blit(rotatedSurf3, rotatedRect3)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 10

def drawScore(score, fps):
    scoreSurf = BASICFONT.render('Score: %d' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    scoreSurf = BASICFONT.render('FPS: %d' % (fps), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WIDTH - 120, 40)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
        
    

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
