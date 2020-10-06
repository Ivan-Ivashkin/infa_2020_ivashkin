import pygame
from pygame.draw import *
from random import randint
pygame.init()

# Настройки экрана
FPS = 0.5
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
    Функция рисует новые шарики со случайными координатами центра, цветом и радиусом. Количество шариков - от 1 до 3.
      Количество шариков, появляющихся на экране в данный момент, определяется случайным образом.
    '''
    global ball_list
    ball_list = []
    num = randint(1, 3)
    for i in range (num):
        x = randint(100,700)
        y = randint(100,500)
        r = randint(30,50)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        list.append(ball_list, (x, y, r))


# Начальное количество очков
score = 0


def click(points):
    '''
    Функция анализирует нажатия левой кнопки мыши, подсчитывает и выводит количество набранных очков.
    points - количество очков, набранных игроком ранее
    '''
    for i in ball_list:
        distance = (event.pos[0] - i[0])**2 + (event.pos[1] - i[1])**2
        if distance <= i[2]**2:
            global score
            score = points + 1
        else:
            score = points - 1


def table(points):
    '''
    Функция обеспечивает вывод в левый верхний угол экрана таблички с текущим счетом игрока.
    points - число очков, выводимое на табличку
    '''
    rect(screen, GREEN, (0, 0, 150, 40))
    my_font = pygame.font.Font(None, 50)
    string = "Счёт: " + str(points)
    if points < 0:
        text_color = RED
    else:
        text_color = BLACK
    text = my_font.render(string, 1, text_color)
    screen.blit(text, (3, 3))


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
    table(score)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()