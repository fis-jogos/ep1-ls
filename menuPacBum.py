#! /usr/bin/env python
import pygame
import time
from menuArrow import *
from colectScreen import *
from screenCredits import *
from pygame.locals import *
from sys import exit

#Define o plano de fundo do menu principal
def setBackgroud():
    background_filename = 'images/bg_menu.png'
    background = pygame.image.load(background_filename).convert()
    return background

#Inicializa o menu principal
def mainMenu():


    #inicializa os objetos do menu principal
    pygame.font.init()
    screen = pygame.display.set_mode((1300, 700), 0, 32)
    pygame.display.set_caption('PAC BUM! > Menu Principal')
    background = setBackgroud()

    #textos que aparecem no menu principal
    font_name = pygame.font.get_default_font()
    game_font = pygame.font.SysFont(font_name, 32)
    textInit = game_font.render('INICIAR', 1, (0, 0, 0))
    textOptions = game_font.render('OPÇÕES',1,(0,0,0))
    textCredit = game_font.render('CRÉDITOS',1,(0,0,0))
    textExit = game_font.render('SAIR',1,(0,0,0))
    textVersion = game_font.render('V - 0.0.1', 1, (0,0,0))

    #cria a seta de controle do menu principal
    arrow = selectArrow()

    #Clock e laço de update do menu principal
    clock = pygame.time.Clock()
    while True:

        #Habilitação dos textos do menu principal
        screen.blit(background, (0, 0))
        screen.blit(textInit, (550, 265))
        screen.blit(textOptions, (550, 315))
        screen.blit(textCredit, (550, 365))
        screen.blit(textExit, (550, 415))
        screen.blit(textVersion,(1210,675))

        #A posição da seta em Y muda de acordo com o valor selecionado. y + 0 * 50 ou y + 1 * 50 ou y + 2 * 50... Pra mudar a posição dela.
        screen.blit(arrow.arr, (arrow.posX, (arrow.posY + arrow.value * 50)))

        #Habilita que a janela seja fechada pelo "x"
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


        #Habilita os controles do jogo pelo teclado
        pressed_keys = pygame.key.get_pressed()

        #Comandos da seta de controle do menu principal
        #Para cima
        if pressed_keys[K_UP]:
            arrow.value -= 1
            time.sleep(1/7)
            if arrow.value < 0:
                arrow.value = 0

        #Para baixo
        if pressed_keys[K_DOWN]:
            arrow.value += 1
            time.sleep(1/7)
            if arrow.value > 3:
                arrow.value = 3

        #Confrima opção
        if pressed_keys[K_RETURN]:
            if arrow.value == 0:
                colectScreen()
            elif arrow.value == 1:
                print('1')
            elif arrow.value == 2:
                screenCredits()
            if arrow.value == 3:
                pygame.quit()
                exit()

        #Atualização dos objetos na tela
        pygame.display.update()

        #Clock máximo do uptade
        time_passed = clock.tick(30)