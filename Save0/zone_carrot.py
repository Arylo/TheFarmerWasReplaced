import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	world = newWorld(start, zone_size)
	go = world["go"]

	carrot_pos = []

	def init():
		global carrot_pos
		carrot_pos = zone_utils.snakePath(zone_size)

	def plantCarrot():
		for [x, y] in carrot_pos:
			go(x, y)
			zone_utils.tryHarvest()
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Carrot:
				plant(Entities.Carrot)

	def harvestCarrot():
		for [x, y] in carrot_pos:
			go(x, y)
			while True:
				if not can_harvest():
					zone_utils.water()
					action.pet()
					continue
				harvest()
				break

	init()
	plantCarrot()
	harvestCarrot()

def entities():
	return [Entities.Carrot]