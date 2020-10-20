import pygame
from pygame.draw import *
from random import *
import random

pygame.init()

# Настройки экрана
FPS = 0.5
screen = pygame.display.set_mode((1200, 900))

# Цвета шариков
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, GREEN, MAGENTA, CYAN, YELLOW]


def new_ball():
    '''
    Функция рисует новые шарики со случайными координатами центра, цветом и радиусом. Количество шариков - от 1 до 3.
      Количество шариков, появляющихся на экране в данный момент, определяется случайным образом.
      Функция рисует также дополнительный шарик-мишень. Его наличие или отсутствие определяется случайным образом.
    '''
    global ball_list, max_ball_num, values
    ball_list = []

    max_ball_num = 3
    num = randint(1, max_ball_num)

    values_list = ['True', 'False']
    values = random.choice(values_list)

    if values == 'True':
        num = num + 1

    x_prev = []
    y_prev = []

    i = 1

    while i <= num:
        x = randint(50, 1000)
        y = randint(50, 850)

        if i == 1:
            list.append(x_prev, x)
            list.append(y_prev, y)

        r = randint(40, 60)

        checker = 0
        for i in range(len(x_prev)):
            for j in range(len(y_prev)):
                if (x - x_prev[i]) ** 2 + (y - y_prev[j]) ** 2 < 180 ** 2:
                    checker = 1
                    break

        if checker == 0:
            if (values == 'True') and (i == num):
                color = COLORS[randint(0, 5)]
                for i in range(r, 10, -20):
                    circle(screen, color, (x, y), i)
                    circle(screen, BLACK, (x, y), i, 1)
                    circle(screen, WHITE, (x, y), i - 10)
                    circle(screen, BLACK, (x, y), i - 10, 1)
            else:
                color = COLORS[randint(0, 5)]
                circle(screen, color, (x, y), r)
            list.append(x_prev, x)
            list.append(y_prev, y)
            list.append(ball_list, (x, y, r))
            i = i + 1
        else:
            continue


# Начальное количество очков
score = 0


def click(points):
    '''
    Функция анализирует нажатия левой кнопки мыши, подсчитывает и выводит количество набранных очков.
      points - количество очков, набранных игроком ранее
    '''
    distance_list = []
    for i in range(len(ball_list)):
        distance = (event.pos[0] - ball_list[i][0])**2 + (event.pos[1] - ball_list[i][1])**2
        list.append(distance_list, distance)

    j = distance_list.index(min(distance_list))
    if distance_list[j] <= ball_list[j][2]**2:
        if values == 'True' and j == len(ball_list) - 1:
            global score
            score = points + 3
        else:
            score = points + 1
    else:
        score = points - 1


def menu():
    '''
    Функция обеспечивает вывод на экран таблички с правилами игры (перед началом игрового процесса).
    '''
    rect(screen, YELLOW, (150, 150, 900, 190))
    text_color = BLACK
    my_font = pygame.font.Font(None, 40)
    text = my_font.render('Правила игры', 1, text_color)
    screen.blit(text, (500, 152))
    text = my_font.render('Чтобы начать, нажмите левую кнопку мыши', 1, text_color)
    screen.blit(text, (318, 300))

    my_font = pygame.font.Font(None, 30)
    text = my_font.render('1. Цель игры - ловить разноцветные шарики, появляющиеся на экране.', 1, text_color)
    screen.blit(text, (155, 180))
    text = my_font.render('2. Нажимайте по шарикам левой кнопкой мыши, пока они не исчезли.', 1, text_color)
    screen.blit(text, (155, 200))
    text = my_font.render('3. Каждое попадание приносит вам по 1 очку. Каждый промах отнимает по 1 очку.', 1,
                          text_color)
    screen.blit(text, (155, 220))
    text = my_font.render('4. Иногда на экране появляется особый шарик (он похож на мишень).', 1,
                          text_color)
    screen.blit(text, (155, 240))
    text = my_font.render('Попадание по нему дает 3 очка.', 1,
                          text_color)
    screen.blit(text, (179, 260))


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

menu()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

flag = 'False'
while not finished and flag == 'False':
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = 'True'
            screen.fill(BLACK)

while not finished and flag == 'True':
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
