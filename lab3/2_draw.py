import pygame
from pygame.draw import *
from pygame.font import *
from math import *

pygame.init()

FPS = 30

#colors
BLACK = (0, 0, 0)
GREEN = (127, 255, 42)
DARK_GREEN = (0, 128, 0)
BLUE = (128, 179, 255)
BROWN = (120, 68, 33)
WHITE = (255, 255, 255)
BEIGE = (233, 198, 175)
LIGHT_BEIGE = (244, 235, 213)
DARK_ORANGE = (255, 102, 3)
RED = (255, 42, 42)
VIOLET = (212, 42, 255)
YELLOW = (255, 212, 42)
GREY = (190, 200, 183)

#screen
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)

def eye(x, y, eye_width, eye_height, color):
    ellipse(screen, color, (x - eye_width//2, y - eye_height//2, eye_width, eye_height))
    ellipse(screen, BLACK, (x - eye_width//2, y - eye_height//2, eye_width, eye_height), 1)
    ellipse(screen, BLACK, (x - 17, y - 10, 34, 24))

def hand(x_st, y_st, x_ed, y_ed):
    line(screen, BEIGE, [x_st, y_st], [x_ed, y_ed], 30)

def hair(x_first, y_first, angle, a, color):
    angle = radians(angle)
    x_second = x_first + a*cos(angle)
    y_second = y_first - a*sin(angle)
    x_third = x_first + a*cos(angle+pi/3)
    y_third = y_first - a*sin(angle+pi/3)
    polygon(screen, color, [(x_first, y_first), (x_second, y_second), (x_third, y_third)])
    polygon(screen, BLACK, [(x_first, y_first), (x_second, y_second), (x_third, y_third)], 1)

#body
circle(screen, DARK_GREEN, (width//4, height), 250)
circle(screen, DARK_ORANGE, (3*width//4, height), 250)

#face
circle(screen, BEIGE, (width//4, height//2), 200)
circle(screen, BEIGE, (3*width//4, height//2), 200)

#mouth
polygon(screen, RED, [(width//4, height//2 + 140), (width//4 - 110, height//2 + 85), (width//4 + 110, height//2 + 85)])
polygon(screen, BLACK, [(width//4, height//2 + 140), (width//4 - 110, height//2 + 85), (width//4 + 110, height//2 + 85)], 1)
polygon(screen, RED, [(3*width//4, height//2 + 140), (3*width//4 - 110, height//2 + 85), (3*width//4 + 110, height//2 + 85)])
polygon(screen, BLACK, [(3*width//4, height//2 + 140), (3*width//4 - 110, height//2 + 85), (3*width//4 + 110, height//2 + 85)], 1)

#nose
polygon(screen, BROWN, [(width//4, height//2 + 50), (width//4 - 30, height//2 + 20), (width//4 + 30, height//2 + 20)])
polygon(screen, BLACK, [(width//4, height//2 + 50), (width//4 - 30, height//2 + 20), (width//4 + 30, height//2 + 20)], 1)
polygon(screen, BROWN, [(3*width//4, height//2 + 50), (3*width//4 - 30, height//2 + 20), (3*width//4 + 30, height//2 + 20)])
polygon(screen, BLACK, [(3*width//4, height//2 + 50), (3*width//4 - 30, height//2 + 20), (3*width//4 + 30, height//2 + 20)], 1)

#eyes
eye(width//4 - 75, height//2 - 50, 100, 90, GREY)
eye(width//4 + 75, height//2 - 50, 100, 90, GREY)
eye(3*width//4 - 75, height//2 - 50, 100, 90, BLUE)
eye(3*width//4 + 75, height//2 - 50, 100, 90, BLUE)

#hands
hand(120, 3*height//4, 30, 0)
hand(width//2 - 120, 3*height//4, width//2 - 30, 0)
ellipse(screen, BEIGE, (10, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (10, 40, 90, 100), 2)
ellipse(screen, BEIGE, (width//2 - 10 - 90, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (width//2 - 10 - 90, 40, 90, 100), 2)

hand(width//2 + 120, 3*height//4, width//2 + 30, 0)
hand(width - 120, 3*height//4, width - 30, 0)
ellipse(screen, BEIGE, (width//2 + 10, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (width//2 + 10, 40, 90, 100), 2)
ellipse(screen, BEIGE, (width - 10 - 90, 40, 90, 100))
ellipse(screen, LIGHT_BEIGE, (width - 10 - 90, 40, 90, 100), 2)

#shoulders
y_st = 480
x_st = 150
polygon(screen, DARK_GREEN, [(x_st, y_st), (x_st + 50, y_st + 80), (x_st - 10, y_st + 150), (x_st - 90, y_st + 120), (x_st - 90, y_st + 22)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+50, y_st+80), (x_st-10, y_st+150), (x_st-90, y_st+120), (x_st-90, y_st+22)], 1)
x_st = width//2 - 150
polygon(screen, DARK_GREEN, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)], 1)

y_st = 480
x_st = width//2 + 150
polygon(screen, DARK_ORANGE, [(x_st, y_st), (x_st + 50, y_st + 80), (x_st - 10, y_st + 150), (x_st - 90, y_st + 120), (x_st - 90, y_st + 22)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+50, y_st+80), (x_st-10, y_st+150), (x_st-90, y_st+120), (x_st-90, y_st+22)], 1)
x_st = width - 150
polygon(screen, DARK_ORANGE, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)])
polygon(screen, BLACK, [(x_st, y_st), (x_st+90, y_st+22), (x_st+90, y_st+120), (x_st+10, y_st+150), (x_st-50, y_st+80)], 1)

#hair
hair(132, 285, 60, 70, YELLOW)
hair(150, 247, 45, 70, YELLOW)
hair(173, 217, 33, 70, YELLOW)
hair(205, 186, 14, 70, YELLOW)
hair(255, 173, 5, 70, YELLOW)
hair(310, 168, -2, 70, YELLOW)
hair(360, 168, -15, 70, YELLOW)
hair(406, 178, -30, 70, YELLOW)
hair(441, 197, -45, 70, YELLOW)
hair(470, 225, -60, 70, YELLOW)

hair(772, 285, 60, 70, VIOLET)
hair(790, 247, 45, 70, VIOLET)
hair(820, 217, 33, 70, VIOLET)
hair(855, 186, 14, 70, VIOLET)
hair(905, 173, 5, 70, VIOLET)
hair(960, 168, -2, 70, VIOLET)
hair(1010, 168, -15, 70, VIOLET)
hair(1044, 178, -30, 70, VIOLET)
hair(1080, 197, -45, 70, VIOLET)
hair(1111, 225, -60, 70, VIOLET)

#table
rect(screen, GREEN, (0, 0, width, 90))
rect(screen, BLACK, (0, 0, width, 90), 1)
my_font = pygame.font.Font(None, 125)
text = my_font.render('PYTHON is REALLY AMAZING', 1, BLACK)
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