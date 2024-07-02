import pygame
import sys
pygame.init()

W,H = 600,400

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("my game")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
#pygame.draw.rect(screen,BLUE,(10,10,50,100),2)
pygame.draw.circle(screen,BLUE,(300,250),10)
pygame.display.update()

#x = W // 2
#y = H // 2
#speed = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#        x-=speed
#    elif keys[pygame.K_RIGHT]:
#        x += speed
    screen.fill(WHITE)
    r = 20
    pygame.draw.circle(screen,PURPLE,(300,255),r)
    pygame.draw.circle(screen,BLUE,(200,200),r)
    pygame.draw.circle(screen,RED,(200,300),r)
    pygame.draw.circle(screen,GREEN,(100,100),r)
    pygame.draw.circle(screen,YELLOW,(300,50),r)
    pygame.display.update()
    clock.tick(FPS)
