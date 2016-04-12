from game_object import *

from player import *
from enemy import *

class ObjectHandler:
	def __init__(self, eventHandler, frameRateHandler, mainSurface, meshDict):
		self.eventHandler = eventHandler
		self.frameRateHandler = frameRateHandler
		self.mainSurface = mainSurface
		self.meshDict = meshDict

		# Private list of all the objects currently in memory.
		self.__objects = []
		# Private list indicating locations where a new object can
		# safely be placed.
		self.__deadIndexes = []

		self.pushObject(Player)
		self.pushObject(Enemy, [(5, 5)])

	# Updates all the alive objects.
	def update(self):
		for i in range(len(self.__objects)):
			if self.__objects[i].alive:
				self.__objects[i].update()

	# Draws all the alive objects.
	def draw(self):
		for i in range(len(self.__objects)):
			if self.__objects[i].alive:
				self.__objects[i].draw()

	# Adds an object, given the class name and
	# additional constructor arguments (in the form of a tuple).
	def pushObject(self, ObjectClass, arguments=()):
		# If there are indicated locations, use one and remove it.
		arguments = tuple(arguments)
		if len(self.__deadIndexes) > 0:
			index = self.__deadIndexes[-1]
			self.__objects[index] = \
				ObjectClass(GameObject(self, index), *arguments)
			self.__deadIndexes.pop(-1)

		# Otherwise, push to the list.
		else:
			index = len(self.__objects)
			self.__objects.append(
				ObjectClass(GameObject(self, index), *arguments))

	# Returns an object from the object list based on an index.
	def getObject(self, index):
		return self.__objects[index]

	# Practically removes an object from physical existence.
	def killObject(self, index):
		# Set it to dead so it won't update or draw.
		self.__objects[index].alive = False
		# Mark its index as writable.
		self.__deadIndexes.append(index)

		print len(self.__objects), len(self.__deadIndexes)