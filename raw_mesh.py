import math
import copy

import trig

class RawMesh:
	class RawPolygon:
		# pointList: list of (x, y) tuples
		# origin: (isCentered[, x, y])
		def __init__(self, pointList, origin=(0, 0)):
			self.rawPointList = list(pointList)
			self.origin = ()
			self.pointRelations = []

			if origin == True:
				self.centerOrigin()
			else:
				self.originX = origin[0]
				self.originY = origin[1]
				self.calculateRelations()

		def centerOrigin(self):
			minX, minY = self.rawPointList[0]
			maxX, maxY = self.rawPointList[0]

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

		def calculateRelations(self):
			self.pointRelations = []

			for i in self.rawPointList:
				self.pointRelations.append(
					(trig.pointDir(self.originX, self.originY, i[0], i[1]),
					 trig.pointDis(self.originX, self.originY, i[0], i[1]))
				)

	# polyDictionary: [(name, pointList), ...]
	def __init__(self, polyDictionary):
		self.rawPolygons = []
		for i in polyDictionary:
			if len(i) == 2:
				self.rawPolygons.append((i[0], RawMesh.RawPolygon(i[1])))
			else:
				self.rawPolygons.append((i[0], RawMesh.RawPolygon(i[1], i[2])))


