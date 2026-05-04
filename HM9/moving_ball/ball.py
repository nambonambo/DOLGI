import pygame

def create_ball(x, y, radius):
    return{
        "x" : x,
        "y" : y,
        "radius" : radius
    }
    
def moving_ball(ball):
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_DOWN]:
        ball["y"] += 20
    if pressed[pygame.K_UP]:
        ball["y"] -= 20
    if pressed[pygame.K_LEFT]:
        ball["x"] -= 20
    if pressed[pygame.K_RIGHT]:
        ball["x"] += 20
        
    
    if ball["x"] - ball["radius"] < 0:
        ball["x"] = ball["radius"]
    if ball["x"] + ball["radius"] > 800:
        ball["x"] = 800 - ball["radius"]

    if ball["y"] - ball["radius"] < 0:
        ball["y"] = ball["radius"]
    if ball["y"] + ball["radius"] > 800:
        ball["y"] = 800 - ball["radius"]
    return ball
        
def draw_ball(screen, ball):
    pygame.draw.circle(screen, (255, 0, 0), ((int(ball["x"])), int(ball["y"])), ball["radius"])