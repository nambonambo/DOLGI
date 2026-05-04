import pygame
from clock import numbers, polar, get_time, blitRotateCenter, set_center

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 380

set_center(CENTER)

hand_img = pygame.image.load("images/mickey_hand.png").convert_alpha()


def make_pivoted_hand(img, hand_size):

    scaled = pygame.transform.scale(img, hand_size)
    w, h = scaled.get_size()

    # Новый Surface: ширина та же, высота x2 (снизу прозрачный отступ)
    padded = pygame.Surface((w, h * 2), pygame.SRCALPHA)
    padded.fill((0, 0, 0, 0))
    padded.blit(scaled, (0, 0))  # картинка в верхней половине
    return padded


minute_hand = make_pivoted_hand(hand_img, (250, 250))
second_hand = make_pivoted_hand(hand_img, (300, 300))


def draw_clock_face():
    pygame.draw.circle(screen, BLACK, CENTER, RADIUS, 8)
    pygame.draw.circle(screen, BLACK, CENTER, 6)
    for n in range(1, 13):
        numbers(screen, n, 50, polar(RADIUS - 60, n * 30), BLACK)


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        hour, minute, second = get_time()

        screen.fill(WHITE)
        draw_clock_face()

        minute_angle = -((minute + second / 60) * 6)
        second_angle = -(second * 6)

        m_w, m_h = minute_hand.get_size()
        s_w, s_h = second_hand.get_size()

        minute_topleft = (CENTER[0] - m_w // 2, CENTER[1] - m_h // 2)
        second_topleft = (CENTER[0] - s_w // 2, CENTER[1] - s_h // 2)

        blitRotateCenter(screen, minute_hand, minute_topleft, minute_angle)
        blitRotateCenter(screen, second_hand, second_topleft, second_angle)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


main()