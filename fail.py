"""
This module a game created using pygame.
Created by: Sergey Tovmasyan
Date: 02.06.2024
"""
import sys
from random import randint
import pygame
class Ball(pygame.sprite.Sprite):
    """
    Class: Ball inhentance from sprite
    its about ball and its move
    """
    def __init__(self, x_coor, ball_speed, image):
        """
        Function: init
        Brief: The functions is inicilzation image and rect
        Params: speed of ball,image of ball and coordination
        Return: 0
        """
        super().__init__()
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x_coor, 0))
        self.speed = ball_speed
    def update(self):
        """
        Function: update
        Brief: the speed of ball += speed
        Params: speed
        Return:0
        """
        self.rect.y += self.speed
def create_ball(balls_group,balls_surf,width):
    """
    Function: create_ball
    Brief: the function append balls in list
    Params:balls_group sprite groups of balls,balls_surf is list of balls images
    Return:0
    """
    indx = randint(0, 4)
    x_coord = randint(20, width - 20)
    speed = randint(1, 5)
    ball = Ball(x_coord, speed, balls_surf[indx])
    balls_group.add(ball)
def collide_balls(balls,box_rect,score):
    """
    Function: collide_balls
    Brief: the function check that bal is in box
    Params:balls
    Return:0
    """
    for ball in balls:
        if box_rect.collidepoint(ball.rect.center):
            score += 1
            ball.kill()
    return score
def check_misses(balls_group,game_over,misses,height):
    """
    Function: collide_balls
    Brief: the function check that bal is in box
    Params:0
    Return:0
    """
    for ball in balls_group.sprites():
        if ball.rect.y >= height - 20:
            misses += 1
            ball.kill()
            if misses >= 3:
                game_over = True
    return game_over,misses
def main():
    """
    Function: main
    main part of program
    """
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 3000)

    width,height = 1200, 800
    scanner = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    fps = 60

    background = pygame.image.load('photo_5393226249775733978_y.jpg').convert()
    box = pygame.image.load('photo_5397686380039105303_m.jpg').convert()
    font = pygame.font.SysFont('arial', 70)
    box_rect = box.get_rect(centerx=width // 2, bottom=height)
    ball_images = [
           'Screenshot_22.png',
           'Screenshot_23.png',
           'Screenshot_24.png',
           'Screenshot_25.png',
           'Screenshot_26.png'
    ]
    balls_surf = [pygame.image.load(ball).convert() for ball in ball_images]
    all_balls = pygame.sprite.Group()
    game_score = 0
    misses = 0
    speed = 10
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                create_ball(all_balls,balls_surf,width)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            box_rect.x = max(box_rect.x - speed, 0)
        elif keys[pygame.K_RIGHT]:
            box_rect.x = min(box_rect.x + speed,width - box_rect.width)
        if not game_over:
            game_score = collide_balls(all_balls,box_rect,game_score)
            game_over,misses = check_misses(all_balls,game_over,misses,height)
            scanner.blit(background, (0, 0))
            score = font.render(f'score :{game_score}',1,(0, 0, 0))
            scanner.blit(score, (20, 10))
            misse = font.render(f'misses : {misses}',1,(0,0,0))
            scanner.blit(misse,(20,60))
            all_balls.update()
            all_balls.draw(scanner)
            scanner.blit(box, box_rect)
        else:
            game_over_text = font.render('GAME OVER', 2, (255, 0, 0))
            scanner.blit(game_over_text, (width // 2 - 200, height // 2))
        pygame.display.update()
        clock.tick(fps)
if __name__ == "__main__":
    main()
