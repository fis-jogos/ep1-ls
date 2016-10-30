#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pacBum import *
from textClass import *
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
    text_list = list()

    title = textScreen()
    title.text  = "\o   Equipe-se  o/"
    title.pygamePosition = [50,755]

    score = textScreen()
    score.pygamePosition = [450,750]

    lifes = textScreen()
    lifes.pygamePosition = [450, 775]

    time = textScreen()
    time.pygamePosition = [450, 800]

    add_text(text_list, title)
    add_text(text_list, score)
    add_text(text_list, lifes)
    add_text(text_list, time)



#Clock e laço de update da faze
    clock = pygame.time.Clock()
    while True:
        screen.blit(background, (0, 0))

        score.text = "Score: " + str(int(PacBum.points))
        lifes.text = "Vidas: " + str(int(PacBum.lifes))
        time.text = "Tempo: "

        draw_text(screen, text_list)

        screen.blit(PacBum.pygameS,(PacBum.pygamePosition),PacBum.rect)

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
        if pressed_keys[K_UP]:
            jump(PacBum, 0, -100)
            animation_pacBum(PacBum)

        #PULAR PARA FRENTE
        if pressed_keys[K_UP] and pressed_keys[K_RIGHT]:
            jump(PacBum, 10, -100)
            animation_pacBum(PacBum)

        #PULAR PARA TRÁS
        if pressed_keys[K_UP] and pressed_keys[K_LEFT]:
            jump(PacBum, -10, -100)
            animation_pacBum(PacBum)


        #update da cena
        pygame.display.update()

        #clock máximo do update
        time_passed = clock.tick(30)

