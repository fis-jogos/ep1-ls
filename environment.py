#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pygame.locals import *
from sys import exit

class environment:

    def __init__(self):

        self.gravity = 10
        self.objects = list(objects)

