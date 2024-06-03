# ??������ ����(Flying an airplane) ������Ʈ
�� ������Ʈ�� ������ ����(Flying an airplane) ����� ������Ʈ�Դϴ�. pygame�� ����ϰ� ������ ������ �������� ���� ��ó�� �� ����Ʈ�� �ʱ� ���� �۵��� ������ ���� �� �ֵ��� �Ͽ����ϴ�. �� ������Ʈ�� ���¼ҽ�����Ʈ����ǽ� ������ ��ȯ���� �ۼ��Ǿ����ϴ�.

## ?����
1. �Ұ�
2. ���� Operating System �� ���� ���
3. ���� ���� ����
4. ���� �÷��� ����
5. �ڵ� ����
6. Reference
7. TODO List



### 1. �Ұ�
***
�� ������ �÷��̾ Ű������ �����¿� Ű�� �����̽��ٸ� �̿��Ͽ� �����⸦ �����ϰ� �� ������� ������ �ʴ� ���ݼ��� �Ѿ��� ���ϸ� �� ������ ���� �� ������ ���� ������ ȹ���ϴ� �����̵� �����Դϴ�. 

������Ʈ�� ���� ��ǥ�� ������ ���۹����� ������ ���� ��� �� ������, ���� �ߵ����� ���� ������ �÷����ϰ� ����� ���Դϴ�. ���� �Ѿ� ���ϱ�(�ϴ� ����)�̳� ����Ʈ�� �ʱ� ���� ������ �����ߴ� �巡�� �ö���(�ϴ� ����)�� ���� ���������� �ڲ� ������� �Ǵ� ���ӵ��� ������ �� �ֽ��ϴ�. �̷��� ���ӵ鿡�� ������ �޾� ģ���� ���� ���⸦ �ϰų� ������ �ְ� ���� �����ϸ鼭 ���������� ��� �� �ִ� ������ ������� �߽��ϴ�.

������ �ֿ� Ư¡�� �÷��� ����� ���� ���� �÷��� ���� ��Ʈ���� �� �ڼ��ϰ� ����帮�ڽ��ϴ�.

<p align="center">
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/f4b636eb-1b5f-42a3-bca3-adadd6ee678d" width="200" height="200"/>     
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/8a59130c-ba0f-4f8e-8911-599e72bc1551" width="250" height="200"/>
</p>


### 2. ?���� Operating System �� ���� ���
***
�ش� ������ Python�� Pygame ���̺귯���� ����ϰ� ������ �����ϴ� � ü���� ������ �����ϴ�.
<p align="center">

|OS|��������|
|------|---|
|Windows|O|
|Mac|���� x|
|Linux|O|
</p>

### ������
#### Windows
1. �ش� ������Ʈ�� �ٿ�ε� �Ѵ�.
2. python 3.12�� ��ġ�Ѵ�
3. �͹̳� �Ǵ� ��� ������Ʈ���� ���� ��ɾ ���� Pygame�� ��ġ�Ѵ�.

    ```sh
    pip3 install pygame
    ```

4. ����� �� �ٿ�ε�� ������Ʈ ���丮���� python3 main.py�� �����ϸ� ���� â�� �߸鼭 ����ȴ�.

#### Mac

 Mac ȯ�� ���� Pygame�� ��ġ�Ǿ��ִ� ȯ�濡�� main.py�� ������ ��� ������ �� ���Դϴ�.(���� x)

#### Linux
1. git clone�� ���� ������ �ٿ�ε� �Ѵ�
   ```sh
   git clone https://github.com/minseok1897/oss_personal_project_phase1/commits/master/
   cd oss_personal_project_phase1
   ```
2. pygame�� ��ġ�Ѵ�
   ```sh
   sudo pip3 install pygame
   ```
3. ������ �����Ѵ�
   ```sh
   python3 main.py
   ```

**��Ŀ���� (����: �������� ���׷� ���� ��Ŀ��� ���� ����� ����Ͽ� ������ ���� ��õ�մϴ�)**
1. git clone�� ���� ������ �ٿ�ε� �Ѵ�
   ```sh
   git clone https://github.com/minseok1897/oss_personal_project_phase1/commits/master/
   cd oss_personal_project_phase1
   ```
2. Docker�� �ٿ�ε� �Ѵ�
3. Dockerfile�� build�Ѵ�
   ```sh
   docker build -t airplane:0.1 .
   ```
4. docker container�� �����Ѵ�
   ```sh
    docker run -it airplane:0.1
    ```
5. �����̳� ����� ���ÿ� ������ ���۵ȴ�.



### 3. ?���� ���� ����
***
������ ���۵Ǹ� ������ �� �����⿡�� �߻�Ǵ� �Ѿ�(������ ��ü)�� ���ϸ� ����(����� �簢��)�� ȹ���Ͽ��� �մϴ�. �� �����⸦ �����Ͽ� ������ ���� �ֽ��ϴ�. �ٸ� ������ �ʴ� ���ݼ��� �߻��ϴ� ����ź(�ʷϻ� ��ü)�� �����ؾ� �մϴ�?

<p align="center">
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/8883d0eb-b6b0-4927-9512-bf31ec3fc61e" width="300" height="300"/>
</p>

### 4. ?���� �÷��� ����
***
������ ����(Flying an Airplane)�� ���۹��� ���� ��ǥ�� ���� ����帮�ڽ��ϴ�.

#### ���۹�
+ �� : ������ �����⸦ ���� �̵���ŵ�ϴ�.
+ �� : ������ �����⸦ �Ʒ��� �̵���ŵ�ϴ�.
+ �� : ������ �����⸦ �������� �̵���ŵ�ϴ�.
+ �� : ������ �����⸦ ���������� �̵���ŵ�ϴ�.
+ SPACEBAR : ������ �����⿡�� �� ������ �������� �Ѿ��� ���ϴ�.
#### ���� ��ǥ
+ �� �����⸦ ������ �Ѿ˷� ���߰ų� ������ ȹ���ϸ� ���� 1���� ��� �˴ϴ�.
+ ������ �ݺ� �÷��� �Ͽ� �ְ� ������ �����մϴ�.
#### ���� �÷���
1. **���� ����**
   
    + ������ ���۵Ǹ� �ƹ� Ű�� ���� �����մϴ�.
2. **���� ��**
   
   + **������ �̵�** : �����¿� Ű�� ���� ���� ����⸦ �̵���ų �� �ֽ��ϴ�.
   + **�� ������** : �� ������� �ִ� 4����� �����ϸ�, �� ������ �������� ������ �Ѿ��� ������ �ӵ��� ������ �����մϴ�. ������ �Ѿ˷� �� �����⸦ �����Ͽ� �����ϸ� ���� 1���� ȹ���մϴ�.
   + **����ź** : ������ �ʴ� ������ ������ �����⸦ ���� ����ź�� �߻��մϴ�. ����ź�� �ʷϻ����� ǥ�õ˴ϴ�.
   + **����** : ������ ȹ���ϸ� ������ 1�� ȹ���մϴ�. ������ ��������� ǥ�õ˴ϴ�.
   + **���� �ý���**: ���� �����⸦ �����ϰų� ������ ȹ���ϸ� 1���� �����ϸ�, 5������ FPS�� 1�� �����Ͽ� ���̵��� �ö󰩴ϴ�.
3. **���� ���� �� �����**
   
   + ������ �� 3���� ���ο� ���� ����˴ϴ�.
     + ù��°: ���� �ε����� ���(�ϴ� ����)
     + �ι�°: ���� ���� ���� ���ϴ� ���(�ϴ� �߾�)
     + ����°: �� ����⿡ �ε����� ���(�ϴ� ����)
  <p align="center">
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/a2d7a937-ffee-4b77-a672-24fc7123417b" width="200" height="200"/>
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/b9051515-57f4-4232-94dd-1a222992df5e" width="200" height="200"/>
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/f1a27f50-5db1-42ca-8617-b7047c263492" width="200" height="200"/>
</p>

   + ������ ����Ǹ� ���� ���� ȭ���� ��Ÿ����, ���ݱ����� �ְ����� ǥ�����ݴϴ�. �ְ� ����� �����ϸ� ���ϸ޼��� ���� ǥ�����ݴϴ�.
   + ������ ������Ϸ��� ���ӿ��� ȭ�鿡�� �ƹ� Ű�� ���� ������� �� �ֽ��ϴ�.

### 5. �ڵ� ����
***
+ class PlayerBullet(): ���� ������� ������ �����ϱ� ���� class�Դϴ�. ������ ���������� ǥ�õǸ� 10,10 ����� ������ �˴ϴ�. ���� ȭ���� �Ѿ�� �Ǹ� �����ǵ��� �Ͽ����ϴ�.
```python
class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -15

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
```
+ class Bullet() : �� ������� ������ �����ϱ� ���� class�Դϴ�. PlayerBullet�� ���� ����� �����ϸ� ������ �ݴ��̸� ���������� ǥ�õ˴ϴ�.
+ class SniperBullet() : ����ź ������ �����ϱ� ���� class�Դϴ�. math�� import�Ͽ��� ������ ����ѵ� �߻��ϰ� �˴ϴ�.
```python
class SniperBullet(pygame.sprite.Sprite):
    //����
        angle = math.atan2(target_y - y, target_x - x)
        self.speed_x = math.cos(angle) * 5
        self.speed_y = math.sin(angle) * 5
    // ����
```
+ class EnemyAirplane() : �� ����� ����� ��Ÿ���� ���� class�Դϴ�. �Ѿ��� ������ ���ǵ�� �����ϰ� ���� �� �ְ� �Ͽ��� �Ѿˤ��� ��� �Լ��� �����Ǿ� �ֽ��ϴ�.
```python
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
```
+ class Coin() : ���� ȹ�� �ý����� �����ϱ� ���� class �Դϴ�. ��������� ǥ�õǾ� �ֽ��ϴ�.
+ def main() : ���α׷��� ������ �� �ʿ��� �⺻ ���� �� ���� ���� ������ ���� �Լ��Դϴ�.
+ def runGame() : ���� ������ ����Ǵ� ���� �ݺ��Ǵ� �Լ��Դϴ�. ������ �̵��ϴ� ������ �Ʒ��� �����ϴ�.
```python
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    airplane = pygame.transform.scale(airplane1, (50, 50))
                    direction = 'up'
                elif event.key ==pygame.K_DOWN:
                    airplane = pygame.transform.scale(airplane3, (50, 50))
                    direction = 'down'
                elif event.key ==pygame.K_RIGHT:
                    airplane = pygame.transform.scale(airplane2, (50, 50))
                    direction = 'right'
                elif event.key ==pygame.K_LEFT:
                    airplane = pygame.transform.scale(airplane4, (50, 50))
                    direction = 'left'
                elif event.key == pygame.K_SPACE:
                    bullet = PlayerBullet(x + 25, y)
                    player_bullets.add(bullet)
        if direction == 'up':
            y-=20
        elif direction == 'down':
            y+=20
        elif direction == 'left':
            x-=20
        elif direction == 'right':
            x+=20
        
```
+ def drawPressKeyMSG() : ���� ���� ȭ�� �� ���� ���� ȭ�鿡�� �����ϴ� ���� �˸��� ���� �Լ��Դϴ�. ó�� ���۰� ����� �� �ȳ� ������ �޸� �Ͽ����ϴ�.
+ def showStartScreen() : ���� ���� ȭ���� �����ϱ� ���� �Լ��Դϴ�. ���� �� �� �κ��� ���ư��� �Ͽ����ϴ�.
+ def showGameOver() : ���� ���� ȭ���� �����ϱ� ���� �Լ��Դϴ�. ���� ������ ���� ������ ǥ���ϱ� ���� STATUS ������ �ξ� �����Ͽ����ϴ�. ���� ���� ����� ���� ���� ���� ������ �߰��Ͽ����ϴ�.
```python
    if newscore ==1:
        bestSurf = gameOverFont3.render('You Break Record!!!!!!!! BEST SCORE:'+ str(HIGHSCORE), True, BLACK)

    if STATUS == 1:
        reasonSurf = gameOverFont3.render('You hit the wall!', True, BLACK)
    elif STATUS == 2:
        reasonSurf = gameOverFont3.render('You were attacked by the enemy', True, BLACK)
    elif STATUS == 3:
        reasonSurf = gameOverFont3.render('You hit enemies!', True, BLACK)

```
+ def drawScore() : ���� ������ ǥ���ϱ� ���� �Լ��Դϴ�.
+ def terminate() : ���� ���Ḧ �����ϱ� ���� �Լ��Դϴ�.


### 6. Reference
***
[1] https://github.com/pygame/pygame "pygame"

[2] https://inventwithpython.com/pygame/chapter6.html "pygame-wormy"

[3] https://ai-creator.tistory.com/522 "[���̽� ������ ���� �����]"

### 7. TODO List
***
+ **���� ���� ��ư** �߰� �� ����
+ **���� ����� ��ų** �߰�
+ **���� ����� ���ݿ� ���� �� ����� ���** �߰�
+ **���� �ý���** ����
+ **�� ���� �����** �߰�
+ **���� ���� ����** �پ�ȭ
