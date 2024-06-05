# ✈️전투기 게임(Flying an airplane) 프로젝트
본 프로젝트는 전투기 게임(Flying an airplane) 만들기 프로젝트입니다. pygame에 기반하고 있으며 간단한 조작으로 예전 피처폰 및 스마트폰 초기 게임 앱들의 감성을 느낄 수 있도록 하였습니다. 본 프로젝트는 오픈소스소프트웨어실습 과제의 일환으로 작성되었습니다.

## 📋목차
1. 소개
2. 구현 기능능
3. 지원 Operating System 및 실행 방법
4. 게임 실행 예시
5. 게임 플레이 설명
6. 코드 설명
7. Reference
8. TODO List



### 1. 소개💁
***
이 게임은 플레이어가 키보드의 상하좌우 키와 스페이스바를 이용하여 전투기를 조종하고 적 전투기와 보이지 않는 저격수의 총알을 피하며 적 전투기 공격 및 코인을 통해 점수를 획득하는 슈팅 아케이드 게임입니다. 

프로젝트의 최종 목표는 간단한 조작법으로 누구나 쉽게 즐길 수 있지만, 강한 중독성을 가져 여러번 플레이하게 만드는 것입니다. 과거 총알 피하기(하단 좌측)이나 스마트폰 초기 게임 시장을 지배했던 드래곤 플라이(하단 우측)과 같이 간단하지만 자꾸 빠져들게 되는 게임들을 경험한 바 있습니다. 이러한 게임들에서 영감을 받아 친구와 점수 내기를 하거나 나만의 최고 점수 갱신하면서 지속적으로 즐실 수 있는 게임을 만들고자 했습니다.

게임의 주요 특징과 플레이 방법은 이후 게임 플레이 설명 파트에서 더 자세하게 설명드리겠습니다.

<p align="center">
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/f4b636eb-1b5f-42a3-bca3-adadd6ee678d" width="200" height="200"/>     
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/8a59130c-ba0f-4f8e-8911-599e72bc1551" width="250" height="200"/>
</p>

### 2. 구현 기능
***
+ 상하좌우 키를 이용하여 유저 비행기 이동
+ 스페이스 바를 이용하여 유저 비행기에서 상대방 비행기 방면으로 공격
+ 적 비행기 등장과 적 비행기의 공격
+ 임의의 위치에서 날라오는 적의 유도탄 공격
+ 공격을 맞았을 때 게임 종료
+ 코인 및 적 비행기 공격 성공시 점수 추가 및 점수 시스템
+ 시작 화면, 종료 화면 구현


### 3. 💻지원 Operating System 및 실행 방법
***
해당 게임은 Python과 Pygame 라이브러리를 사용하고 있으며 지원하는 운영 체제는 다음과 같습니다.
<p align="center">

|OS|지원여부|
|------|---|
|Windows|⭕️|
|Mac|검증 ❌|
|Linux|⭕️|
</p>

### 실행방법
#### Windows
1. 해당 프로젝트를 다운로드 한다.
2. python 3.12를 설치한다
3. 터미널 또는 명령 프롬프트에서 다음 명령어를 통해 Pygame을 설치한다.

    ```sh
    pip3 install pygame
    ```

4. 재부팅 후 다운로드된 프로젝트 디렉토리에서 python3 main.py를 실행하면 게임 창이 뜨면서 실행된다.

#### Mac

 Mac 환경 역시 Pygame이 설치되어있는 환경에서 main.py를 실행할 경우 구동이 될 것입니다.(검증 x)

#### Linux
1. git clone을 통해 파일을 다운로드 한다
   ```sh
   git clone https://github.com/minseok1897/oss_personal_project_phase1/commits/master/
   cd oss_personal_project_phase1
   ```
2. pygame을 설치한다
   ```sh
   sudo pip3 install pygame
   ```
3. 게임을 실행한다
   ```sh
   python3 main.py
   ```

**도커사용시 (주의: 여러가지 버그로 인해 도커대신 위의 방법을 사용하여 실행할 것을 추천합니다)**
1. git clone을 통해 파일을 다운로드 한다
   ```sh
   git clone https://github.com/minseok1897/oss_personal_project_phase1/commits/master/
   cd oss_personal_project_phase1
   ```
2. Docker를 다운로드 한다
3. Dockerfile을 build한다
   ```sh
   docker build -t airplane:0.1 .
   ```
4. docker container를 실행한다
   ```sh
    docker run -it airplane:0.1
    ```
5. 컨테이너 실행과 동시에 게임이 시작된다.



### 4. 🎮게임 실행 예시
***
게임이 시작되면 유저는 적 전투기에서 발사되는 총알(빨간색 구체)를 피하며 코인(노란색 사각형)을 획득하여야 합니다. 적 전투기를 공격하여 제거할 수도 있습니다. 다만 보이지 않는 저격수가 발사하는 유도탄(초록색 구체)을 조심해야 합니다?

<p align="center">
<img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/8883d0eb-b6b0-4927-9512-bf31ec3fc61e" width="300" height="300"/>
</p>

### 5. 🎮게임 플레이 설명
***
전투기 게임(Flying an Airplane)의 조작법과 게임 목표에 관해 설명드리겠습니다.

#### 조작법
+ ↑ : 유저의 전투기를 위로 이동시킵니다.
+ ↓ : 유저의 전투기를 아래로 이동시킵니다.
+ ← : 유저의 전투기를 왼쪽으로 이동시킵니다.
+ → : 유저의 전투기를 오른쪽으로 이동시킵니다.
+ SPACEBAR : 유저의 전투기에서 적 전투기 방향으로 총알을 쏩니다.
#### 게임 목표
+ 적 전투기를 유저의 총알로 맞추거나 코인을 획득하면 점수 1점을 얻게 됩니다.
+ 게임을 반복 플레이 하여 최고 점수를 갱신합니다.
#### 게임 플레이
1. **게임 시작**
   
    + 게임이 시작되면 아무 키를 눌러 시작합니다.
2. **게임 중**
   
   + **전투기 이동** : 상하좌우 키를 통해 유저 비행기를 이동시킬 수 있습니다.
   + **적 전투기** : 적 전투기는 최대 4기까지 등장하며, 각 비행기는 랜덤으로 정해진 총알의 개수와 속도로 유저를 공격합니다. 유저의 총알로 적 전투기를 공격하여 성공하면 점수 1점을 획득합니다.
   + **유도탄** : 보이지 않는 곳에서 유저의 전투기를 향해 유도탄을 발사합니다. 유도탄은 초록색으로 표시됩니다.
   + **코인** : 코인을 획득하면 점수를 1점 획득합니다. 코인은 노란색으로 표시됩니다.
   + **점수 시스템**: 앞적 전투기를 공격하거나 코인을 획득하면 1점씩 증가하며, 5점마다 FPS가 1씩 증가하여 난이도가 올라갑니다.
3. **게임 오버 및 재시작**
   
   + 게임은 총 3개의 요인에 의해 종료됩니다.
     + 첫번째: 벽에 부딪히는 경우(하단 좌측)
     + 두번째: 적에 의해 공격 당하는 경우(하단 중앙)
     + 세번째: 적 비행기에 부딪히는 경우(하단 우측)
  <p align="center">
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/a2d7a937-ffee-4b77-a672-24fc7123417b" width="200" height="200"/>
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/b9051515-57f4-4232-94dd-1a222992df5e" width="200" height="200"/>
  <img src="https://github.com/minseok1897/oss_personal_project_phase1/assets/127393443/f1a27f50-5db1-42ca-8617-b7047c263492" width="200" height="200"/>
</p>

   + 게임이 종료되면 게임 오버 화면이 나타나고, 지금까지의 최고기록을 표시해줍니다. 최고 기록을 갱신하면 축하메세지 또한 표시해줍니다.
   + 게임을 재시작하려면 게임오버 화면에서 아무 키를 눌러 재시작할 수 있습니다.

### 6. 코드 설명
***
+ class PlayerBullet(): 유저 비행기의 공격을 구현하기 위한 class입니다. 색깔은 검정색으로 표시되며 10,10 사이즈를 가지게 됩니다. 또한 화면을 넘어가게 되면 삭제되도록 하였습니다.
    + def init : 최초 유저 비행기의 공격 구체를 생성함.
    + def update : 시간에 따라 공격 구체를 이동시키고 화면 밖으로 나가면 삭제함
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
+ class Bullet() : 적 비행기의 공격을 구현하기 위한 class입니다. PlayerBullet과 구현 방식은 동일하며 방향이 반대이며 빨간색으로 표시됩니다.
    + def init: 적 비행기 공격 구체를  생성함.
    + def update : 시간에 따라 공격 구체를 이동시키고 화면 밖으로 나가면 삭제함
+ class SniperBullet() : 유도탄 공격을 구현하기 위한 class입니다. math를 import하여서 각도를 계산한뒤 발사하게 됩니다.
    + def init: 유도탄을 최초로 생성함
    + def update: 시간에 따라 유저의 초기 방향으로 이동시킴킴
```python
class SniperBullet(pygame.sprite.Sprite):
    //생략
        angle = math.atan2(target_y - y, target_x - x)
        self.speed_x = math.cos(angle) * 5
        self.speed_y = math.sin(angle) * 5
    // 생략
```
+ class EnemyAirplane() : 적 비행기 모습을 나타내기 위한 class입니다. 총알의 개수와 스피드는 랜덤하게 구할 수 있게 하였고 총알 쏘는 함수가 구현되어 있습니다.
    + def init: 적 비행기를 등장시킴, 이때 적 비행기가 가진 총알 갯수는 5에서 10 중에 랜덤으로 정함
    + def update: 적 비행기를 이동시키고 정해진 총알 갯수를 모두 쏘면 퇴장함
    + def shoot: 총알을 생성하고 이를 발사함함
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
+ class Coin() : 점수 획득 시스템을 구현하기 위한 class 입니다. 노란색으로 표시되어 있습니다.
    +def init: 코인을 생성하고 위치시킴킴
+ def main() : 프로그램을 시작할 때 필요한 기본 세팅 및 게임 시작 구현을 위한 함수입니다.
+ def runGame() : 실제 게임이 진행되는 동안 반복되는 함수입니다. 전투기 이동하는 과정은 아래와 같습니다.
    + while 문을 돌때마다 각 요소를 업데이트하여 위치를 조정해주고 공격들을 맞았을때 케이스에 따라 결과 분류류
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
+ def drawPressKeyMSG() : 게임 시작 화면 및 게임 오버 화면에서 시작하는 법을 알리기 위한 함수입니다. 처음 시작과 재시작 시 안내 문구를 달리 하였습니다.
+ def showStartScreen() : 게임 시작 화면을 구현하기 위한 함수입니다. 제목 중 한 부분은 돌아가게 하였습니다.
+ def showGameOver() : 게임 오버 화면을 구현하기 위한 함수입니다. 게임 오버에 대한 이유를 표시하기 위해 STATUS 변수를 두어 관리하였습니다. 또한 기존 기록을 깼을 때도 축하 문구를 추가하였습니다.
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
+ def drawScore() : 게임 점수를 표시하기 위한 함수입니다.
+ def terminate() : 게임 종료를 구현하기 위한 함수입니다.


### 7. Reference
***
[1] https://github.com/pygame/pygame "pygame"

[2] https://inventwithpython.com/pygame/chapter6.html "pygame-wormy"

[3] https://ai-creator.tistory.com/522 "[파이썬 간단한 게임 만들기]"

### 8. TODO List
***
+ **게임 설명 버튼** 추가 및 구현
+ **유저 비행기 스킬** 추가
+ **유저 비행기 공격에 의한 적 비행기 사망** 추가
+ **점수 시스템** 개선
+ **적 보스 비행기** 추가
+ **적의 등장 방향** 다양화
