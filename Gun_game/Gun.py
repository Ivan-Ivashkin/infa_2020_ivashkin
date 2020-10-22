import pygame
import math
from pygame.draw import *
from pygame.event import *
from random import *

pygame.init()

# Настройки прорисовки и экрана
FPS = 30
width = 1200
height = 720
screen = pygame.display.set_mode((width, height))

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
target_color = [RED, YELLOW, GREEN, BLUE, PURPLE]

# Настройки
target_num = 2 # количество мишеней, одновременно присутствующих на экране
min_gun_len = 40 # длина пушки до выстрела
max_gun_len = 100 # максимальная длина отрезка, изображающего пушку
left_line = 40 # величина поля в левой части экрана, в котором расположена пушка
target_max_rad = 70 # максимальный радиус мишени
rad_bullet = 20 # радиус пули
target_max_angle = 2*math.pi # максимальное значение угла (применяется при расчетах движения мишени)
target_speed = 5 # скорость перемещения мишеней
gun_bottom = [0, height/2] # координата основания пушки
gun_len = min_gun_len
flag = 0
min_power = 5 # начальная мощность пушки
power = min_power
g = 10 # ускорение свободного падения


def target_delete():
    '''
    Функция заменяет пораженные мишени новыми
    :return:
    '''
    target_list[target_list.index(target_list)] = list(new_target())
    return target_list


def new_target():
    '''
    Функция создает кружок-мишень
    :return:
    '''
    color = choice(target_color)
    x = randint(target_max_rad + left_line, width - target_max_rad)
    y = randint(target_max_rad, height - target_max_rad)
    rad = randint(30, target_max_rad)
    circle(screen, color, (x, y), rad)
    circle(screen, BLACK, (x, y), rad, 1)
    angle = randint(0, int(target_max_angle))
    return [x, y, rad, angle, color]


def moving_target(target):
    '''
    Функция обеспечивает передвижение мишени
    :return:
    '''
    x = target[0]
    y = target[1]
    rad = target[2]
    color = target[4]
    if x >= width - rad:
        target[3] = math.pi / 2 + random() * math.pi
    if y >= height - rad:
        target[3] = random() * math.pi
    if rad + left_line >= x:
        target[3] = random() * math.pi - math.pi / 2
    if rad >= y:
        target[3] = random() * math.pi + math.pi
    angle = target[3]
    x += int(target_speed * math.cos(angle))
    y -= int(target_speed * math.sin(angle))
    target[0] = x
    target[1] = y
    circle(screen, color, (x, y), rad)
    circle(screen, BLACK, (x, y), rad, 1)
    return target


# Предварительное создание мишеней
target_list = []
for i in range(target_num):
    list.append(target_list, list(new_target()))

# Предварительное создание списка пуль
bullet_list = []


def gun_drawing(gun_bottom, gun_top, color):
    '''

    :param gun_bottom:
    :param gun_top:
    :return:
    '''
    line(screen, color, gun_bottom, gun_top, 7)


def gun_turning(cursor, gun_bottom, gun_len):
    '''
    Функция поворачивает пушку вслед за курсором мыши
    :return:
    '''
    dx = cursor[0] - gun_bottom[0]
    dy = (-1)*(cursor[1] - gun_bottom[1])
    if dx == 0:
        dx = 1
    angle = math.atan(dy/dx)
    x = gun_len * math.cos(angle)
    y = height/2 - gun_len * math.sin(angle)
    return [x, y], angle


def new_bullet(gun_top):
    '''
    Функция обеспечивает возникновение шарика-снаряда
    :return:
    '''
    x = int(gun_top[0])
    y = int(gun_top[1])
    circle(screen, MAROON, (x, y), rad_bullet)
    circle(screen, BLACK, (x, y), rad_bullet, 1)
    return [x, y]


def moving_bullet(bullet):
    '''
    Функция обеспечивает полет шарика-снаряда
    :return:
    '''
    x = bullet[0]
    y = bullet[1]
    vx = int(bullet[2])
    vy = int(bullet[3])
    rad = bullet[4]
    color = bullet[5]

    if x >= width - rad:
        vx = int(vx * (-1) * 0.75 )
    if y >= height - rad:
        vy = int(vy * (-1) * 0.75)
    if rad >= x:
        vx = int(vx * (-1) * 0.75)
    if rad >= y:
        vy = int(vy * (-1) * 0.75)

    x += vx
    y -= vy
    vy -= 1

    bullet[0] = x
    bullet[1] = y
    bullet[2] = vx
    bullet[3] = vy
    circle(screen, color, (int(x), int(y)), rad)
    circle(screen, BLACK, (int(x), int(y)), rad, 1)
    return bullet


def hit():
    '''
    Функция проверяет, произошло ли попадание пули в мишень
    :return:
    '''
    pass


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEMOTION:
            gun_top, angle = gun_turning(list(pygame.mouse.get_pos()), gun_bottom, gun_len)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = 0
            color = RED
            gun_len = min_gun_len
            bullet = [new_bullet(gun_top)[0], new_bullet(gun_top)[1], power*math.cos(angle), power*math.sin(angle), rad_bullet, MAROON]
            list.append(bullet_list, bullet)

    if flag == 1:
        gun_top, angle = gun_turning(list(pygame.mouse.get_pos()), gun_bottom, gun_len)
        gun_drawing(gun_bottom, gun_top, RED)
        if gun_len < max_gun_len:
            gun_len = gun_len + 1
            power = power + 1
    else:
        gun_drawing(gun_bottom, gun_top, BLACK)
        gun_len = min_gun_len
        power = min_power

    for bullet in bullet_list:
        moving_bullet(bullet)

    for target in target_list:
        moving_target(target)

    pygame.display.update()
    screen.fill(WHITE)

pygame.quit()