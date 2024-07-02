import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от мыши")

WHITE = (255, 255, 255)
RED = (255,0,0)
FPS = 60
clock = pygame.time.Clock()
sp = None
sc.fill(WHITE)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        if sp is None:
            sp = pos
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        sc.fill(WHITE)
        pygame.draw.rect(sc, RED, pygame.Rect(sp[0], sp[1], width, height))
        pygame.display.update()
    else:
        sp = None
    clock.tick(FPS)
