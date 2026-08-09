import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	world = newWorld(start, zone_size)
	go = world["go"]

	grass_pos = zone_utils.snakePath(zone_size)

	def init():
		pass

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
			zone_utils.tryHarvest()

	init()
	for _ in range((get_world_size() * get_world_size()) / (zone_size * zone_size) * 2):
		plantGrass()
		zone_utils.comboPlant(grass_pos, start, zone_size)
		harvestGrass()

def entities():
	return [Entities.Grass]