import pygame
from pygame.draw import *
from pygame.font import *
from math import *

pygame.init()

FPS = 30

#colors
BLACK = (0, 0, 0)
GREEN = (127, 255, 42)
BLUE = (128, 179, 255)
BROWN = (120, 68, 33)
WHITE = (255, 255, 255)
BEIGE = (233, 198, 175)
LIGHT_BEIGE = (244, 235, 213)
DARK_ORANGE = (255, 102, 3)
RED = (255, 42, 42)
VIOLET = (212, 42, 255)

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

def hair(x_first, y_first, angle, a):
    angle = radians(angle)
    x_second = x_first + a*cos(angle)
    y_second = y_first - a*sin(angle)
    x_third = x_first + a*cos(angle+pi/3)
    y_third = y_first - a*sin(angle+pi/3)
    polygon(screen, VIOLET, [(x_first, y_first), (x_second, y_second), (x_third, y_third)])
    polygon(screen, BLACK, [(x_first, y_first), (x_second, y_second), (x_third, y_third)], 1)

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
ellipse(screen, BEIGE, (50, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (50, 40, 90, 100), 2)
ellipse(screen, BEIGE, (width - 50 - 90, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (width - 50 - 90, 40, 90, 100), 2)

#shoulders
y_st = 500
x_st = 250
polygon(screen, DARK_ORANGE, [(x_st, y_st), (x_st + 50, y_st + 80), (x_st - 10, y_st + 150), (x_st - 90, y_st + 120), (x_st - 90, y_st + 22)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+50, y_st+80), (x_st-10, y_st+150), (x_st-90, y_st+120), (x_st-90, y_st+22)], 1)
x_st = width - 250
polygon(screen, DARK_ORANGE, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)], 1)

#hair
hair(260, 275, 60, 70)
hair(280, 240, 45, 70)
hair(305, 210, 29, 70)
hair(345, 186, 14, 70)
hair(395, 173, 5, 70)
hair(450, 168, -2, 70)
hair(500, 168, -15, 70)
hair(550, 178, -30, 70)
hair(595, 197, -45, 70)
hair(628, 215, -58, 70)

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