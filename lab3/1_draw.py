import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (248, 248, 255), (0, 0, 500, 500), 0)

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)

circle(screen, (255, 0, 0), (165, 150), 20)
circle(screen, (0, 0, 0), (165, 150), 20, 2)

circle(screen, (255, 0, 0), (235, 150), 20)
circle(screen, (0, 0, 0), (235, 150), 20, 2)

circle(screen, (0, 0, 0), (165, 150), 10)
circle(screen, (0, 0, 0), (235, 150), 10)

rect(screen, (0, 0, 0), (150, 210, 100, 20))
line(screen, (0, 0, 0), [100,80], [185,130], 13)
line(screen, (0, 0, 0), [308,90], [213,130], 13)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()