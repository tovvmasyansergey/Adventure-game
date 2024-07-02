import pygame
pygame.init()
W, H = 600, 400
sc = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Изображения")
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 176)
car_surf = pygame.image.load("dodje.webp")
car_surf = car_surf.convert()
car_rect = car_surf.get_rect(center = (W,H))
sc.blit(car_surf, car_rect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(FPS)
