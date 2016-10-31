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
        self.split_range = 10
        self.pygameS = pygame.image.load(self.image).convert_alpha()
        self.fgameS = world.add.circle(20, pos=(400, 300), color='green', mass = 500)
        self.position  = [625,655]
        self.rect = [0,0,60,60]
        self.cont_animation = 0
        self.points = 0
        self.bombs = 0
        self.vel_in_x = 20
        self.vel_in_y = 20

#Função da animação do personagem principal.
def animation_pacBum(self):

    self.cont_animation += 0.1

    if self.cont_animation < 0.75:
        self.rect[0] = 0

    elif self.cont_animation > 0.75:
        self.rect[0] = 60

    if self.cont_animation >= 1.25:
        self.cont_animation = 0

#Função que desenha o Pac Bum
def draw_pacbum(screen, self):

    screen.blit(self.pygameS,(self.position),self.rect)

#Função que atualiza o lado para o qual o pac bum está virado
def animation_update(self, image):
    self.image = image
    self.pygameS = pygame.image.load(self.image).convert_alpha()


#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def forward_colectScreen(self):

    animation_update(self, 'images/pacbum_front.png')

    if self.position[0] >= 1000:
        self.position[0] = 990


    self.position[0] = self.position[0] + self.vel_in_x





#Função e detecção de colisão do movimento do personagem principal na tela colectScreen
def backward_colectScreen(self):

    animation_update(self, 'images/pacbum_back.png')

    if self.position[0] <= 200:
        self.position[0] = 210


    self.position[0] = self.position[0] - self.vel_in_x


#Função que marca o Pac Bum como morto
def pacbum_is_dead(self):

        if self.dead == True:
            self.vel_in_x = 0
            self.position = [3000,3000]
            return True
        else:
            pass






