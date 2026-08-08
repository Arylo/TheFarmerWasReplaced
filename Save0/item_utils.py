import zone_wood
import zone_carrot
import zone_sunflower
import zone_pumpkin
import zone_grass
import zone_cactus

# 资源 -> 生产该资源的 zone
map = {
	Items.Hay: (zone_grass, 0, 2),
	Items.Carrot: (zone_carrot, 0, 5),
	Items.Power: (zone_sunflower, 0, get_world_size() / 2),
	Items.Wood: (zone_wood, 0, get_world_size()),
	Items.Pumpkin: (zone_pumpkin, 0, get_world_size()),
	Items.Cactus: (zone_cactus, 0, get_world_size()),
}

def _startItem(item):
	module, start, zone_size = map[item]
	for entity in module.entities():
		cost = get_cost(entity)
		for next_item in cost:
			count = cost[next_item]
			current_count = num_items(next_item)
			need_count = count * get_world_size() * get_world_size() * 1.2
			while current_count < need_count:
				_startItem(next_item)
				current_count = num_items(next_item)

	module.start(start, zone_size)

def startItem(item):
	if item != Items.Power:
		while True:
			current_num = num_items(Items.Power)
			random_num = random()
			needRun = (current_num <= 2000) or (current_num <= 3000 and random_num < 0.5) or (current_num <= 4000 and random_num < 0.25)
			quick_print("current_num:", current_num, "random_num:", random_num, "needRun:", needRun)
			if not needRun:
				break
			for _ in range(5):
				_startItem(Items.Power)
	_startItem(item)