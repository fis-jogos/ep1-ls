#! /usr/bin/env python
import pygame
from FGAme import *
from pygame.locals import *
from sys import exit

class ship:

    def __init__(self):
        self.struct = world.add.aabb(shape=(30,80), pos=(50, 50), mass=2000)
        self.image = 'ship.png'
        self.obj = pygame.image.load(self.image).convert_alpha()

    def setShip():
        select = ship()
        return select


pygame.init()
screen = pygame.display.set_mode((300, 300), 0, 32)
nave = ship()
print (nave.struct.pos[0])
print (nave.struct.pos[1])

clock = pygame.time.Clock()


while True:

    posx = int(float(nave.struct.pos[0]))
    posy = int(float(nave.struct.pos[1]))
    screen.blit(nave.obj, (posx, posy))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pygame.display.update()
    time_passed = clock.tick(30)