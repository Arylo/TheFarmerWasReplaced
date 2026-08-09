import action
import pos
from world import newWorld

def water():
	while get_water() < 1:
		if num_items(Items.Water) == 0:
			return
		use_item(Items.Water)
		
def harvestAll():
	action.backZero()
	while True:
		if not can_harvest():
			action.pet()
			continue
		harvest()

		if pos.is_top_right():
			break
		action.next()

def tryHarvest(wait = False):
	if get_entity_type() == None:
		return
	if can_harvest():
		harvest()
	elif wait:
		water()
		action.pet()

def initList(val, world_size = get_world_size()):
	lst = []
	for i in range(world_size):
		lst.append([])
		for j in range(world_size):
			lst[i].insert(j, val)
	return lst

def snakePath(zone_size):
	pos = []
	for i in range(zone_size):
		for j in range(zone_size):
			if i % 2 == 0:
				pos.append([i, j])
			else:
				pos.append([i, zone_size - 1 - j])
	return pos

def isInPos(absX, absY, pos_paths, start, zone_size):
	paths = pos_paths
	for i in range(len(paths)):
		paths[i] = [paths[i][0] + start, paths[i][1] + start]
	return (absX >= start) and (absX < start + zone_size) and (absY >= start) and (absY < start + zone_size)

def comboPlant(pos_paths = [], start = 0, zone_size = get_world_size()):
	current_entity = get_entity_type()
	if current_entity != Entities.Grass and current_entity != Entities.Bush and current_entity != Entities.Tree and current_entity != Entities.Carrot:
		return

	entity, (cx, cy) = get_companion()
	if (isInPos(cx, cy, pos_paths, start, zone_size)):
		return False

	action.go(cx, cy)
	if get_entity_type() != entity:
		tryHarvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(entity)
	return True

def comboPlants(pos_paths, start, zone_size):
	for [x, y] in pos_paths:
		action.go(start + x, start +y)
		comboPlant(pos_paths, start, zone_size)