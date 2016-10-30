#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pacBum import *
from pygame.locals import *
from sys import exit


# Define o backgroud
def setBackgroud():
    background_filename = 'images/bg_colect_screen.png'
    background = pygame.image.load(background_filename).convert()
    return background



# cria a faze
def colectScreen():

    pygame.font.init()
    screen = pygame.display.set_mode((1260, 840), 0, 32)
    background = setBackgroud()

    PacBum = pacBum()
    PacBum.fgameS.pos  = (50, 100)
    PacBum.fgameS.gravity = 7
    print( PacBum.fgameS.pos)

    font_name = pygame.font.get_default_font()
    game_font= pygame.font.SysFont(font_name, 28)

    textTitle = game_font.render('\O/      EQUIPE-SE     \O/', 1, (0, 0, 0))



#Clock e laço de update da faze
    clock = pygame.time.Clock()
    while True:

        #Atualização dos textos que aparecem na tela
        score = "Score: " + str(int(PacBum.points))
        lifes = "Vidas: " + str(int(PacBum.lifes))
        time = "Tempo: "

        textPoints = game_font.render(score,1,(0,0,0))
        textLifes = game_font.render(lifes,1,(0,0,0))
        textTime = game_font.render(time,1,(0,0,0))


        screen.blit(background, (0, 0))
        screen.blit(PacBum.pygameS,(PacBum.fgameS.pos),PacBum.rect)
        screen.blit(textTitle, (50, 775))
        screen.blit(textPoints, (450, 750))
        screen.blit(textLifes, (450, 775))
        screen.blit(textTime, (450, 800))


        #Habilita que a tela seja fechada no "x"
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()




        #Habilita as teclas para o controle
        pressed_keys = pygame.key.get_pressed()
        gravity_influence(PacBum)

        #ANDAR PARA FRENTE
        if pressed_keys[K_RIGHT]:
            animation_pacBum(PacBum)
            forward_colectScreen(PacBum, 10)





        #ANDAR PARA TRÁS
        if pressed_keys[K_LEFT]:
            animation_pacBum(PacBum)
            backward_colectScreen(PacBum, 10)


        #PULAR
        if pressed_keys[K_SPACE]:
            jump(PacBum, 0, -75)
            animation_pacBum(PacBum)

        #PULAR PARA FRENTE
        if pressed_keys[K_SPACE] and pressed_keys[K_RIGHT]:
            jump(PacBum, 10, -75)
            animation_pacBum(PacBum)

        #PULAR PARA TRÁS
        if pressed_keys[K_SPACE] and pressed_keys[K_LEFT]:
            jump(PacBum, -10, -75)
            animation_pacBum(PacBum)


        #update da cena
        pygame.display.update()

        #clock máximo do update
        time_passed = clock.tick(30)

