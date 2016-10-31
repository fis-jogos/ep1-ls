#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pygame.locals import *
from sys import exit


#Classe do personagem principal
class pacBum:

    def __init__(self):
        self.image = 'images/pacbum_front.png'
        self.lifes = 0
        self.dead = False
        self.mass = 10
        self.raio = 30
        self.pygameS = pygame.image.load(self.image).convert_alpha()
        self.position  = [50,640]
        self.rect = [0,0,60,60]
        self.cont_animation = 0
        self.points = 0
        self.phase = 0
        self.gravity = 0
        self.bombs = 0

#Função da animação do personagem principal.
def animation_pacBum(self):

    self.cont_animation += 0.1

    if self.cont_animation < 0.75:
        self.rect[0] = 0

    elif self.cont_animation > 0.75:
        self.rect[0] = 60

    if self.cont_animation >= 1.25:
        self.cont_animation = 0


def animation_update(self, image):
    self.image = image
    self.pygameS = pygame.image.load(self.image).convert_alpha()


#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def forward_colectScreen(self, speedX):

    animation_update(self, 'images/pacbum_front.png')

    if self.position[0] >= 1100:
        speedX = 0


    self.position[0] = self.position[0] + speedX





#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def backward_colectScreen(self, speedX):

    animation_update(self, 'images/pacbum_back.png')

    if self.position[0] <= 50:
        speedX = 0

    self.position[0] = self.position[0] - speedX





