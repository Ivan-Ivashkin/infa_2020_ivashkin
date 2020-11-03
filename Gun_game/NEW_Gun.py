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
        self.x = randint(max_rad + sc_line, width - max_rad)
        self.y = randint(max_rad, height - max_rad)
        self.rad = randint(30, target_max_rad)
        self.angle = randint(0, int(settings.target_max_angle))
        self.speed = speed

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.rad)
        circle(screen, BLACK, (self.x, self.y), self.rad, 1)

    def move(self):
        width, height = self.surface.get_size()
        if self.x >= width - self.rad:
            self.angle = math.pi / 2 + random() * math.pi
        if self.y >= height - self.rad - sc_line:
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
        self.angle = math.atan2(self.bottom_y - y, x - self.bottom_x)

    def power_up(self):
        self.color = RED
        if self.len < settings.max_gun_len:
            self.len += 1
            self.power += 1

    def shoot(self):
        x = self.bottom_x + self.len * math.cos(self.angle)
        y = self.bottom_y - self.len * math.sin(self.angle)
        power = self.power
        self.color = BLACK
        self.power = settings.min_power
        self.len = settings.min_gun_len
        return x, y, power, self.power


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
        circle(self.surface, self.color, (int(self.x), int(self.y)), self.rad)
        circle(self.surface, BLACK, (int(self.x), int(self.y)), self.rad, 1)

    def move(self):
        width, height = self.surface.get_size()

        if not self.rad < self.x < width - self.rad or \
            not self.rad < self.y < height - self.rad:
            self.vx *= -0.75
            self.vy *= 0.9
            wall_hits += 1

            if self.x >= width - self.rad:
                self.x = width - self.rad - 1
            elif self.y >= height - self.rad:
                self.y = height - self.rad - 1
            elif self.rad >= self.x:
                self.x = self.rad + 1
            elif self.rad >= self.y:
                self.y = self.rad + 1

            self.x += self.vx
            self.y -= self.vy
            self.vy -= g

    def hit_check(self, target):
        return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) <= (target.rad + self.rad) ** 2


pygame.init()
screen = pygame.display.set_mode((settings.width, settings.height))

gun = Gun(screen)
shots = 0
bullet_list = []

target_list = []
for i in range(settings.target_num):
    target_list.append(Target(screen))

finished = False
clock = pygame.time.Clock()

while not finished:
    clock.tick(settings.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            break
        elif event.type == pygame.MOUSEMOTION:
            gun.aim(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            shots = shots + 1
            x, y, power, angle = gun.shoot()
            bullet_list.append(Bullet(screen, x, y, power, angle))

    if pygame.mouse.get_pressed()[0]:
        gun.power_up()

    gun.draw()

    for bullet in bullet_list:
        bullet.draw()
        bullet.move()

    for target in target_list:
        target.draw()
        target.move()

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