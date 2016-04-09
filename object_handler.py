from player import *

class ObjectHandler:
	def __init__(self, eventHandler, frameRateHandler, mainSurface):
		self.eventHandler = eventHandler
		self.frameRateHandler = frameRateHandler
		self.mainSurface = mainSurface

		self.player = Player(self.mainSurface.get_size(), self.frameRateHandler)

	def update(self):
		self.player.update(self.eventHandler)

	def draw(self):
		self.player.draw(self.mainSurface)