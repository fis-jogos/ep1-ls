class environment:

	gravity = 10
	entities=[]

	def __init__(self, *entities, gravity):
		self.entities = list(entities)
		self.gravity = 0

	def draw(self):

		for entity in self.entities:
			entity.draw()


	def add(self, entity):
		self.entities.append(entity)




