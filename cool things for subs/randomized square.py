import pygame
import sys
from random import randrange

pg = pygame
pg.init()

WINDOW = 1000
TILE_SIZE = 50
# POS_RANGE defines grid-aligned positions as (start, stop, step)
POS_RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

def get_random_position():
    return (randrange(*POS_RANGE), randrange(*POS_RANGE))

snake = pg.Rect([0,0], (TILE_SIZE-2, TILE_SIZE-2))
snake.center = get_random_position()
clock = pg.time.Clock()
screen = pg.display.set_mode((WINDOW, WINDOW))
segments = []
length = 1
snake_dir = (0, 0)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            elif event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            elif event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            elif event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)

    screen.fill('black')
    snake.move_ip(snake_dir)
    segments.append(snake.copy())
    segments = segments[-length:]
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    pg.display.flip()
    clock.tick(60)
    time, time_step = 0,110
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        time = time_now
        


