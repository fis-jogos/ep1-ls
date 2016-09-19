import sys; sys.path.append('.')
from pacbum import *
from environment import * 
from time import *

#Dimensões da tela
WIDTH = 1300
HEIGHT = 700

#Ambientação
env = environment(gravity = 10)

PacBum = PacBum(Actor('persona_1'), mass = 1000, gravity  = env.gravity, status = True, imagestatus = False, 
				posx =  130, posy = 550, velx = 400, vely = -100, acx = 0, acy = 0, forcex =0, forcey = 0)

Cannon = Cannon(Actor('canhao'), mass = 1, gravity = env.gravity, posx = 100, posy = 590, theta = 0)

WheelCannon = Actor('roda_canhao', pos=(30, 630))

TnumberGravity = Actor('1', pos=(100,10))

UnumberGravity = Actor('0', pos=(140,10))

#Objetos no ambiente
env.add(PacBum)
env.add(Cannon)
env.add(WheelCannon)


def draw():
	env.draw()

def update(dt):

	screen.clear()
	PacBum.acy = (PacBum.forcey/PacBum.mass) + PacBum.gravity
	PacBum.vely = (PacBum.vely + PacBum.acy * dt)
	PacBum.posy = PacBum.posy + PacBum.vely * dt + ((PacBum.acy*(dt*dt)) / 2)
	
	PacBum.acx = (PacBum.forcex/PacBum.mass)
	PacBum.velx = PacBum.velx + PacBum.acx * dt
	PacBum.posx = PacBum.posx + PacBum.velx * dt + ((PacBum.acx*(dt*dt)) / 2)



