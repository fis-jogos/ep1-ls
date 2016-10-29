#! /usr/bin/env python
import pygame
import time
from menuArrow import *
from pygame.locals import *
from sys import exit


def setBackgroud():
    background_filename = 'images/bg_menu.png'
    background = pygame.image.load(background_filename).convert()
    return background


def mainMenu():


    pygame.font.init()
    font_name = pygame.font.get_default_font()
    game_font = pygame.font.SysFont(font_name, 32)

    screen = pygame.display.set_mode((1300, 700), 0, 32)
    pygame.display.set_caption('PAC BUM! > Menu Principal')
    background = setBackgroud()
    arrow = setArrow()
    textInit = game_font.render('INICIAR', 1, (0, 0, 0))
    textOptions = game_font.render('OPÇÕES',1,(0,0,0))
    textCredit = game_font.render('CRÉDITOS',1,(0,0,0))
    textExit = game_font.render('SAIR',1,(0,0,0))
    textVersion = game_font.render('V - 0.0.1', 1, (0,0,0))


    clock = pygame.time.Clock()
    while True:

        screen.blit(background, (0, 0))
        screen.blit(textInit, (550, 265))
        screen.blit(textOptions, (550, 315))
        screen.blit(textCredit, (550, 365))
        screen.blit(textExit, (550, 415))
        screen.blit(textVersion,(1210,675))
        #Explicação da proxima linha: A posição da seta em Y muda de acordo com o valor selecionado. y + 0 * 50 ou y + 1 * 50 ou y + 2 * 50... Pra mudar a posição dela.
        screen.blit(arrow.arr, (arrow.posX, (arrow.posY + arrow.value * 50)))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            arrow.value -= 1
            time.sleep(1/7)
            if arrow.value < 0:
                arrow.value = 0


        if pressed_keys[K_DOWN]:
            arrow.value += 1
            time.sleep(1/7)
            if arrow.value > 3:
                arrow.value = 3

        pygame.display.update()
        time_passed = clock.tick(30)