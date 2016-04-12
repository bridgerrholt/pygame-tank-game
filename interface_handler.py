import pygame
from pygame.locals import *

class InterfaceHandler:
	def __init__(self, objectHandler):
		self.objectHandler = objectHandler

		self.debugColor = Color(255, 0, 0)
		self.debugText = pygame.font.SysFont("arial", 16)

	def draw(self):
		
		self.drawText(self.debugText, "FPS: " + str(int(self.objectHandler.frameRateHandler.previousRate)), False, self.debugColor, (5, 5))

	def drawText(self, font, text, antialias, color, destination):
		self.objectHandler.mainSurface.blit(font.render(text, antialias, color), destination)