import pygame
from random import *

from pygame.constants import K_DOWN
# pygame은 오른쪽, 밑으로 그림이 그려진다

###############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Quiz")  # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트, 등)
background = pygame.image.load(
    "C:\\Users\\rudal\\OneDrive\\바탕 화면\\python\\pygame_basic\\background.png")
character = pygame.image.load(
    "C:\\Users\\rudal\\OneDrive\\바탕 화면\\python\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.6

to_x = 0
to_y = 0


enemy = pygame.image.load(
    "C:\\Users\\rudal\\OneDrive\\바탕 화면\\python\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_heigth = enemy_size[1]
enemy_x_pos = randint(0, screen_width-enemy_width)
enemy_y_pos = 0
enemy_speed = 0.6

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    enemy_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed * dt
    if enemy_y_pos > screen_height - enemy_heigth:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, screen_width-enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = int(enemy_x_pos)
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (int(enemy_x_pos), enemy_y_pos))

    pygame.display.update()  # 게임화면을 다시 그리기 (반드시 계속 실행이 되어야 하는 부분)


# pygame 종료
pygame.quit()
