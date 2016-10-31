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

    obj.gravity = self.gravity
    self.objects.append(obj)

def draw_objects(screen, self):

    for obj in self.objects:

        animation_obj(obj)
        screen.blit(obj.pygameS,(obj.position),obj.rect)

def animation_obj(obj):

    if obj.inScreen == False:

        obj.cont_animation += 0.1

        if obj.cont_animation < 0.75:
            obj.rect[0] = 0

        elif obj.cont_animation > 0.75:
            obj.rect[0] = 125

        if obj.cont_animation >= 1.25:
            obj.cont_animation = 0


