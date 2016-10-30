#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pygame.locals import *
from sys import exit

class environment:

    def __init__(self):
        self.objects = list()
        self.gravity = 0


def add_objects(self, obj):

    self.objects.append(obj)

def draw_pacbum(screen, self):

    for obj in self.objects:
        screen.blit(obj.pygameS,(obj.position),obj.rect)