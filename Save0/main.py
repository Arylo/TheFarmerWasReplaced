import item_utils

# 要完成的解锁（按依赖顺序）
list = [
	Unlocks.Trees,
	Unlocks.Grass,
	Unlocks.Carrots,
	Unlocks.Watering,
	Unlocks.Expand,
	Unlocks.Pumpkins,
	Unlocks.Cactus,
	Unlocks.Dinosaurs,
	Unlocks.The_Farmers_Remains,
	Unlocks.Polyculture,
]

for u in list:
	while True:
		cost = get_cost(u)
		if len(cost) == 0:
			break
		for item in cost:
			while True:
				needCount = cost[item]
				currentCount = num_items(item)
				if needCount * 1.2 <= currentCount:
					break
				quick_print(u, item, needCount, currentCount)
				item_utils.startItem(item)
		unlock(u)

list = [
	Items.Cactus,
	Items.Pumpkin,
	Items.Wood,
	Items.Carrot,
	Items.Hay,
]

while True:
	for item in list:
		for _ in range(3):
			item_utils.startItem(item)