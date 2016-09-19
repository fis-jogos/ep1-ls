import sys; sys.path.append('.')
from pacbum import *
from environment import * 
from pygame import *

#Dimensões da tela
WIDTH = 1300
HEIGHT = 700

#Ambientação
env = environment(gravity = 10)

PacBum = PacBum(Actor('persona_1'), mass = 1000, gravity  = env.gravity, status = True, imagestatus = False, 
				posx =  110, posy = 580, velx = 400, vely = -0, acx = 0, acy = 0, forcex =0, forcey = 0)

Cannon = Cannon(Actor('canhao'), mass = 1, gravity = env.gravity, posx = 100, posy = 590, theta = 0)

WheelCannon = Actor('roda_canhao', pos=(30, 630))

TnumberGravity = Actor('0', pos=(600,325))
UnumberGravity = Actor('0', pos=(680,325))
BoardView = Actor('gravidade', pos=(630, 200))


#Objetos no ambiente
env.add(PacBum)
env.add(Cannon)
env.add(WheelCannon)


def draw():
	env.draw()



def update(dt):

	screen.clear()

	if keyboard.space:
		PacBum.acelerationXY()
		PacBum.velocityXY(dt)
		PacBum.positionXY(dt)
		if(PacBum.posy > 665):
			PacBum.gravity = 0
			PacBum.velx = 0
			PacBum.vely = 0

	if keyboard.g:

		if env.gravity < 100:
			TnumberGravity.image = '0'
			UnumberGravity.draw()
			TnumberGravity.draw()
			BoardView.draw()
		else:
			TnumberGravity.image = Tnumber
			BoardView.image = 'gravidade'
			UnumberGravity.draw()
			TnumberGravity.draw()
			BoardView.draw()


	if keyboard.g & keyboard.up:

		if env.gravity > 900:
			env.gravity = 900
			TnumberGravity.image = '9'
		else:
			env.gravity += 100
			time.delay(400)
			Tnumber = env.gravity / 100
			Tnumber = int(Tnumber)
			Tnumber = str(Tnumber)


	if keyboard.g & keyboard.down:

		if env.gravity < 100:
			env.gravity = 100
			TnumberGravity.image = '1'
		else:
			env.gravity -= 100
			time.delay(400)
			Tnumber = env.gravity / 100
			Tnumber = int(Tnumber)
			Tnumber = str(Tnumber)