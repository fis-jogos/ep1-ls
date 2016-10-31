#! /usr/bin/env python
import pygame
import time
from FGAme import *
from pacBum import *
from textClass import *
from environment import *
from background import *
from objects import *
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
    bombs = textScreen()
    bombs.pygamePosition = [650, 750]

    add_text(text_list, title)
    add_text(text_list, comment)
    add_text(text_list, score)
    add_text(text_list, lifes)
    add_text(text_list, bombs)
    add_text(text_list, time)

    #Inicializa os objetos da tela.
    world = environment()
    PacBum = pacBum()

    #Cow skull
    skull = obj_game()
    skull.image = "images/cow_skull.png"
    skull.pygameS = pygame.image.load(skull.image).convert_alpha()
    skull.inScreen = False
    skull.position = [1100, 610]
    skull.rect = [0,0,125,125]

    #Pac bomb
    bomb = obj_game()
    bomb.image = "images/pac_bomb.png"
    bomb.pygameS = pygame.image.load(bomb.image).convert_alpha()
    bomb.inScreen = False
    bomb.position = [1100, 500]
    bomb.rect = [0,0,125,125]

    #Super points
    spoints = obj_game()
    spoints.image = "images/pac_super_points.png"
    spoints.pygameS = pygame.image.load(spoints.image).convert_alpha()
    spoints.inScreen = False
    spoints.position = [900, 300]
    spoints.rect = [0,0,125,125]

    #Vida
    lifes = obj_game()
    lifes.image = "images/pac_life.png"
    lifes.pygameS = pygame.image.load(lifes.image).convert_alpha()
    lifes.inScreen = False
    lifes.position = [800, 300]
    lifes.rect = [0,0,125,125]

    #Veneno
    venon = obj_game()
    venon.image = "images/pac_venon.png"
    venon.pygameS = pygame.image.load(venon.image).convert_alpha()
    venon.inScreen = False
    venon.position = [500, 300]
    venon.rect = [0,0,125,125]

    #RIP
    rip = obj_game()
    rip.image = "images/rip.png"
    rip.pygameS = pygame.image.load(rip.image).convert_alpha()
    rip.inScreen = False
    rip.position = [500, 300]
    rip.rect = [0,0,125,125]


    add_objects(world, skull)
    add_objects(world, bomb)
    add_objects(world, spoints)
    add_objects(world, lifes)
    add_objects(world, venon)
    add_objects(world, rip)













    #Clock e laço de update da faze
    clock = pygame.time.Clock()
    while True:

        draw_background(screen, bg)

        score.text = "Score: " + str(int(PacBum.points))
        lifes.text = "Vidas: " + str(int(PacBum.lifes))
        time.text = "Tempo: "
        bombs.text = "Bombas: " + str(int(PacBum.bombs))

        draw_text(screen, text_list)
        draw_objects(screen, world)

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


        #SUBIR
        if pressed_keys[K_UP]:
            PacBum.position[1] = 575
            animation_pacBum(PacBum)


        #DESCER
        if pressed_keys[K_DOWN]:
            PacBum.position[1] = 625
            animation_pacBum(PacBum)


        #update da cena
        pygame.display.update()

        #clock máximo do update
        time_passed = clock.tick(30)

