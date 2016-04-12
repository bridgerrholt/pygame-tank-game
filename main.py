import sys
import time

import pygame
from pygame.locals import *

from initialize import *
from event_handler import EventHandler
from frame_rate_handler import *
from object_handler import *
from load_meshes import *

from polygon_object import *
from raw_mesh import *
from mesh import *

def main():
	initialize()
	eventHandler = EventHandler()
	frameRateHandler = FrameRateHandler(60)
	meshDict = loadMeshes()

	backColor = Color(0, 0, 0)
	mainSurface = pygame.display.set_mode((1280, 720))

	objectHandler = ObjectHandler(eventHandler, frameRateHandler, mainSurface, meshDict)

	tankMesh = RawMesh([
		("body", [(8, 0), (40, 0), (48, 8), (48, 40), (40, 48), (8, 48), (0, 40), (0, 8)]),
		("gun", [(0, 0), (45, 0), (45, 10), (0, 10)], (5, 5))
	])

	playerMesh = Mesh(tankMesh, (0, 0))



	while True:
		frameRateHandler.updateStart()
		eventHandler.update()

		if eventHandler.quit or eventHandler.keys.release[K_ESCAPE]:
			break

		objectHandler.update()

		mainSurface.fill(backColor)
		objectHandler.draw()

		pygame.display.flip()

		frameRateHandler.updateEnd()


if __name__ == "__main__":
	main()