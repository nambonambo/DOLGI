import pygame
from math import pi, sin, cos
import datetime

center = (0, 0)


def set_center(c):
    global center
    center = c


def numbers(screen, number, size, position, color):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(str(number), True, color)
    rect = text.get_rect(center=position)
    screen.blit(text, rect)


def polar(r, theta):
    x = center[0] + sin(pi * theta / 180) * r
    y = center[1] - cos(pi * theta / 180) * r
    return x, y


def get_time():
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second


def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)