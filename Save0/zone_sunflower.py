import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	world = newWorld(start, zone_size)
	isRight = world["isRight"]
	go = world["go"]

	sunflower_pos = []
	sunflower_count = zone_utils.initList(-1, zone_size)

	def init():
		global sunflower_pos
		sunflower_pos = zone_utils.snakePath(zone_size)

	def plantSunflower():
		for [x, y] in sunflower_pos:
			go(x, y)
			zone_utils.tryHarvest()
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Sunflower:
				plant(Entities.Sunflower)
			count = measure()
			sunflower_count[x][y] = count
			if count > 13 and isRight():
				zone_utils.water()

	def findMax():
		pos = []
		count_list = []
		for [x, y] in sunflower_pos:
			count = sunflower_count[x][y]
			if count == -1:
				continue
			count_list.append(count)
		max_count, min_count = max(count_list), min(count_list)
		for c in range(max_count, min_count - 1, -1):
			for [x, y] in sunflower_pos:
				count = sunflower_count[x][y]
				if count == c:
					pos.append([x, y])
		return pos

	def harvestSunflower():
		pos = findMax()
		for [x, y] in pos:
			go(x, y)
			while True:
				if not can_harvest():
					zone_utils.water()
					action.pet()
					continue
				harvest()
				sunflower_count[x][y] = -1
				break

	init()
	plantSunflower()
	harvestSunflower()

def entities():
	return [Entities.Sunflower]