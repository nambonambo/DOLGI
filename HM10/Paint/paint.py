import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

current_color = BLACK
tool = "brush"  # brush, rect, circle, eraser

drawing = False
start_pos = None

screen.fill(WHITE)

font = pygame.font.SysFont("Arial", 20)


# --- функции инструментов ---
def draw_brush(surface, color, pos):
    pygame.draw.circle(surface, color, pos, 5)


def draw_eraser(surface, pos):
    pygame.draw.circle(surface, WHITE, pos, 10)


def draw_rectangle(surface, color, start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(surface, color, rect, 2)


def draw_circle(surface, color, start, end):
    radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5)
    pygame.draw.circle(surface, color, start, radius, 2)


# --- основной цикл ---
run = True
while run:
    
    view = font.render("b = карандаш, r = прямоуг, c = круг, e = ластик", True, BLACK)
    screen.blit(view, (10,10))
    view = font.render("1 = красный, 2 = зеленый, 3 = синий, 4 = черный", True, BLACK)
    screen.blit(view, (10,40))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # выбор инструмента (клавиши)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

            # выбор цвета
            if event.key == pygame.K_1:
                current_color = (255, 0, 0)  # красный
            if event.key == pygame.K_2:
                current_color = (0, 255, 0)  # зеленый
            if event.key == pygame.K_3:
                current_color = (0, 0, 255)  # синий
            if event.key == pygame.K_4:
                current_color = (0, 0, 0)    # черный

        # начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # конец рисования
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "rect":
                draw_rectangle(screen, current_color, start_pos, end_pos)
            elif tool == "circle":
                draw_circle(screen, current_color, start_pos, end_pos)

    # движение мыши
    if drawing:
        mouse_pos = pygame.mouse.get_pos()

        if tool == "brush":
            draw_brush(screen, current_color, mouse_pos)
        elif tool == "eraser":
            draw_eraser(screen, mouse_pos)

    pygame.display.update()
    clock.tick(1020)

pygame.quit()