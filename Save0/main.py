import item_utils

# 要完成的解锁（按依赖顺序）
list = [
	Unlocks.Trees,
	Unlocks.Grass,
	Unlocks.Carrots,
	Unlocks.Watering,
	Unlocks.Pumpkins,
	Unlocks.Expand,
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
			needCount = cost[item]
			start_time = get_time()
			start_count = num_items(item)
			realNeedCount = needCount * 1.2
			while True:
				current_count = num_items(item)
				if current_count >= realNeedCount:
					break

				quick_print(u, item, needCount, current_count, "...")
				item_utils.startItem(item)
				end_count = num_items(item)
				running_time = get_time() - start_time
				prod_count = end_count - start_count
				diff_count = end_count - current_count
				info = "OK"
				if diff_count == 0:
					info = "ERR"
				elif end_count < realNeedCount:
					quick_print(realNeedCount, end_count, current_count, prod_count, running_time)
					need_second = (realNeedCount - end_count) / (prod_count / running_time)
					need_minute = 0
					need_hour = 0
					if (need_second > 60):
						need_minute = need_second / 60
					if (need_minute > 60):
						need_hour = need_minute / 60

					need_second = str(need_second) + "s"
					if (need_minute > 1):
						need_minute = str(need_minute) + "m"
					else:
						need_minute = ""
					if (need_hour > 1):
						need_hour = str(need_hour) + "h"
					else:
						need_hour = ""

					info = "ETA " + need_second + " " + need_minute + " " + need_hour
				quick_print(u, item, needCount, current_count, "...", info)
				quick_print("========================")
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