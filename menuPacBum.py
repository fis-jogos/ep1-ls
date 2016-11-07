#! /usr/bin/env python
import pygame
import time
from menuArrow import *
from colectScreen import *
from screenCredits import *
from background import *
from pygame.locals import *
from sys import exit

#Inicializa o menu principal
def mainMenu():


    #inicializa os objetos do menu principal
    pygame.font.init()
    screen = pygame.display.set_mode((1300, 700), 0, 32)
    pygame.display.set_caption('PAC BUM! > Menu Principal')

    #Definição do background.
    bg = background()
    bg.image = "images/bg_menu.png"
    bg.rect = [0,0,1300,1300]


    #textos que aparecem no menu principal
    list_text = list()

    textInit = textScreen()
    textInit.text = "INICIAR"
    textInit.pygamePosition =[550, 265]

    textOptions = textScreen()
    textOptions.text = "OPÇÕES"
    textOptions.pygamePosition = [550, 315]

    textCredit = textScreen()
    textCredit.text = "CRÉDITOS"
    textCredit.pygamePosition = [550,365]

    textExit = textScreen()
    textExit.text = "SAIR"
    textExit.pygamePosition = [550,415]

    textVersion = textScreen()
    textVersion.text = "V - 0.1.0"
    textVersion.pygamePosition = [1210,675]

    add_text(list_text, textInit)
    add_text(list_text, textOptions)
    add_text(list_text, textCredit)
    add_text(list_text, textExit)
    add_text(list_text, textVersion)


    #cria a seta de controle do menu principal
    arrow = selectArrow()



    #Clock e laço de update do menu principal
    clock = pygame.time.Clock()
    while True:

        #Desenha o plano de fundo.
        draw_background(screen, bg)

        #Desenha os textos da tela.
        draw_text(screen, list_text)

        #Desenha a seta do menu principal.
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