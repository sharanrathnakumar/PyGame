import pygame
import sys
import os
from pygame.locals import *

x = 10
y = 10
screen = 0


def myquit():
    pygame.quit()
    sys.ext(0)


def check_inputs(events):
    global x, y, screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    myquit()
                elif event.key == K_LEFT:
                    x -= 5
                    print("Left")
                elif event.key == K_RIGHT:
                    x += 5
                    print("RIGHT")
                else:
                    print(event.key)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, 50, 50, 10))
    pygame.display.update()


def main():
    global screen
    Screen_width = 600
    Screen_Height = 480

    pygame.init()
    window = pygame.display.set_mode((Screen_width, Screen_Height))
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.get_surface()
    pygame.display.update()
    while True:
        check_inputs(pygame.event.get())


main()
