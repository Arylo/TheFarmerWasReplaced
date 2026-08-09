import zone_utils
import action
from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	BELONG_BUSH_SIZE = 5

	world = newWorld(start, zone_size)
	go = world["go"]

	tree_pos = []
	bush_pos = []

	def init():
		all_pos = zone_utils.snakePath(zone_size)

		global tree_pos
		global bush_pos
		for [x, y] in all_pos:
			if (x + y) % 2 == 0:
				tree_pos.append([x, y])
			else:
				bush_pos.append([x, y])

	def plantTree():
		for [x, y] in tree_pos:
			go(x, y)
			zone_utils.tryHarvest()
			plant(Entities.Tree)
			if zone_size < BELONG_BUSH_SIZE:
				zone_utils.water()
			else:
				zone_utils.comboPlant(tree_pos, start, zone_size)

	def plantBush():
		if zone_size < BELONG_BUSH_SIZE:
			return
		for [x, y] in bush_pos:
			go(x, y)
			zone_utils.tryHarvest()
			plant(Entities.Bush)

	def harvestWood():
		for [x, y] in bush_pos:
			go(x, y)
			harvest()
		for [x, y] in tree_pos:
			go(x, y)
			harvest()

	init()
	for _ in range(2):
		plantTree()
		plantBush()
		harvestWood()

def entities():
	return [Entities.Tree, Entities.Bush]