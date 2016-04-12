import math
import time

import pygame
from pygame.locals import *

import trig
from polygon_object import *
from game_object import *
from combat_object import *
from mesh import *

from bullet import *

class Player(GameObject, CombatObject):
	def __init__(self, gameObject):
		super(Player, self).copy(gameObject)
		super(GameObject, self).__init__({
			"hpMax": 100,
			"attackPower": 10
		})

		self.color = Color(255, 255, 255)

		self.speedMax = 300.0
		self.speedInc = 200.0
		self.speedDec = 200.0

		self.speed = 0.0
		self.direction = 0.0
		self.directionChange = math.pi*.75

		self.speedX = 0.0
		self.speedY = 0.0

		self.mesh = Mesh(self.objectHandler.meshDict["tank_0"],
			(self.objectHandler.mainSurface.get_width()/2.0,
			 self.objectHandler.mainSurface.get_height()/2.0))

		self.poly = PolygonObject(
			[(8, 0), (40, 0), (48, 8), (48, 40), (40, 48), (8, 48), (0, 40), (0, 8)])
		self.poly.centerOrigin()
		self.poly.setPosition(self.objectHandler.mainSurface.get_width()/2.0, self.objectHandler.mainSurface.get_height()/2.0)

		self.gunPoly = PolygonObject(
			[(0, 0), (45, 0), (45, 10), (0, 10)],
			(5, 5))
		self.gunPoly.setPosition(self.poly.posX, self.poly.posY)

	
		self.reloadTime = 0.5
		self.nextReady = time.time()


	def update(self):
		"""self.speedX, xChange = self.speedConditional(self.speedX,
			eventHandler.keys.down[K_d], eventHandler.keys.down[K_a])

		self.speedY, yChange = self.speedConditional(self.speedY,
			eventHandler.keys.down[K_s], eventHandler.keys.down[K_w])

		if xChange or yChange:
			self.poly.setRotation(trig.pointDir(0, 0, self.speedX, self.speedY))"""

		xDesire = 0
		yDesire = 0
		if self.objectHandler.eventHandler.keys.down[K_d]:
			xDesire += 100
		elif self.objectHandler.eventHandler.keys.down[K_a]:
			xDesire -= 100
		if self.objectHandler.eventHandler.keys.down[K_s]:
			yDesire += 100
		elif self.objectHandler.eventHandler.keys.down[K_w]:
			yDesire -= 100

		if self.objectHandler.eventHandler.keys.down[K_SPACE]:
			self.speed += self.speedInc*self.objectHandler.frameRateHandler.deltaCoefficient - self.speed*0.005
			if self.speed > self.speedMax:
				self.speed = self.speedMax
		elif self.objectHandler.eventHandler.keys.down[K_LSHIFT]:
			if self.speed > 0.0:
				self.speed -= self.speedDec*self.objectHandler.frameRateHandler.deltaCoefficient - self.speed*0.005
				if self.speed < 0.0:
					self.speed = 0.0


		"""if xDesire != 0 or yDesire != 0:
			desiredDir = trig.pointDir(0, 0, xDesire, yDesire)

			changeDir = self.directionChange*self.objectHandler.frameRateHandler.deltaCoefficient
			#print changeDir

			if abs(desiredDir-self.direction) <= changeDir or \
				abs(desiredDir-self.direction+math.pi*2) <= changeDir:
				self.direction = desiredDir;

			elif ((self.direction-desiredDir + math.pi*2) % (math.pi*2)) > math.pi:
				self.direction += changeDir;
			else:
				self.direction -= changeDir;

			self.speed += self.speedInc*self.objectHandler.frameRateHandler.deltaCoefficient - self.speed*0.005
			if self.speed > self.speedMax:
				self.speed = self.speedMax

		elif self.speed > 0.0:
			self.speed -= self.speedDec*self.objectHandler.frameRateHandler.deltaCoefficient - self.speed*0.005
			if self.speed < 0.0:
				self.speed = 0.0"""

		changeDir = self.directionChange*self.objectHandler.frameRateHandler.deltaCoefficient
		if self.objectHandler.eventHandler.keys.down[K_a]:
			self.direction += changeDir
		elif self.objectHandler.eventHandler.keys.down[K_d]:
			self.direction -= changeDir


		while self.direction < 0:
			self.direction += math.pi*2
		while self.direction >= math.pi*2:
			self.direction -= math.pi*2

		moveX, moveY = trig.disDir(0, 0, self.speed*self.objectHandler.frameRateHandler.deltaCoefficient, self.direction)
		# print moveX, moveY

		self.poly.setRotation(self.direction)
		self.poly.move(moveX, moveY)
		self.mesh.getPoly("body").setRotation(self.direction)
		self.mesh.move(moveX, moveY)
		self.gunPoly.move(moveX, moveY)


		"""self.poly.move(self.speedX*self.frameRateHandler.deltaCoefficient,
			self.speedY*self.frameRateHandler.deltaCoefficient)
		self.gunPoly.setPosition(self.poly.posX, self.poly.posY)"""

		"""self.gunPoly.setRotation(trig.pointDir(
			self.gunPoly.posX, self.gunPoly.posY,
			self.objectHandler.eventHandler.mouse.x, self.objectHandler.eventHandler.mouse.y))"""

		self.mesh.getPoly("gun").setRotation(trig.pointDir(
			self.gunPoly.posX, self.gunPoly.posY,
			self.objectHandler.eventHandler.mouse.x, self.objectHandler.eventHandler.mouse.y))

		if self.objectHandler.eventHandler.mouse.left.down: # or True:
			self.fireBullet()


	def draw(self):
		#pygame.draw.polygon(self.objectHandler.mainSurface, self.color, self.poly.pointList)
		#pygame.draw.polygon(self.objectHandler.mainSurface, self.color, self.gunPoly.pointList)
		pygame.draw.polygon(self.objectHandler.mainSurface, self.color, self.mesh.getPoints("body"))
		pygame.draw.polygon(self.objectHandler.mainSurface, self.color, self.mesh.getPoints("gun"))


	# Brings the given speed away from 0.
	def increaseSpeed(self, speed, value):
		speed += value
		if speed < -self.speedMax:
			speed = -self.speedMax
		elif speed > self.speedMax:
			speed = self.speedMax
		return speed

	# Brings the given speed to 0.
	def decreaseSpeed(self, speed, value):
		if speed < 0:
			speed += value - speed*0.005
			if speed > 0:
				speed = 0
		elif speed > 0:
			speed -= value - speed*0.005
			if speed < 0:
				speed = 0
		return speed

	# Given 2 bools, increases or decreases the given speed.
	def speedConditional(self, speed, toAdd, toSubtract):
		if toAdd:
			speed += self.speedInc*self.objectHandler.frameRateHandler.deltaCoefficient - speed*0.005
			if speed > self.speedMax:
				speed = self.speedMax
			return (speed, True)
		elif toSubtract:
			speed -= self.speedInc*self.objectHandler.frameRateHandler.deltaCoefficient - speed*0.005
			if speed < -self.speedMax:
				speed = -self.speedMax
			return (speed, True)
		else:
			return (self.decreaseSpeed(speed, self.speedDec*self.objectHandler.frameRateHandler.deltaCoefficient), False)

	def fireBullet(self):
		currentTime = time.time()
		if currentTime >= self.nextReady:
			gunRotation = self.mesh.getPoly("gun").rotation
			self.objectHandler.pushObject(Bullet, (self.index, trig.disDir(self.poly.posX, self.poly.posY, 40, gunRotation), gunRotation, 1000))
			self.nextReady = currentTime + self.reloadTime
