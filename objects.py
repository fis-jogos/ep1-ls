#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pygame.locals import *
from sys import exit

class obj_game:

    def __init__(self):

        self.image = 'images/'
        self.inScreen = False
        self.mass = 10
        self.pygameS = 0
        self.position  = [50,625]
        self.rect = [0,0,60,60]
        self.gravity  = 0
        self.cont_animation = 0
        self.who_touch = "default"
        self.split_range = 0
        self.vel_in_x = 0
