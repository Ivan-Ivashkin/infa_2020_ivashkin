import pygame
from pygame.draw import *
from pygame.event import *
from random import *
import time
import math

pygame.init()

# Параметры шариков
max_rad = 50
min_speed = 5
max_speed = 9
max_angle = 2*math.pi
ball_num = 10
super_ball_num = 3

# Цвета шариков
BLUE_1 = (179, 229, 252)
BLUE_2 = (79, 195, 247)
BLUE_3 = (3, 169, 244)
BLUE_4 = (2, 136, 209)
BLUE_5 = (1, 87, 155)
COLORS = [BLUE_1, BLUE_2, BLUE_3, BLUE_4, BLUE_5]
COLORS_NUM = 5

# Цвета прочих объектов
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Настройки прорисовки и экрана
FPS = 30
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))


def menu():
    '''
    Функция обеспечивает отображение таблички с правилами игры перед началом игрового процесса
    :return: возвращаемых параметров нет
    '''
    rect(screen, BLUE_1, (100, 200, width-200, height-400))
    text_color = BLACK
    my_font = pygame.font.Font(None, 40)
    text = my_font.render('Игра "Поймай шарик"', 1, text_color)
    screen.blit(text, (500, 205))
    text = my_font.render('Чтобы начать, нажмите левую кнопку мыши', 1, text_color)
    screen.blit(text, (335, 475))

    my_font = pygame.font.Font(None, 30)
    text = my_font.render('Правила игры', 1, text_color)
    screen.blit(text, (570, 243))

    text = my_font.render('1. Цель игры - ловить разноцветные шарики, перемещающиеся по экрану, нажимая на них левой кнопкой', 1, text_color)
    screen.blit(text, (105, 275))
    text = my_font.render('мыши.', 1, text_color)
    screen.blit(text, (130, 295))

    text = my_font.render('2. Попадание по обычному (синему) шарику приносит вам 1 очко.', 1, text_color)
    screen.blit(text, (105, 315))

    text = my_font.render('3. Кроме обычных шариков, на экране есть особые шарики красного цвета. Они движутся быстрее синих.', 1,
                          text_color)
    screen.blit(text, (105, 335))
    text = my_font.render('Попадание по ним дает 3 очка.', 1, text_color)
    screen.blit(text, (130, 355))

    text = my_font.render('4. После поимки одной "партии" шариков на экране появляется следующая "партия" - начинается новый', 1,
                          text_color)
    screen.blit(text, (105, 375))
    text = my_font.render('раунд. С каждым новым раундом общее количество шариков и их скорость увеличиваются.', 1, text_color)
    screen.blit(text, (130, 395))

    text = my_font.render('5. Ваше время ограничено: игра продолжается 60 секунд.', 1, text_color)
    screen.blit(text, (105, 415))

    text = my_font.render('Желаем удачи!', 1, text_color)
    screen.blit(text, (570, 445))


def game_over(points, game_round, game_time, name):
    '''
    Функция обеспечивает вывод таблички с результатами игры и запись результатов в файл
    :param points: количество очков, набранных за игры
    :param game_round: раунд, на котором остановился игрок
    :param game_time: продолжительность игры
    :param name: имя игрока
    :return: возвращаемых параметров нет
    '''
    rect(screen, BLUE_1, (100, 200, width-200, height-400))
    text_color = BLACK
    my_font = pygame.font.Font(None, 40)
    text = my_font.render('Время вышло! Игра окончена', 1, text_color)
    screen.blit(text, (475, 205))

    text = my_font.render('Спасибо за игру! До встречи!', 1, text_color)
    screen.blit(text, (475, 475))

    line = 'Количество набранных очков: ' + str(points)
    text = my_font.render(line, 1, text_color)
    screen.blit(text, (105, 315))

    line = 'Количество сыгранных раундов: ' + str(game_round)
    text = my_font.render(line, 1, text_color)
    screen.blit(text, (105, 355))

    line = 'Время игры: ' + str(game_time) + ' секунд'
    text = my_font.render(line, 1, text_color)
    screen.blit(text, (105, 395))

    if name == '':
        text = my_font.render('Имя игрока: <введите ваше имя в консоль>', 1, RED)
        screen.blit(text, (105, 275))
        pygame.display.update()
        name = input()
        game_over(points, game_round, game_time, name)
    else:
        line = 'Имя игрока: ' + name
        text = my_font.render(line, 1, BLACK)
        screen.blit(text, (105, 275))
        raiting = open('raiting.txt', 'a')
        raiting.write('\n' + str(name) + ' - ' + str(game_time) + ' - ' + str(game_round) + ' - ' + str(points) + '\n')
        raiting.close()
        text = my_font.render('Для выхода из игры нажмите левую кнопку мыши', 1, BLUE_1)
        screen.blit(text, (335, 530))
        pygame.display.update()

menu()
pygame.display.update()

start = False
while not start:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True


def new_ball():
    '''
    Функция обеспечивает создание нового обычного шарика
    :return: (списком) координаты центра шарика, его радиус, угол направления полета, коэффициент скорости, цвет
    '''
    color = COLORS[randint(0, COLORS_NUM - 1)]
    x = randint(max_rad, width - max_rad)
    y = randint(max_rad, height - max_rad)
    rad = randint(40, max_rad)
    circle(screen, color, (x, y), rad)
    angle = randint(0, int(max_angle))
    speed = randint(min_speed, max_speed)
    return [x, y, rad, angle, speed, color]


def new_super_ball():
    '''
    Функция обеспечивает создание нового особого шарика
    :return: (списком) координаты центра шарика, его радиус, угол направления полета, коэффициент скорости, цвет
    '''
    x = randint(max_rad, width - max_rad)
    y = randint(max_rad, height - max_rad)
    rad = randint(30, max_rad)
    color = RED
    circle(screen, color, (x, y), rad)
    angle = randint(0, int(max_angle))
    speed = max_speed + 10
    return [x, y, rad, angle, speed, color]


def ball_load(ball_num):
    '''
    Функция обеспечивает заполнение экрана обычными шариками
    :param ball_num: количество обычных шариков в 'партии'
    :return: список списков характеристик шариков
    '''
    ball_list = []
    for i in range(ball_num):
        list.append(ball_list, list(new_ball()))
    return ball_list


def super_ball_load(super_ball_num):
    '''
    Функция обеспечивает заполнение экрана особыми шариками
    :param super_ball_num: количество особых шариков в 'партии'
    :return: список списков характеристик особых шариков
    '''
    super_ball_list = []
    for i in range(super_ball_num):
        list.append(super_ball_list, list(new_super_ball()))
    return super_ball_list


ball_list = ball_load(ball_num)
super_ball_list = super_ball_load(super_ball_num)


def click_ball(ball, ball_list, event, points, ball_num):
    '''
    Функция обеспечивает обработку клика по обычному шарику
    :param ball: наследуемая переменная-счетчик (параметры текущего шарика)
    :param ball_list: списков списков характеристик обычных шариков
    :param event: параметр контроля событий мыши
    :param points: текущее количество очков
    :param ball_num: количество обычных шариков в 'партии'
    :return: списков списков характеристик обычных шариков,
             текущее количество очков,
             количество обычных шариков в 'партии'
    '''
    x = ball[0]
    y = ball[1]
    rad = ball[2]
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2
    if distance <= rad**2:
        points = points + 1
        del ball_list[ball_list.index(ball)]
    return ball_list, points, ball_num


def click_super_ball(super_ball, super_ball_list, event, points, super_ball_num):
    '''
    Функция обеспечивает обработку клика по особому шарику
    :param super_ball: наследуемая переменная-счетчик (параметры текущего шарика)
    :param super_ball_list: списков списков характеристик особых шариков
    :param event: параметр контроля событий мыши
    :param points: текущее количество очков
    :param super_ball_num: количество особых шариков в 'партии'
    :return: списков списков характеристик особых шариков,
             текущее количество очков,
             количество обычных шариков в 'партии'
    '''
    x = super_ball[0]
    y = super_ball[1]
    rad = super_ball[2]
    distance = (event.pos[0] - x)**2 + (event.pos[1] - y)**2
    if distance <= rad**2:
        points = points + 3
        del super_ball_list[super_ball_list.index(super_ball)]
    return super_ball_list, points, super_ball_num


def balls_moving(ball):
    '''
    Функция обеспечивает передвижение шариков и их отталкивание от границ экрана
    :param ball: наследуемая переменная-счетчик (параметры текущего шарика)
    :return: наследуемая переменная-счетчик (измененные параметры текущего шарика)
    '''
    x = ball[0]
    y = ball[1]
    rad = ball[2]
    speed = ball[4]
    color = ball[5]
    if x >= width - rad:
        ball[3] = math.pi / 2 + random() * math.pi
    if y >= height - rad:
        ball[3] = random() * math.pi
    if rad >= x:
        ball[3] = random() * math.pi - math.pi / 2
    if rad >= y - 40:
        ball[3] = random() * math.pi + math.pi
    angle = ball[3]
    x += int(speed * math.cos(angle))
    y -= int(speed * math.sin(angle))
    ball[0] = x
    ball[1] = y
    circle(screen, color, (x, y), rad)
    return ball


def points_table(points):
    '''
    Функция обеспечивает работу счетчика очков
    :param points: количество очков, выводимое на экран
    :return: возвращаемых параметров нет
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Счёт: " + str(points)
    text = my_font.render(string, 1, BLACK)
    screen.blit(text, (5, 3))


def round_table(game_round):
    '''
    Функция обеспечивает работу счетчика раундов
    :param game_round: порядковый номер текущего раунда
    :return: возвращаемых параметров нет
    '''
    my_font = pygame.font.Font(None, 50)
    string = "Раунд: " + str(game_round)
    text = my_font.render(string, 1, BLACK)
    screen.blit(text, (570, 3))


def time_table(stopwatch):
   '''
   Функция обеспечивает работу таймера
   :param stopwatch: показываемое время, оставшееся до окончания игры
   :return: возвращаемых параметров нет
   '''
   my_font = pygame.font.Font(None, 50)
   string = "Время: " + str(stopwatch)
   if stopwatch <= 10:
       text_color = RED
   else:
       text_color = BLACK
   text = my_font.render(string, 1, text_color)
   screen.blit(text, (width - 173, 3))


# Начальные показатели счетчиков
points = 0
game_round = 1

# Настройки времени
game_time = 60
table_time = game_time + math.trunc((pygame.time.get_ticks() / 1000))
start_time = time.time()
clock = pygame.time.Clock()

finished = False

while not finished:
        clock.tick(FPS)
        if time.time() - game_time > start_time:
            finished = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball in ball_list:
                    ball_list, points, ball_num = click_ball(ball, ball_list, event, points, ball_num)
                for super_ball in super_ball_list:
                    super_ball_list, points, super_ball_num = click_super_ball(super_ball, super_ball_list, event, points, super_ball_num)

        for ball in ball_list + super_ball_list:
            balls_moving(ball)

        if super_ball_list == [] and ball_list == []:
            super_ball_num += 1
            ball_num += 2
            game_round += 1
            max_speed += 1
            super_ball_list = super_ball_load(super_ball_num)
            ball_list = ball_load(ball_num)

        rect(screen, BLUE_1, (0, 0, width, 40))
        rect(screen, BLACK, (0, 0, width, 40), 1)

        points_table(points)
        round_table(game_round)

        stopwatch = table_time - math.trunc((pygame.time.get_ticks() / 1000))
        time_table(stopwatch)

        pygame.display.update()
        screen.fill(BLACK)

name = ''
game_over(points, game_round, game_time, name)

start = False
while not start:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True

pygame.quit()