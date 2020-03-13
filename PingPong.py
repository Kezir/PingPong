import pygame
from paddle import Paddle,EnemyPaddle
from Ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = EnemyPaddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE)
ball.rect.x = 300
ball.rect.y = 300

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
running = True
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 60)

punkty1 = 0
punkty2 = 0

while running:
    pkt1 = font.render(str(punkty1), True, WHITE)
    pkt1Rect = pkt1.get_rect()
    pkt1Rect.center = (70, 40)

    pkt2 = font.render(str(punkty2), True, WHITE)
    pkt2Rect = pkt2.get_rect()
    pkt2Rect.center = (630, 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)

    if ball.rect.x > 680:
        ball.speedx *= -1
        punkty1 += 1

    if ball.rect.x < 0:
        ball.speedx *= -1
        punkty2 += 1

    if ball.rect.y > 480 or ball.rect.y < 0:
        ball.speedy *= -1



    if paddleA.rect.colliderect(ball.rect) or paddleB.rect.colliderect(ball.rect):
        ball.speedx *= -1


    ball.move()
    paddleB.move(ball.rect.y)
    all_sprites_list.update()
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)
    screen.blit(pkt1, pkt1Rect)
    screen.blit(pkt2, pkt2Rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()