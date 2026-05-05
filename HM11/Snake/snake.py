import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Full Version")

clock = pygame.time.Clock()

# цвета
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
        head = (self.body[0][0] + self.dx, self.body[0][1] + self.dy)
        self.body.insert(0, head)

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, CELL, CELL))

    def collision(self):
        head = self.body[0]


        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True


        if head in self.body[1:]:
            return True

        return False


class Food:
    def __init__(self, snake_body):
        self.spawn(snake_body)

    def spawn(self, snake_body):
        self.x = random.randrange(0, WIDTH, CELL)
        self.y = random.randrange(0, HEIGHT, CELL)

        self.weight = random.randint(1, 3)   
        self.timer = 300                     

        if (self.x, self.y) in snake_body:
            self.spawn(snake_body)

    def update(self):
        self.timer -= 1

    def expired(self):
        return self.timer <= 0

    def draw(self):
        if self.weight == 1:
            color = RED
        elif self.weight == 2:
            color = (255, 140, 0)
        else:
            color = (255, 0, 255)

        pygame.draw.rect(screen, color, (self.x, self.y, CELL, CELL))


snake = Snake()
food = Food(snake.body)

score = 0
level = 1
speed = 8

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
            if event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = CELL
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -CELL
                snake.dy = 0
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = CELL
                snake.dy = 0



    snake.move()


    if snake.collision():
        running = False


    food.update()

    if food.expired():
        food = Food(snake.body)


    if snake.body[0] == (food.x, food.y):
        snake.grow()
        score += food.weight
        food = Food(snake.body)


        if score // 5 + 1 > level:
            level += 1
            speed += 1  


    snake.draw()
    food.draw()

    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()