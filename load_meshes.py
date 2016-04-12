from raw_mesh import *

def loadMeshes():
	returnDict = {}

	returnDict["tank_0"] = RawMesh([
		("body", [(8, 0), (40, 0), (48, 8), (48, 40), (40, 48), (8, 48), (0, 40), (0, 8)], True),
		("gun", [(0, 0), (45, 0), (45, 10), (0, 10)], (5, 5))
	])

	returnDict["enemy_0"] = RawMesh([
		("body", [(8, 0), (40, 0), (48, 8), (48, 40), (40, 48), (8, 48), (0, 40), (0, 8)], True)
	])

	return returnDict
