from pygame.draw import *
from pygame.event import *
from random import *
import time
import math

pygame.init()

# Настройки прорисовки и экрана
FPS = 30
width = 800
height = 800
screen = pygame.display.set_mode((width, height))

# Цвета
WHITE = (255, 255, 255)
ORANGE = (0, 0, 0)

# Настройки
target_num = 2 # количество мишеней, одновременно присутствующих на экране
max_len = 100 # максимальная длина отрезка, изображающего пушку


def target_delete():
    '''
    Функция заменяет пораженные мишени новыми
    :return:
    '''
    pass


def new_target():
    '''
    Функция создает кружок-мишень
    :return:
    '''
    pass


# Предварительная подготовка мишеней
target_list = []
for i in range(target_num):
    ist.append(ball_list, list(new_ball()))


def gun_turning():
    '''
    Функция поворачивает пушку вслед за курсором мыши
    :return:
    '''
    pass


def gun_shot():
    '''
    Функция подготавливает пушку к выстрелу: дуло удлиняется и меняет цвет
    :return:
    '''
    pass


def new_bullet():
    '''
    Функция обеспечивает возникновение шарика-снаряда
    :return:
    '''
    pass


def moving_bullet():
    '''
    Функция обеспечивает полет шарика-снаряда
    :return:
    '''
    pass


def hit():
    '''
    Функция проверяет, произошло ли попадание пули в мишень
    :return:
    '''
    pass


finished = False

while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEMOTION:
                gun_turning()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gun_shot()
            elif event.type == pygame.MOUSEBUTTONUP:
                bullet = new_bullet()

            moving_bullet(bullet)
            hit(bullet, target)

        pygame.display.update()
        screen.fill(WHITE)

start = False
while not start:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True

pygame.quit()