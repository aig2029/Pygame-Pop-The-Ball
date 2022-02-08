from random import random
from turtle import back
import pygame
import random

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Donald.Lee/Desktop/PythonWorkspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/Donald.Lee/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기 
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 크기에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 10;

# 적 enemy 캐릭터

enemy_image = pygame.image.load("C:/Users/Donald.Lee/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy_image.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기 
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
# enemy_x_pos = screen_width / 2 - enemy_width / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
# enemy_y_pos = screen_height/2 - enemy_height/2 # 화면 세로의 크기에 해당하는 곳에 위치

enemies = []
for i in range(5):
    enemy_x_pos = random.randrange(0, screen_width-enemy_width) # 화면 가로의 절반 크기에 해당하는 곳에 위치
    enemy_y_pos = 0
    dy = random.randint(3,9)
    enemies.append({'x':enemy_x_pos, 'y':enemy_x_pos, 'dy':dy })
# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
enemies = []
# 총 시간
total_time = 100

# 시간 계산
start_ticks = pygame.time.get_ticks()


# 이벤트 루프
running = True # 게임이 진행중인가?
while running : 
    dt = clock.tick(60) # 게임화면이ㅡ 초당 프레임 수를 설정

# 캐릭터가 100만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작


    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT :
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed 
            elif event.key == pygame.K_UP :
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN :
                to_y += character_speed 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :    
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    for enemy in enemies:
        enemy['y'] += enemy['dy']

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width    

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height    

    
    if enemy_y_pos==screen_height:
        enemy_x_pos = random.randrange(0, screen_width-enemy_width) # 화면 가로의 절반 크기에 해당하는 곳에 위치
        enemy_y_pos = 0 # 화면 세로의 크기에 해당하는 곳에 위치
    enemy_y_pos += 10

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy_rect = enemy_image.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos

    # # 충돌 체크
    # if character_rect.colliderect(enemy_rect):
    #     print("충돌했어요")
    #     running = False


    screen.blit(background,(0,0)) 
    screen.blit(character,(character_x_pos,character_y_pos)) 
    screen.blit(enemy_image,(50,50)) # 적 그리기

    for enemy in enemies:
        screen.blit(enemy_image,(enemy['x'],enemy['y'])) # 적 그리기
        

    # 타이머 집어 넣기
    # 경과 시간 꼐산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시\

    timer = game_font.render( str((int)(total_time-elapsed_time)), True, (255,255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10)) 

    # 만약 시간이 0이하이면 게임 종료
    if(total_time-elapsed_time<0):
        print("타임 아웃")
        running = False



    pygame.display.update()       
# 잠시 대기
# pygame.time.delay(1000) # 2초 정도 대기(ms)


# pygame 종료
pygame.quit()