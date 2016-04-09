import math
import trig

class PolygonObject:
	def __init__(self, pointList, origin=(0, 0), position=(0, 0)):
		self.rawPointList = list(pointList)
		self.pointList = list(pointList)
		self.pointRelations = []

		self.originX, self.originY = origin
		self.posX, self.posY = position
		self.rotation = 0

		self.calculateRelations()

	def centerOrigin(self):
		minX = self.rawPointList[0][0]
		maxX = self.rawPointList[0][0]
		minY = self.rawPointList[0][1]
		maxY = self.rawPointList[0][1]

		for i in self.rawPointList:
			if i[0] < minX:
				minX = i[0]
			elif i[0] > maxX:
				maxX = i[0]
			if i[1] < minY:
				minY = i[1]
			elif i[1] > maxY:
				maxY = i[1]

		self.originX = minX + (maxX-minX)/2.0
		self.originY = minY + (maxY-minY)/2.0

		self.calculateRelations()
		self.doRotation()

	def rotate(self, amount):
		self.rotation = (self.rotation + amount) % (2*math.pi)

		self.doRotation()

	def setRotation(self, newRotation):
		self.rotation = newRotation % (2*math.pi)

		self.doRotation()

	def doRotation(self):
		self.pointList = []

		for i in self.pointRelations:
			self.pointList.append(trig.disDir(
				self.posX, #-self.originX,
				self.posY, #-self.originY,
				i[1], i[0]+self.rotation))

	def calculateRelations(self):
		self.pointRelations = []

		for i in self.rawPointList:
			self.pointRelations.append(
				(trig.pointDir(self.originX, self.originY, i[0], i[1]),
				 trig.pointDis(self.originX, self.originY, i[0], i[1]))
			)

	def move(self, x, y):
		self.posX += x
		self.posY += y
		for i in range(len(self.pointList)):
			self.pointList[i] = (self.pointList[i][0]+x, self.pointList[i][1]+y)

	# Calls move with values to reach the given position.
	def setPosition(self, x, y):
		self.move(x - self.posX, y - self.posY)