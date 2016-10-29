#! /usr/bin/env python
import pygame
import time
from pygame.locals import *
from sys import exit

class selectArrow:

    def __init__(self):
        self.name = 'images/select.png'
        self.arr = pygame.image.load(self.name).convert_alpha()
        self.value = 0
        self.posX = 500
        self.posY = 250

def setArrow():
    select = selectArrow()
    return select

