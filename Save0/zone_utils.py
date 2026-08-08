import action
import pos

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

def tryHarvest():
	if can_harvest():
		harvest()

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