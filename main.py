import pygame
from random import randint
from ball import Ball
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)
W,H = 1200,800
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
FPS = 60

balls = pygame.sprite.Group()
bg = pygame.image.load('photo_5393226249775733978_y.jpg').convert()
bg1 = pygame.image.load('photo_5397686380039105303_m.jpg').convert()
f = pygame.font.SysFont('arial',30)

t_rect = bg1.get_rect(centerx = W//2,bottom = H)
ball_images = ['Screenshot_22.png','Screenshot_23.png',
'Screenshot_24.png','Screenshot_25.png','Screenshot_26.png']
balls_surf = []
for ball in ball_images:
    balls_surf.append(pygame.image.load(ball).convert())

def createBall(group):
    indx = randint(0, 4)
    x = randint(20, W-20)
    speed = randint(1, 5)
    return Ball(x, speed, balls_surf[indx], group)
game_score = 0
misses = 0
def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            game_score += 1
            ball.kill()

speed = 10
createBall(balls)
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
        elif event.type == pygame.USEREVENT:
            createBall(balls)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W - t_rect.width:
            t_rect.x = W - t_rect.width
    if not game_over:
        collideBalls()
        for ball in balls:
            if ball.rect.y >= H - 20:
                misses += 1
                ball.kill()
                if misses >= 3:
                    game_over = True
        sc.blit(bg,(0,0))
        ms_text = f.render(f'{game_score}',1,(0,0,0))
        sc.blit(ms_text,(200,100))
        balls.draw(sc)
        sc.blit(bg1,t_rect)
    else:
        game_over_text = f.render('GAME OVER', 2, (255, 0, 0))
        sc.blit(game_over_text, (W // 2 - 100, H // 2))
    balls.update(H)
    pygame.display.update()
    clock.tick(FPS)
