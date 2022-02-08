from turtle import back
import pygame

################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()
################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 폰트)



# 이벤트 루프
running = True # 게임이 진행중인가?
while running : 
    dt = clock.tick(60) # 게임화면이ㅡ 초당 프레임 수를 설정

# 캐릭터가 100만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작


    print("fps : " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)
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


    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    character_y_pos += to_y

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

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos;
    character_rect.top = character_y_pos;

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충둘했어요")
        running = False


    screen.blit(background,(0,0)) 
    screen.blit(character,(character_x_pos,character_y_pos)) 
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기

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
pygame.time.delay(1000) # 2초 정도 대기(ms)


# pygame 종료
pygame.quit()