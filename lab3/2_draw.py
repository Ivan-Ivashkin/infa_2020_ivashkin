import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((927, 769))

rect(screen, (255, 240, 245), (0, 0, 927, 769))

circle(screen, (210, 105, 30), (450, 820), 300)
circle(screen, (255, 228, 196), (450, 400), 230)

circle(screen, (255, 228, 196), (450, 400), 220)
circle(screen, (255, 228, 196), (450, 400), 220)

ellipse(screen, (135, 206, 250), (320, 320, 100, 90))
ellipse(screen, (0, 0, 0), (320, 320, 100, 90), 1)

ellipse(screen, (135, 206, 250), (480, 320, 100, 90))
ellipse(screen, (0, 0, 0), (480, 320, 100, 90), 1)

ellipse(screen, (0, 0, 0), (515, 357, 30, 27))
ellipse(screen, (0, 0, 0), (355, 357, 30, 27))

line(screen, (255, 228, 196), [85, 50], [190, 570], 40)
line(screen, (255, 228, 196), [800, 50], [710, 580], 40)

polygon(screen, (255, 0, 0), [(350, 480), (450, 545), (550, 480)])
polygon(screen, (0, 0, 0), [(350, 480), (450, 545), (550, 480)], 1)

polygon(screen, (139, 69, 19), [(410, 430), (450, 460), (490, 430)])
polygon(screen, (0, 0, 0), [(410, 430), (450, 460), (490, 430)], 1)

polygon(screen, (210, 105, 30), [(145, 575), (235, 535), (295, 605), (245, 680), (155, 665)])
polygon(screen, (0, 0, 0), [(145, 575), (235, 535), (295, 605), (245, 680), (155, 665)], 1)

polygon(screen, (210, 105, 30), [(605, 605), (665, 535), (755, 575), (745, 665), (655, 680)])
polygon(screen, (0, 0, 0), [(605, 605), (665, 535), (755, 575), (745, 665), (655, 680)], 1)

rect(screen, (0, 255, 0), (0, 0, 927, 90))
rect(screen, (0, 0, 0), (0, 0, 927, 90), 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()