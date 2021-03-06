import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

# Цвета шариков
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''
    Функция рисует новый шарик со случайными координатами центра, цветом и радиусом.
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


score = 0


def click(points):
    '''
    Функция анализирует нажатия левой кнопки мыши, подсчитывает и выводит количество набранных очков.
    points - количество очков, набранных игроком ранее
    '''
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2

    if distance <= r**2:
        print('Попал!')
        global score
        score = points + 1
    else:
        print('Промах!')
        score = points - 1
    print('Счет:', score)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(score)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()