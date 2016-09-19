import pygame

class PacBum:
	
	mass = 1
	gravity = 10
	status = True
	imagestatus = False
	posx = 0
	posy = 0
	velx = 0
	vely = 0
	acx = 0
	acy = 0
	forcex = 0
	forcey = 0
	
	def __init__(self, actor, mass, gravity, status, imagestatus, posx, posy, velx, vely, acx, acy, forcex, forcey):

		self.actor = actor
		self.mass = mass
		self.gravity = gravity
		self.status = status
		self.posx = posx
		self.posy = posy
		self.velx = velx
		self.vely = vely
		self.acx = acx
		self.acy = acy
		self.forcex = forcex
		self.forcey = forcey

	def draw(self):
		self.actor.x = self.posx
		self.actor.y = self.posy
		self.actor.draw()

	def acelerationXY(self):

		self.acx = (self.forcex/self.mass)
		self.acy = (self.forcey/self.mass) + self.gravity

	def velocityXY(self, dt):

		self.velx = self.velx + self.acx * dt
		self.vely = self.vely + self.acy * dt

	def positionXY(self, dt):

		self.posx = self.posx + self.velx * dt + ((self.acx*(dt*dt)) / 2)
		self.posy = self.posy + self.vely * dt + ((self.acy*(dt*dt)) / 2)

	def addforcex(self):
		if self.forcex < 900:
			self.forcex += 100
		else:
			self.forcex = 900

	def rmforcex(self):
		if self.forcex > 100:
			self.forcex -= 100
		else:
			self.forcex = 100

	def addforcey(self):
		if self.forcey < 900:
			self.forcey += 100
		else:
			self.forcey = 900

	def rmforcey(self):
		if self.forcey > 100:
			self.forcey -= 100
		else:
			self.forcey = 100





	def addvelx(self):
		if self.velx < 900:
			self.velx += 100
		else:
			self.velx = 900

	def rmvelx(self):
		if self.velx > 100:
			self.velx -= 100
		else:
			self.velx = 100

	def addvely(self):
		if self.vely < 900:
			self.vely += 100
		else:
			self.vely = 900

	def rmvelyy(self):
		if self.vely > 100:
			self.vely -= 100
		else:
			self.vely = 100





class Cannon:

	mass = 1
	gravity = 10
	posx = 0
	posy = 0
	theta = 0


	def __init__(self, actor, mass, gravity, posx, posy, theta):

		self.actor = actor
		self.mass = mass
		self.gravity = gravity
		self.posx = posx
		self.posy = posy
		self.theta = theta

	def draw(self):
		self.actor.x = self.posx
		self.actor.y = self.posy
		self.actor.draw()

