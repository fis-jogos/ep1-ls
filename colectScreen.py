#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pacBum import *
from textClass import *
from environment import *
from background import *
from pygame.locals import *
from sys import exit



# cria a faze
def colectScreen():

    #Inicializa a tela.
    pygame.font.init()
    screen = pygame.display.set_mode((1260, 840), 0, 32)
    pygame.display.set_caption('PAC BUM! > Coleta parte 1')

    #Inicializa o plano de fundo.
    bg = background()
    bg.image = "images/bg_colect_screen.png"


    #Inicializa os textos da tela
    text_list = list()
    title = textScreen()
    title.text  = "Coleta 1 - Velho Oeste"
    title.pygamePosition = [50,755]
    comment = textScreen()
    comment.text = "Equipe-se!"
    comment.pygamePosition = [50, 800]
    score = textScreen()
    score.pygamePosition = [450,750]
    lifes = textScreen()
    lifes.pygamePosition = [450, 775]
    time = textScreen()
    time.pygamePosition = [450, 800]

    add_text(text_list, title)
    add_text(text_list, comment)
    add_text(text_list, score)
    add_text(text_list, lifes)
    add_text(text_list, time)

    #Inicializa os objetos da tela.
    PacBum = pacBum()
    world = environment()

    add_objects(world, PacBum)

    #Clock e laço de update da faze
    clock = pygame.time.Clock()
    while True:

        draw_background(screen, bg)

        score.text = "Score: " + str(int(PacBum.points))
        lifes.text = "Vidas: " + str(int(PacBum.lifes))
        time.text = "Tempo: "

        draw_text(screen, text_list)
        draw_pacbum(screen, world)

        #Habilita que a tela seja fechada no "x"
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        #Habilita as teclas para o controle
        pressed_keys = pygame.key.get_pressed()

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

