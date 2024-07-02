import pygame
class Ball(pygame.sprite.Sprite):
    def __init__(self,x,speed,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)
    def update(self,h):
        if self.rect.y < h-20:
            self.rect.y += self.speed
        else:
            self.kill()

