import pygame
pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Шрифты")
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)
f = pygame.font.SysFont('arial', 24)
sc_text = f.render('Привет мир!', 1, RED, YELLOW)
pos = sc_text.get_rect(center=(W//2, H//2))
sc.fill(WHITE)
sc.blit(sc_text, pos)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
