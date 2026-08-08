import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	world = newWorld(start, zone_size)
	go = world["go"]

	grass_pos = []

	def init():
		global grass_pos
		grass_pos = zone_utils.snakePath(zone_size)

	def plantGrass():
		for [x, y] in grass_pos:
			go(x, y)
			zone_utils.tryHarvest()
			if get_ground_type() == Grounds.Soil:
				till()
			if get_entity_type() != Entities.Grass:
				plant(Entities.Grass)
			if zone_size < 3:
				zone_utils.water()

	def harvestGrass():
		for [x, y] in grass_pos:
			go(x, y)
			if can_harvest():
				harvest()
			else:
				action.pet()

	init()
	plantGrass()
	for _ in range((get_world_size() * get_world_size()) / (zone_size * zone_size) * 2):
		harvestGrass()

def entities():
	return [Entities.Grass]