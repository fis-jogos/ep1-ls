import sys; sys.path.append('.')
from pacbum import *

#Dimensões da tela
WIDTH = 1300
HEIGHT = 700

#Constantes

#Criar PacBUm
PacBum = PacBum(Actor('persona_1'), mass = 1, gravity  = 10, status = True, posx =  100, posy = 100)

#Cria Canhao
Cannon = Cannon(Actor('canhao'), mass = 1, gravity = 10, posx = 100, posy = 590 )

WheelCannon = Actor('roda_canhao', pos=(30, 630))

def draw():
	PacBum.draw()
	Cannon.draw()
	WheelCannon.draw()
