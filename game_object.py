import copy

class GameObject(object):
	def __init__(self, objectHandler, index, alive=True):
		self.objectHandler = objectHandler
		self.index = index
		self.alive = alive

	def copy(self, gameObject):
		# self = copy.copy(gameObject)
		self.objectHandler = gameObject.objectHandler
		self.index = gameObject.index
		self.alive = gameObject.alive