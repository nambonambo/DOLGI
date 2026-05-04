import pygame
from ball import *

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


ball = create_ball(400, 400, 25)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.fill((255, 255, 255))        
    
    moving_ball(ball)
    draw_ball(screen, ball)
    
    
    pygame.display.update()
    clock.tick(60)
    
