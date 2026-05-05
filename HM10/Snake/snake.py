import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Arial", 24)



class Snake:
    def __init__(self):

        self.body = [(100, 100), (80, 100), (60, 100)]
        self.dx = CELL
        self.dy = 0

    def move(self):

        head = (self.body[0][0] + self.dx, self.body[0][1] + self.dy)
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        # добавляем сегмент (не удаляем хвост)
        head = (self.body[0][0] + self.dx, self.body[0][1] + self.dy)
        self.body.insert(0, head)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    def check_collision(self):
        head = self.body[0]

        # столкновение со стеной
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True

        # столкновение с собой
        if head in self.body[1:]:
            return True

        return False



class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            x = random.randrange(0, WIDTH, CELL)
            y = random.randrange(0, HEIGHT, CELL)

            # не появляется в змее
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL, CELL))


snake = Snake()
food = Food(snake.body)

score = 0
level = 1
speed = 7 


running = True
while running:
    screen.fill(WHITE)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -CELL
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = CELL
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -CELL
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = CELL
                snake.dy = 0

    snake.move()

    if snake.check_collision():
        score_text = font.render("GAME OVER", True, BLACK)
        screen.blit(score_text, (220, 270))
        running = False

    if snake.body[0] == food.position:
        snake.grow()
        score += 1

        food = Food(snake.body)

        if score % 4 == 0:
            level += 1
            speed += 2


    snake.draw()
    food.draw()


    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()