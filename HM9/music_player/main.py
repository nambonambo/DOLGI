import pygame
import player

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 28)
clock = pygame.time.Clock()

player.init_player("music")

run = True
while run:
    screen.fill((20, 20, 20))

    # ---- events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next_track()

            if event.key == pygame.K_b:
                player.prev_track()

            if event.key == pygame.K_q:
                run = False

    # ---- UI ----
    track_text = font.render(
        f"Track: {player.get_current_track_name()}",
        True,
        (255, 255, 255)
    )
    screen.blit(track_text, (20, 50))

    status_text = font.render(
        f"Status: {player.get_status()}",
        True,
        (0, 200, 0)
    )
    screen.blit(status_text, (20, 100))

    controls = font.render(
        "P=Play S=Stop N=Next B=Back Q=Quit",
        True,
        (200, 200, 200)
    )
    screen.blit(controls, (20, 200))

    pygame.display.update()
    clock.tick(60)

pygame.quit()