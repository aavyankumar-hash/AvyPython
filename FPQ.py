import pygame 
from pygame import mixer
pygame.init()

width = 1400
height= 800


black =(0,0,0)
white = (255, 255, 255)
gray = (128, 128, 128)



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('beat maker ')
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
fps = 60
timer = pygame.time.Clock()

def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0,0,200,height-200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0,height-200,width,200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hattext = font.render('hi hat', True, white)
    screen.blit(hi_hattext, (30, 30))
    snare_text = font.render('snare', True, white)
    screen.blit(snare_text, (30,130))
    kick_text = font.render('kick', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = font.render('crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = font.render('clap', True, white)
    screen.blit(clap_text, (30, 430))
    floortom_text = font.render('floor tom', True, white)
    screen.blit(floortom_text, (30, 530))


run = True
while run :
    timer.tick(fps)
    screen.fill(black)
    draw_grid()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.flip()
pygame.quit()



























