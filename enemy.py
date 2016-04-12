
import pygame
from pygame.locals import *

import trig
from polygon_object import *
from game_object import *
from combat_object import *
from mesh import *

class Enemy(GameObject, CombatObject):
	def __init__(self, gameObject, pos):
		super(Enemy, self).copy(gameObject)
		super(GameObject, self).__init__({
			"hpMax": 100,
			"attackPower": 10
		})

		self.color = Color(255, 0, 0)

		self.speedMax = 300.0
		self.speedInc = 200.0
		self.speedDec = 200.0

		self.speed = 0.0
		self.direction = 0.0
		self.directionChange = math.pi*.75

		self.speedX = 0.0
		self.speedY = 0.0

		self.mesh = Mesh(self.objectHandler.meshDict["enemy_0"],
			pos)

	def update(self):
		pass

	def draw(self):
		pygame.draw.polygon(self.objectHandler.mainSurface, self.color, self.mesh.getPoints("body"))