from raw_mesh import *

class Mesh:
	class Polygon:
		def __init__(self, rawPolygonRef, position=(0, 0)):
			self.polyRef = rawPolygonRef
			self.posX, self.posY = position
			self.rotation = 0

			self.pointList = list(rawPolygonRef.rawPointList)

		def rotate(self, amount):
			self.rotation = (self.rotation + amount) % (2*math.pi)

		def setRotation(self, newRotation):
			self.rotation = newRotation % (2*math.pi)

		def doRotation(self, extraDisplacement=(0, 0), extraRotation=0):
			for i in range(len(self.pointList)):
				self.pointList[i] = trig.disDir(
					self.posX+extraDisplacement[0],
					self.posY+extraDisplacement[1],
					self.polyRef.pointRelations[i][1],
					self.polyRef.pointRelations[i][0] + self.rotation + extraRotation)
			return self.pointList

		def move(self, x, y):
			self.posX += x
			self.posY += y
			for i in range(len(self.pointList)):
				self.pointList[i] = (self.pointList[i][0]+x, self.pointList[i][1]+y)

		def setPosition(self, x, y):
			self.move(x - self.posX, y - self.posY)


	def __init__(self, rawMeshRef, position, rotation=0):
		self.meshRef = rawMeshRef
		self.posX, self.posY = position
		self.rotation = rotation

		self.polyList = []
		for i in self.meshRef.rawPolygons:
			self.polyList.append((i[0], Mesh.Polygon(i[1])))

	def getPoly(self, name):
		for i in self.polyList:
			if i[0] == name:
				return i[1]

	def getPoints(self, name):
		for i in self.polyList:
			if i[0] == name:
				return i[1].doRotation((self.posX, self.posY), self.rotation)

	def rotate(self, amount):
		self.rotation = (self.rotation + amount) % (2*math.pi)

		self.doRotation()

	def setRotation(self, newRotation):
		self.rotation = newRotation % (2*math.pi)

		self.doRotation()

	def doRotation(self):
		for key, value in self.pointDict.iteritems():
			for i in range(len(self.pointDict[key])):
				self.self.pointDict[key][i] = trig.disDir(
					self.posX,
					self.posY,
					i[1], i[0]+self.rotation)

	def move(self, x, y):
		self.posX += x
		self.posY += y

	# Calls move with values to reach the given position.
	def setPosition(self, x, y):
		self.move(x - self.posX, y - self.posY)