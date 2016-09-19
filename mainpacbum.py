import sys; sys.path.append('.')
from pacbum import *
from environment import * 
from pygame import *

#Dimensões da tela
WIDTH = 1300
HEIGHT = 700


#Ambientação
env = environment(gravity = 10)

PacBum = PacBum(Actor('persona_1'), mass = 100, gravity = env.gravity, status = True, imagestatus = False, 
				posx =  130, posy = 590, velx = 100, vely = -100, acx = 0, acy = 0, forcex =0, forcey = 0)

Cannon = Cannon(Actor('cannon'), mass = 1, gravity = env.gravity, posx = 100, posy = 580, theta = 0)

WheelCannon = Actor('roda_canhao', pos=(30, 630))

Tnumber = Actor('0', pos=(530,325))
Unumber = Actor('0', pos=(630,325))
Vnumber = Actor('0', pos=(730, 325))
BoardView = Actor('force_x', pos=(630, 200))
Background = Actor('background', pos=(650,350))


#Objetos no ambiente
env.add(Background)
env.add(PacBum)
env.add(Cannon)
env.add(WheelCannon)


def draw():
	env.draw()


def convertnumber(value):
	if value > 0:
		number = value / 100
		number = int(number)
		number = str(number)
		return number
	else:
		number = (value / 100) * (-1)
		number = int(number)
		number = str(number)
		return number		

def update(dt):

	screen.clear()

	if keyboard.space:
		PacBum.acelerationXY()
		PacBum.velocityXY(dt)
		PacBum.positionXY(dt)

	#Mostrar Força X
	if keyboard.q:
		BoardView.image = 'force_x'
		BoardView.draw()
		aux = convertnumber(PacBum.forcex)
		Tnumber.image = aux
		Tnumber.draw()
		Unumber.draw()
		Vnumber.draw()


	#Mostrar Força Y
	if keyboard.w:
		BoardView.image = 'force_y'
		aux = convertnumber(PacBum.forcey)
		Tnumber.image = aux
		BoardView.draw()
		Tnumber.draw()
		Unumber.draw()
		Vnumber.draw()


	#Add Força X
	if keyboard.f & keyboard.p:
		PacBum.addforcex()
		time.delay(100)

	#Remove Força X
	if keyboard.f & keyboard.l:
		PacBum.rmforcex()
		time.delay(100)


	#Add Força Y
	if keyboard.r & keyboard.p:
		PacBum.addforcey()
		time.delay(100)

	#Remove Força Y
	if keyboard.r & keyboard.l:
		PacBum.rmforcey()
		time.delay(100)



	#Mostrar velocidade X
	if keyboard.a:
		BoardView.image = 'velocity_x'
		aux = convertnumber(PacBum.velx)
		Tnumber.image = aux
		BoardView.draw()
		Tnumber.draw()
		Unumber.draw()
		Vnumber.draw()

	#Mostrar velocidade Y
	if keyboard.s:
		BoardView.image = 'velocity_y'
		aux = convertnumber(PacBum.vely)
		Tnumber.image = aux
		BoardView.draw()
		Tnumber.draw()
		Unumber.draw()
		Vnumber.draw()

	#Add velocidade X
	if keyboard.e & keyboard.p:
		PacBum.addvelx()
		time.delay(100)
 
	#Remove velocidade X
	if keyboard.e & keyboard.l:
		PacBum.rmvelx()
		time.delay(100)


	#Add velocidade Y
	if keyboard.d & keyboard.p:
		PacBum.addvely()
		time.delay(100)

	#Remove velocidade Y
	if keyboard.d & keyboard.l:
		PacBum.rmvely()
		time.delay(100)


