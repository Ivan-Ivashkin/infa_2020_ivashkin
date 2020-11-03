import math
from colors import *

FPS = 30
width = 1200
height = 720

target_colors = [RED, YELLOW, GREEN, BLUE, PURPLE]

target_num = 2 # количество мишеней, одновременно присутствующих на экране
min_gun_len = 40 # длина пушки до выстрела
max_gun_len = 100 # максимальная длина отрезка, изображающего пушку
sc_line = 55 # величина поля в левой части экрана, в котором расположена пушка
target_max_rad = 50 # максимальный радиус мишени
rad_bullet = 15 # радиус пули
target_max_angle = 2*math.pi # максимальное значение угла (применяется при расчетах движения мишени)
target_speed = 10 # скорость перемещения мишеней
gun_bottom = [0, height/2] # координата основания пушки
gun_len = min_gun_len
flag = 0
min_power = 5 # начальная мощность пушки
power = min_power
points = 0
shots = 0
g = 1 # ускорение свободного падения