import pygame
import sys
import random

pg = pygame
pg.init()

BLOCK_SIZE = 25
SW, SH = 800, 800

# use default font if font file missing
FONT = pg.font.Font(None, 36)

screen = pg.display.set_mode((SW, SH))
pg.display.set_caption("Snake! Game!")
clock = pg.time.Clock()

def drawgrid():
    for x in range(0, SW, BLOCK_SIZE):
        pg.draw.line(screen, (40, 40, 40), (x, 0), (x, SH))
    for y in range(0, SH, BLOCK_SIZE):
        pg.draw.line(screen, (40, 40, 40), (0, y), (SW, y))

def random_cell():
    cols = SW // BLOCK_SIZE
    rows = SH // BLOCK_SIZE
    return (random.randrange(cols) * BLOCK_SIZE, random.randrange(rows) * BLOCK_SIZE)

def reset():
    head = (SW//2//BLOCK_SIZE*BLOCK_SIZE, SH//2//BLOCK_SIZE*BLOCK_SIZE)
    return [head], (1, 0), random_cell()

snake, direction, apple = reset()

def move_snake(snake, direction):
    x, y = snake[0]
    dx, dy = direction
    new_head = (x + dx*BLOCK_SIZE, y + dy*BLOCK_SIZE)
    return [new_head] + snake[:-1]

running = True
grow = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pg.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pg.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pg.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # move
    x, y = snake[0]
    dx, dy = direction
    new_head = (x + dx*BLOCK_SIZE, y + dy*BLOCK_SIZE)

    # check collisions with walls
    if not (0 <= new_head[0] < SW and 0 <= new_head[1] < SH) or new_head in snake:
        snake, direction, apple = reset()
        grow = False
        continue

    snake.insert(0, new_head)
    if new_head == apple:
        apple = random_cell()
        grow = True
    if not grow:
        snake.pop()
    grow = False

    screen.fill((0, 0, 0))
    drawgrid()

    # draw apple
    pg.draw.rect(screen, (200, 0, 0), (*apple, BLOCK_SIZE, BLOCK_SIZE))

    # draw snake
    for i, part in enumerate(snake):
        color = (0, 200, 0) if i == 0 else (0, 120, 0)
        pg.draw.rect(screen, color, (*part, BLOCK_SIZE, BLOCK_SIZE))

    # score
    score_surf = FONT.render(f"Score: {len(snake)-1}", True, (255,255,255))
    screen.blit(score_surf, (10, 10))

    pg.display.update()
    clock.tick(10)

pg.quit()
sys.exit()

