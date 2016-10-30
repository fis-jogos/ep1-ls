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
        self.fgameS = world.add.circle(25, pos=(400, 300), color='green', mass = 1000)
        self.pygameS = pygame.image.load(self.image).convert_alpha()
        self.pygamePosition  = [50,625]
        self.rect = [0,0,60,60]
        self.cont_animation = 0
        self.points = 0
        self.phase = 0



#Função da animação do personagem principal.
def animation_pacBum(self):

    self.cont_animation += 0.1

    if self.cont_animation < 0.75:
        self.rect[0] = 0

    elif self.cont_animation > 0.75:
        self.rect[0] = 60

    if self.cont_animation >= 1.25:
        self.cont_animation = 0





#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def forward_colectScreen(self, speedX):

    self.image = 'images/pacbum_front.png'
    self.pygameS = pygame.image.load(self.image).convert_alpha()
    if self.pygamePosition[0] >= 1100:
        speedX = 0


    self.pygamePosition[0] = self.pygamePosition[0] + speedX





#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def backward_colectScreen(self, speedX):

    self.image = 'images/pacbum_back.png'
    self.pygameS = pygame.image.load(self.image).convert_alpha()

    if self.pygamePosition[0] <= 50:
        speedX = 0

    self.pygamePosition[0] = self.pygamePosition[0] - speedX




#Função e detecção de colisão do pulo do personagem principal na tela colectScreen
def jump(self, speedX, speedY):

    if self.fgameS.pos[1] < 625:
        speedY = 0

    return self.fgameS.move(speedX, speedY)

def gravity_influence(self):

    G = self.fgameS.gravity[1]

    if self.fgameS.pos[1] >= 625:
        G = 0

    return self.fgameS.move(0, -G)




