from game_object import *

from player import *

class ObjectHandler:
	def __init__(self, eventHandler, frameRateHandler, mainSurface):
		self.eventHandler = eventHandler
		self.frameRateHandler = frameRateHandler
		self.mainSurface = mainSurface

		self.__objects = []
		self.__deadIndexes = []

		self.pushObject(Player)

	def getGameObject(self):
		if len(self.__deadIndexes) > 0:
			index = self.__deadindexes[-1]
		else:
			index = len(self.__objects)

		return GameObject(self, index)

	def update(self):
		for i in range(len(self.__objects)):
			if self.__objects[i].alive:
				self.__objects[i].update()

	def draw(self):
		for i in range(len(self.__objects)):
			if self.__objects[i].alive:
				self.__objects[i].draw()

	def pushObject(self, ObjectClass, arguments=()):
		if len(self.__deadIndexes) > 0:
			index = self.__deadIndexes[-1]
			self.__objects[index] = ObjectClass(GameObject(self, index), *arguments)
			self.__deadIndexes.pop(-1)
		else:
			index = len(self.__objects)
			self.__objects.append(ObjectClass(GameObject(self, index), *arguments))

	def getObject(self, index):
		return self.__objects[index]

	def killObject(self, index):
		self.__objects[index].alive = False
		self.__deadIndexes.append(index)
		print len(self.__objects), len(self.__deadIndexes)