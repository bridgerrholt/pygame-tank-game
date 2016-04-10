import pygame
from pygame.locals import *

import trig

class Bullet:
	def __init__(self, pos, direction, speed):
		# The starting position of the bullet (x, y).
		self.x, self.y = pos
		# The direction (in radians) that the bullet is traveling.
		self.direction = direction
		# The speed (pixels per second) that the bullet is traveling.
		self.speed = speed

	def update(self, frameRateManager):
		self.x, self.y = trig.disDir(self.x, self.y,
			self.speed*frameRateManager.deltaCoefficient, self.direction)

	def draw(self, surface):
		pygame.draw.circle(surface, Color(255, 255, 255), (int(round(self.x)), int(round(self.y))), 5)