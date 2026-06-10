import pygame
import sys

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDR GAME")

# 폰트
font = pygame.font.SysFont("arial", 50)
small_font = pygame.font.SysFont("arial", 30)

clock = pygame.time.Clock()

def draw_start_screen():
    screen.fill((0, 0, 0))  # 검은 배경

    title = font.render("DDR GAME", True, (255, 255, 255))
    start_text = small_font.render("PRESS SPACE TO START", True, (200, 200, 200))

    screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 300))

running = True
game_started = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 스페이스로 시작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True

    if not game_started:
        draw_start_screen()
    else:
        screen.fill((30, 30, 30))
        play_text = font.render("GAME START!", True, (0, 255, 0))
        screen.blit(play_text, (250, 250))

    pygame.display.update()

pygame.quit()
sys.exit()