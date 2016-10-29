#! /usr/bin/env python
import pygame
import time
from menuArrow import *
import menuPacBum
from pygame.locals import *
from sys import exit

def setBackgroud():
    background_filename = 'images/bg_menu_back.png'
    background = pygame.image.load(background_filename).convert()
    return background

def screenCredits():
    pygame.init()
    pygame.font.init()
    font_name = pygame.font.get_default_font()
    game_font = pygame.font.SysFont(font_name, 32)
    textCred_1 = game_font.render("Universidade de Brasília - 2016", 1, (0,0,0))
    textCred_2 = game_font.render("PacBum V - 0.0.1 por: Lucas S. Souza", 1, (0,0,0))
    textCred_3 = game_font.render("Email: lucas.soaresouza@gmail.com", 1, (0,0,0))


    screen = pygame.display.set_mode((1300, 700), 0, 32)
    pygame.display.set_caption('PAC BUM! > Creditos')
    background = setBackgroud()


    credPos_1= [400, 700]
    credPos_2= [400, 740]
    credPos_3= [400, 780]
    speed = 3

    clock = pygame.time.Clock()
    while True:
        screen.blit(background, (0, 0))
        if credPos_1[1] > 200:
            credPos_1[1] -= speed
            credPos_2[1] -= speed
            credPos_3[1] -= speed
        else:
            credPos_1[1] = 200
            credPos_2[1] = 240
            credPos_3[1] = 280

        screen.blit(textCred_1, credPos_1)
        screen.blit(textCred_2, credPos_2)
        screen.blit(textCred_3, credPos_3)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_ESCAPE]:
            pygame.quit()
            menuPacBum.mainMenu()

        pygame.display.update()
        time_passed = clock.tick(30)

