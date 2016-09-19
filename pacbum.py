class PacBum:
	
	mass = 1
	gravity = 10
	status = True
	posx = 0
	posy = 0
	
	def __init__(self, actor, mass, gravity, status, posx, posy):

		self.actor = actor
		self.mass = mass
		self.gravity = gravity
		self.status = status
		self.posx = posx
		self.posy = posy

	def draw(self):
		self.actor.x = self.posx
		self.actor.y = self.posy
		self.actor.draw() 

class Cannon:

	mass = 1
	gravity = 10
	posx = 0
	posy = 0

	def __init__(self, actor, mass, gravity, posx, posy):

		self.actor = actor
		self.mass = mass
		self.gravity = gravity
		self.posx = posx
		self.posy = posy

	def draw(self):
		self.actor.x = self.posx
		self.actor.y = self.posy
		self.actor.draw()

