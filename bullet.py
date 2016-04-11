import pygame
from pygame.locals import *

import trig
from game_object import *

class Bullet(GameObject):
	def __init__(self, gameObject, parent, pos, direction, speed):
		super(Bullet, self).copy(gameObject)

		self.parent = parent
		# The starting position of the bullet (x, y).
		self.x, self.y = pos
		# The direction (in radians) that the bullet is traveling.
		self.direction = direction
		# The speed (pixels per second) that the bullet is traveling.
		self.speed = speed

	def update(self):
		self.x, self.y = trig.disDir(self.x, self.y,
			self.speed*self.objectHandler.frameRateHandler.deltaCoefficient, self.direction)
		margin = 200
		if self.x < -margin or self.x > self.objectHandler.mainSurface.get_width()+margin or \
			self.y < -margin or self.y > self.objectHandler.mainSurface.get_height()+margin:
			self.objectHandler.killObject(self.index)

	def draw(self):
		pygame.draw.circle(self.objectHandler.mainSurface, Color(255, 255, 255), (int(round(self.x)), int(round(self.y))), 5)