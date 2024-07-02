import pygame
pygame.init()
W = 600
H = 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Surface")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()


surf = pygame.Surface((200, 200))
surf.fill(RED)
pygame.draw.circle(surf, GREEN, (100, 100), 80)

surf_alpha = pygame.Surface((W, 100))
pygame.draw.rect(surf_alpha, BLUE, (0, 0, W, 100))
surf_alpha.set_alpha(128)

surf.blit(surf_alpha, (0, 50))
sc.blit(surf, (50, 50))

pygame.display.update()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    clock.tick(FPS)
