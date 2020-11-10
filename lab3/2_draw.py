import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 30

# colors
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

# screen
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)


def eye(x, y, eye_width, eye_height, color):
    """
    Функция рисует глаз.
    :param x: координата центра глаза по оси X
    :param y: координата центра глаза по оси Y
    :param eye_width: ширина глаза
    :param eye_height: высота глаза
    :param color: цвет
    """
    ellipse(screen, color, (x - eye_width // 2, y - eye_height // 2, eye_width, eye_height))
    ellipse(screen, BLACK, (x - eye_width // 2, y - eye_height // 2, eye_width, eye_height), 1)
    ellipse(screen, BLACK, (x - 17, y - 10, 34, 24))


def hand(x_st, y_st, x_ed, y_ed):
    """
    Функция рисует руку.
    :param x_st: X начала руки
    :param y_st: Y начала руки
    :param x_ed: X конца руки
    :param y_ed: Y конца руки
    """
    line(screen, BEIGE, [x_st, y_st], [x_ed, y_ed], 30)


def hair(x_first, y_first, angle, a, color):
    """
    Функция рисует 1 элемент волос.
    :param x_first: левый нижний угол элемента по оси X
    :param y_first: левый нижний угол элемента по оси Y
    :param angle: угол поворота элемента
    :param a: длина стороны элемента
    :param color: цвет
    """
    angle = radians(angle)
    x_second = x_first + a * cos(angle)
    y_second = y_first - a * sin(angle)
    x_third = x_first + a * cos(angle + pi / 3)
    y_third = y_first - a * sin(angle + pi / 3)
    polygon(screen, color, [(x_first, y_first), (x_second, y_second), (x_third, y_third)])
    polygon(screen, BLACK, [(x_first, y_first), (x_second, y_second), (x_third, y_third)], 1)


def body(x, y, radius, color):
    """
    Функция рисует тело человека.
    :param x: координата центра по X
    :param y: координата центра по Y
    :param radius: радиус тела
    :param color: цвет
    """
    circle(screen, color, (x, y), radius)


def face(x, y, radius, color):
    """
    Функция рисует лицо.
    :param x: координата центра по X
    :param y: координата центра по Y
    :param radius: радиус лица
    :param color: цвет
    """
    circle(screen, color, (x, y), radius)
    circle(screen, color, (x, y), radius)


def mouth(x, y, color):
    """
    Функция рисует рот.
    :param x: координата X нижнего уголка рта
    :param y: координата Y нижнего уголка рта
    :param color: цвет
    """
    polygon(screen, color, [(x, y), (x - 110, y - 55), (x + 110, y - 55)])
    polygon(screen, BLACK, [(x, y), (x - 110, y - 55), (x + 110, y - 55)], 1)


def nose(x, y, color):
    """
    Функция рисует рот.
    :param x: координата X нижнего уголка рта
    :param y: координата Y нижнего уголка рта
    :param color: цвет
    """
    polygon(screen, color, [(x, y), (x - 30, y - 30), (x + 30, y - 30)])
    polygon(screen, BLACK, [(x, y), (x - 30, y - 30), (x + 30, y - 30)], 1)


def eyes(x, y, eye_width, eye_height, color):
    """
    Функция рисует пару глаз.
    :param x: координата X центра между глаз
    :param y: координата Y центра между глаз
    :param eye_width: ширина глаза
    :param eye_height: высота глаза
    :param color: цвет
    """
    eye(x - 75, y, eye_width, eye_height, color)
    eye(x + 75, y, eye_width, eye_height, color)


def hands(x, y):
    """
    Функция рисует пару рук.
    :param x: координата X
    :param y: координата Y
    """
    hand(x + 0, y, x - 80, 0)
    hand(x + 400, y, x + 480, 0)
    ellipse(screen, BEIGE, (x - 110, 40, 90, 100))
    ellipse(screen, LIGHT_BEIGE, (x - 110, 40, 90, 100), 2)
    ellipse(screen, BEIGE, (x + 425, 40, 90, 100))
    ellipse(screen, LIGHT_BEIGE, (x + 425, 40, 90, 100), 2)


def shoulders(x_st, y_st, color):
    """
    Функция рисуен плечи.
    :param x_st: начальная координата X
    :param y_st: начальная координата Y
    :param color: цвет
    """
    x_st -= 150
    polygon(screen, color, [(x_st, y_st), (x_st + 50, y_st + 80), (x_st - 10, y_st + 150), (x_st - 90, y_st + 120),
                            (x_st - 90, y_st + 22)])
    polygon(screen, BLACK, [(x_st, y_st), (x_st + 50, y_st + 80), (x_st - 10, y_st + 150), (x_st - 90, y_st + 120),
                            (x_st - 90, y_st + 22)], 1)
    x_st += 300
    polygon(screen, color, [(x_st, y_st), (x_st + 90, y_st + 22), (x_st + 90, y_st + 120), (x_st + 10, y_st + 150),
                            (x_st - 50, y_st + 80)])
    polygon(screen, BLACK, [(x_st, y_st), (x_st + 90, y_st + 22), (x_st + 90, y_st + 120), (x_st + 10, y_st + 150),
                            (x_st - 50, y_st + 80)], 1)


def full_hair(x, y, a, color):
    """
    Функция рисует волосы человечка
    :param x: начальная координата X
    :param y: начальная координата Y
    :param a: длина сегмента
    :param color: цвет
    """
    x_list = [0, 18, 41, 73, 123, 178, 228, 274, 309, 338]
    y_list = [0, 38, 68, 99, 112, 117, 117, 107, 88, 60]
    deg_list = [60, 45, 33, 14, 5, -2, -15, -30, -45, -60]
    for i in range(10):
        hair(x + x_list[i], y - y_list[i], deg_list[i], a, color)


def man(x, y, eyes_color, hair_color, body_color, mouth_color=RED, face_color=BEIGE, nose_color=BROWN):
    """
    Функция рисует человечка.
    :param x: координаты центра тела по X
    :param y: координаты центра тела по Y
    :param eyes_color: цвет глаз
    :param hair_color: цвет волос
    :param body_color: цвет тела
    :param mouth_color: цвет рта
    :param face_color: цвет лица
    :param nose_color: цвет носа
    """
    body(x, y, 250, body_color)
    hands(x - 200, y - 200)
    shoulders(x, y - 250, body_color)
    face(x, y - 385, 200, face_color)
    mouth(x, y - 250, mouth_color)
    nose(x, y - 340, nose_color)
    eyes(x, y - 420, 100, 90, eyes_color)
    full_hair(x - 185, y - 450, 70, hair_color)


def text(words, color):
    """
    Функция пишет текст в рамочке заданного цвета.
    :param words: текст для вывода на экран
    :param color: цвет рамочки
    """
    rect(screen, color, (0, 0, width, 90))
    rect(screen, BLACK, (0, 0, width, 90), 1)
    my_font = pygame.font.Font(None, 125)
    text_temp = my_font.render(words, 1, BLACK)
    screen.blit(text_temp, (3, 3))


man(width // 4, height, BLUE, YELLOW, DARK_GREEN)
man(3 * width // 4, height, GREEN, RED, BLACK)
text('PYTHON is REALLY AMAZING', GREEN)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
