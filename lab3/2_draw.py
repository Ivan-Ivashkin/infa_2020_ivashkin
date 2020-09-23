import pygame
from pygame.draw import *
from pygame.font import *

pygame.init()

FPS = 30

#colors
BLACK = (0, 0, 0)
GREEN = (127, 255, 42)
BLUE = (128, 179, 255)
BROWN = (120, 68, 33)
WHITE = (255, 255, 255)
BEIGE = (233, 198, 175)
DARK_ORANGE = (255, 102, 3)
RED = (255, 42, 42)

#screen
width = 927
height = 769
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)

def eye(x, y, eye_width, eye_height):
    ellipse(screen, BLUE, (x - eye_width//2, y - eye_height//2, eye_width, eye_height))
    ellipse(screen, BLACK, (x - eye_width//2, y - eye_height//2, eye_width, eye_height), 1)
    ellipse(screen, BLACK, (x - 17, y - 10, 34, 24))

def hand(x_st, y_st, x_ed, y_ed):
    line(screen, BEIGE, [x_st, y_st], [x_ed, y_ed], 40)

#body
circle(screen, DARK_ORANGE, (width//2, height), 300)

#face
circle(screen, BEIGE, (width//2, height//2), 230)

#mouth
polygon(screen, RED, [(width//2, height//2 + 140), (width//2 - 110, height//2 + 85), (width//2 + 110, height//2 + 85)])
polygon(screen, BLACK, [(width//2, height//2 + 140), (width//2 - 110, height//2 + 85), (width//2 + 110, height//2 + 85)], 1)

#nose
polygon(screen, BROWN, [(width//2, height//2 + 50), (width//2 - 30, height//2 + 20), (width//2 + 30, height//2 + 20)])
polygon(screen, BLACK, [(width//2, height//2 + 50), (width//2 - 30, height//2 + 20), (width//2 + 30, height//2 + 20)], 1)

#eyes
eye(width//2 - 75, height//2 - 50, 100, 90)
eye(width//2 + 75, height//2 - 50, 100, 90)

#hands
hand(width//2 - width//4, 3*height//4, 60, 20)
hand(width//2 + width//4, 3*height//4, width - 60, 20)

#table
rect(screen, GREEN, (0, 0, width, 90))
rect(screen, BLACK, (0, 0, width, 90), 1)
my_font = pygame.font.Font(None, 126)
text = my_font.render('PYTHON is AMAZING', 1, BLACK)
screen.blit(text, (3, 3))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()