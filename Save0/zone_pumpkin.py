import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	DEFAULT_VALUE = -999
	map = zone_utils.initList(DEFAULT_VALUE, zone_size)
	world = newWorld(start, zone_size)
	go = world["go"]
	goNeat = world["goNeat"]
	left = world["left"]
	right = world["right"]
	isLeft = world["isLeft"]
	isRight = world["isRight"]
	getRelativeX = world["getRelativeX"]
	getRelativeY = world["getRelativeY"]

	pumpkin_pos = []

	def init():
		global pumpkin_pos
		pumpkin_pos = zone_utils.snakePath(zone_size)

	def isAllGood():
		sum = 0
		for i in range(zone_size):
			for j in range(zone_size):
				sum += map[i][j]
		return sum == zone_size * zone_size

	def findBads():
		bads = []
		for i in range(zone_size):
			for j in range(zone_size):
				if map[i][j] == DEFAULT_VALUE:
					bads.append([i, j])
		return bads

	def plantPumpkins():
		for [x, y] in pumpkin_pos:
			go(x, y)
			if get_entity_type() != Entities.Pumpkin:
				zone_utils.tryHarvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Pumpkin)
				if isRight():
					zone_utils.water()
			x, y = getRelativeX(), getRelativeY()
			if (not isLeft()) and map[x - 1][y] == DEFAULT_VALUE:
				left()
				if can_harvest():
					map[x - 1][y] = 1
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				right()
			if can_harvest():
				map[x][y] = 1

		while not isAllGood():
			ps = findBads()
			while len(ps) > 0:
				x, y = goNeat(ps)

				if get_entity_type() == Entities.Pumpkin:
					if can_harvest():
						map[x][y] = 1
					elif len(ps) == 1:
						action.pet()

				elif get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					zone_utils.water()

				ps.remove([x, y])

	def harvestPumpkin():
		harvest()

	init()
	plantPumpkins()
	harvestPumpkin()

def entities():
	return [Entities.Pumpkin]