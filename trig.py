import math

# Returns the direction (in radians) from one position to another.
def pointDir(x1, y1, x2, y2):
	return math.atan2(-(y2-y1), (x2-x1)) % (2*math.pi)

# Returns the distance (no units) between two positions.
def pointDis(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)
	
# Returns a position (x, y) calculated by moving a given position a
# given distance (no units) in a given direction (in radians).
def disDir(x, y, distance, direction):
	return (x + distance*math.cos(direction),
		y + distance*-math.sin(direction))

# Returns a position (x, y) calculated by moving a given position a
# given distance (no units) toward another position.
def moveToward(x1, y1, x2, y2, distance):
	direction = pointDir(x1, y1, x2, y2)
	return disDir(x1, y1, distance, direction)