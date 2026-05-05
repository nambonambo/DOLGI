import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_color = BLACK
tool = "brush"

drawing = False
start_pos = None

font = pygame.font.SysFont("Arial", 20)

screen.fill(WHITE)


def draw_brush(surface, color, pos):
    pygame.draw.circle(surface, color, pos, 5)


def draw_eraser(surface, pos):
    pygame.draw.circle(surface, WHITE, pos, 10)


def draw_rectangle(surface, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, 2)


def draw_circle(surface, color, start, end):
    radius = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    pygame.draw.circle(surface, color, start, radius, 2)


def draw_square(surface, color, start, end):
    size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size, size)
    pygame.draw.rect(surface, color, rect, 2)


def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    points = [(x1, y1), (x1, y2), (x2, y2)]
    pygame.draw.polygon(surface, color, points, 2)


def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    base = x2 - x1
    height = int(abs(base) * math.sqrt(3) / 2)
    points = [
        (x1, y2),
        (x2, y2),
        ((x1 + x2) // 2, y2 - height)
    ]
    pygame.draw.polygon(surface, color, points, 2)


def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]
    pygame.draw.polygon(surface, color, points, 2)


run = True

while run:
    screen.blit(font.render("b=brush r=rect c=circle s=square t=triangle a=equilateral h=rhombus e=eraser", True, BLACK), (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_s:
                tool = "square"
            if event.key == pygame.K_t:
                tool = "right_triangle"
            if event.key == pygame.K_a:
                tool = "equilateral"
            if event.key == pygame.K_h:
                tool = "rhombus"
            if event.key == pygame.K_e:
                tool = "eraser"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                draw_rectangle(screen, current_color, start_pos, end_pos)
            elif tool == "circle":
                draw_circle(screen, current_color, start_pos, end_pos)
            elif tool == "square":
                draw_square(screen, current_color, start_pos, end_pos)
            elif tool == "right_triangle":
                draw_right_triangle(screen, current_color, start_pos, end_pos)
            elif tool == "equilateral":
                draw_equilateral_triangle(screen, current_color, start_pos, end_pos)
            elif tool == "rhombus":
                draw_rhombus(screen, current_color, start_pos, end_pos)

    if drawing:
        pos = pygame.mouse.get_pos()

        if tool == "brush":
            draw_brush(screen, current_color, pos)
        elif tool == "eraser":
            draw_eraser(screen, pos)

    pygame.display.update()
    clock.tick(1160)

pygame.quit()