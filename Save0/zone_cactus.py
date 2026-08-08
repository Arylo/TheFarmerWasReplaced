import zone_utils
from world import newWorld

DEFAULT_VALUE = -9999

def start(start = 0, zone_size = get_world_size()):
	map = zone_utils.initList(DEFAULT_VALUE, zone_size)
	cactus_pos = zone_utils.snakePath(zone_size)
	world = newWorld(start, zone_size)
	go = world["go"]
	isTop = world["isTop"]
	isBottom = world["isBottom"]
	isLeft = world["isLeft"]
	isRight = world["isRight"]
	goZero = world["goZero"]


	def init():
		goZero()

	def plantCactus():
		for [x, y] in cactus_pos:

			go(x, y)

			if get_ground_type() != Grounds.Soil:
				till()

			if get_entity_type() != Entities.Cactus:
				plant(Entities.Cactus)

			map[x][y] = measure()
			if (not isTop()) and map[x][y + 1] == DEFAULT_VALUE:
				val = measure(North)
				if val != None:
					map[x][y + 1] = val
			if (not isRight()) and map[x + 1][y] == DEFAULT_VALUE:
				val = measure(East)
				if val != None:
					map[x + 1][y] = val
			if (not isBottom()) and map[x][y - 1] == DEFAULT_VALUE:
				val = measure(South)
				if val != None:
					map[x][y - 1] = val
			if (not isLeft()) and map[x - 1][y] == DEFAULT_VALUE:
				val = measure(West)
				if val != None:
					map[x - 1][y] = val

	def swapCactus(x, y, d):
		go(x, y)
		swap(d)
		if d == North:
			map[x][y], map[x][y + 1] = map[x][y + 1], map[x][y]
		elif d == South:
			map[x][y], map[x][y - 1] = map[x][y - 1], map[x][y]
		elif d == East:
			map[x][y], map[x + 1][y] = map[x + 1][y], map[x][y]
		elif d == West:
			map[x][y], map[x - 1][y] = map[x - 1][y], map[x][y]

	def findBad():
		x, y, d = -1, -1, None
		size = len(map)
		for i in range(size):
			for j in range(size):
				current = map[i][j]
				if (i < size - 1):
					east = map[i + 1][j]
					if current > east:
						return i, j, East
				if (j < size - 1):
					north = map[i][j + 1]
					if current > north:
						return i, j, North
		return x, y, d

	def sortRows(start_pos = [0, 0], size = zone_size):
		for row in range(size):
			for line in range(1, size):
				x = row + start_pos[0]
				y = line + start_pos[1]
				while y != 0:
					current = map[x][y]
					south = map[x][y - 1]
					if current < south:
						swapCactus(x, y, South)
						y -= 1
						continue
					break

	def sortCols(start_pos = [0, 0], size = zone_size):
		for col in range(size):
			for line in range(1, size):
				x = line + start_pos[0]
				y = col + start_pos[1]
				while x != 0:
					current = map[x][y]
					west = map[x - 1][y]
					if current < west:
						swapCactus(x, y, West)
						x -= 1
						continue
					break

	def sortCactus():
		sortRows()
		sortCols()
		while True:
			x, y, d = findBad()
			if x == -1:
				break
			swapCactus(x, y, d)

	def harvestCactus():
		harvest()

	init()
	plantCactus()
	sortCactus()
	harvestCactus()

def entities():
	return [Entities.Cactus]
