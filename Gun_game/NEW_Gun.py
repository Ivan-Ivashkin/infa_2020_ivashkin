import math
from random import *

import pygame
from pygame.draw import *
from pygame.event import *

import settings
from colors import *


class Target:
    def __init__(
        self,
        surface,
        color=None,
        max_rad=settings.target_max_rad,
        speed=settings.target_speed
    ):
        self.surface = surface
        self.color = color or choice(settings.target_colors)
        width, height = self.surface.get_size()
        self.x = randint(max_rad + settings.sc_line, width - max_rad)
        self.y = randint(max_rad, height - max_rad)
        self.rad = randint(30, settings.target_max_rad)
        self.angle = randint(0, int(2*math.pi))
        self.speed = speed

    def draw(self):
        '''
        Функция рисует мишени
        :return:
        '''
        circle(screen, self.color, (self.x, self.y), self.rad)
        circle(screen, BLACK, (self.x, self.y), self.rad, 1)

    def move(self):
        '''
        Функция перемещает мишени (со случайным отражением от стен)
        :return:
        '''
        width, height = self.surface.get_size()
        if self.x >= width - self.rad:
            self.angle = math.pi / 2 + random() * math.pi
        if self.y >= height - self.rad - settings.sc_line:
            self.angle = random() * math.pi
        if self.rad >= self.x:
            self.angle = random() * math.pi - math.pi / 2
        if self.rad >= self.y:
            self.angle = random() * math.pi + math.pi
        self.x += int(self.speed * math.cos(self.angle))
        self.y -= int(self.speed * math.sin(self.angle))


class Gun:
    def __init__(self, surface):
        self.surface = surface
        self.bottom_x = 0
        self.bottom_y = surface.get_height() // 2
        self.len = settings.min_gun_len
        self.angle = 0
        self.color = BLACK
        self.power = settings.min_power

    def draw(self):
        '''
        Функция рисует линию, изображающую пушку
        :return:
        '''
        x = int(self.bottom_x + self.len * math.cos(self.angle))
        y = int(self.bottom_y - self.len * math.sin(self.angle))
        line(
            self.surface,
            self.color,
            (self.bottom_x, self.bottom_y),
            (x, y),
            7
        )

    def aim(self, x, y):
        '''
        Функция изменяет угол наклона пушки в зависимости от положения курсора на экране
        :param x: координата x курсора
        :param y: координата y курсора
        :return:
            self.angle: мгновенное значение угла наклона
        '''
        self.angle = math.atan2(self.bottom_y - y, x - self.bottom_x)
        return self.angle

    def power_up(self):
        '''
        Функция наращивает мощность пушки
        :return:
        '''
        self.color = RED
        if self.len < settings.max_gun_len:
            self.len += 1
            self.power += 0.75

    def shoot(self):
        '''
        Функция обрабатывает момент "выстрела"
        :return:
            x: координата x "дула" при выстреле
            y: координата y "дула" при выстреле
            power: мощность пушки при выстреле
        '''
        x = self.bottom_x + self.len * math.cos(self.angle)
        y = self.bottom_y - self.len * math.sin(self.angle)
        power = self.power
        self.color = BLACK
        self.power = settings.min_power
        self.len = settings.min_gun_len
        return x, y, power


class Bullet:
    def __init__(self, surface, x, y, power, angle):
        self.x = x
        self.y = y
        self.vx = power * math.cos(angle)
        self.vy = power * math.sin(angle)
        self.surface = surface
        self.rad = settings.rad_bullet
        self.color = MAROON
        self.wall_hits = 0

    def draw(self):
        '''
        Функция рисует ядра пушки
        :return:
        '''
        circle(self.surface, self.color, (int(self.x), int(self.y)), self.rad)
        circle(self.surface, BLACK, (int(self.x), int(self.y)), self.rad, 1)

    def move(self):
        '''
        Функция перемещает ядра пушки (с затуханием скорости при отражении от стен)
        :return:
            self.wall_hits: число ударов ядра о стены
        '''
        width, height = self.surface.get_size()

        if not self.rad < self.x < width - self.rad or \
            not self.rad < self.y < height - self.rad:
            self.wall_hits += 1

            if self.x >= width - self.rad:
                self.x = width - self.rad - 1
                self.vx *= -0.75
                self.vy *= 0.9
            elif self.y >= height - self.rad:
                self.y = height - self.rad - 1
                self.vy *= -0.75
                self.vx *= 0.9
            elif self.rad >= self.x:
                self.x = self.rad + 1
                self.vx *= -0.75
                self.vy *= 0.9
            elif self.rad >= self.y:
                self.y = self.rad + 1
                self.vy *= -0.75
                self.vx *= 0.9

        self.x += self.vx
        self.y -= self.vy
        self.vy -= settings.g
        return self.wall_hits

    def hit_check(self, target):
        '''
        Функция проверяет, попало ли ядро в мишень
        :param target: объект (мишень), попадание в который проверяется
        :return:
            значение True или False
        '''
        return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) <= (target.rad + self.rad) ** 2


class Table:
    def __init__(self, surface, x, y, pre_text):
        self.surface = surface
        self.my_font = pygame.font.Font(None, 50)
        self.x = x
        self.y = y
        self.pre_text = pre_text

    def write(self, num):
        '''
        Функция выводит таблички со счетом и количеством выстрелов
        :param num: выводимое число
        :return:
        '''
        text = self.my_font.render(self.pre_text + str(num), 1, BLACK)
        self.surface.blit(text, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((settings.width, settings.height))

gun = Gun(screen)
shots = 0
points = 0
bullet_list = []

target_list = []
for i in range(settings.target_num):
    target_list.append(Target(screen))

t_points = Table(screen, 5, 3, "Счёт: ")
t_shots = Table(screen, settings.width - 250, 3, "Выстрелов: ")

finished = False
clock = pygame.time.Clock()

while not finished:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        elif event.type == pygame.MOUSEMOTION:
            angle = gun.aim(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            shots += 1
            x, y, power = gun.shoot()
            bullet_list.append(Bullet(screen, x, y, power, angle))

    if pygame.mouse.get_pressed()[0]:
        gun.power_up()

    gun.draw()

    for bullet in bullet_list:
        bullet.draw()
        wall_hits = bullet.move()
        for target in target_list:
            if bullet.hit_check(target):
                target_list.remove(target)
                target_list.append(Target(screen))
                points += 1
        if wall_hits > 15:
            bullet_list.remove(bullet)

    for target in target_list:
        target.draw()
        target.move()

    t_points.write(points)
    t_shots.write(shots)

    pygame.display.update()
    screen.fill(WHITE)

    rect(
        screen,
        GREY,
        (
            0,
            settings.height - settings.sc_line,
            settings.width,
            settings.sc_line
        )
    )

pygame.quit