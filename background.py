#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

class background:

    def __init__(self):

        self.image = "images/bg_menu.png"


def draw_background(screen, self):

        background = pygame.image.load(self.image).convert()
        screen.blit(background,(0,0))
