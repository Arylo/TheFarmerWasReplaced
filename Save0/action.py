import pos

def next():
	tap()
	if pos.is_top():
		move(East)
	move(North)

def goNeat(target_list, can_cross = True):
	len_list = []
	tap()
	current_pos_x = get_pos_x()
	current_pos_y = get_pos_y()

	def toN(from_num, to_num):
		if from_num <= to_num:
			return to_num - from_num
		if (not can_cross):
			return get_world_size()
		return to_num + get_world_size() - from_num
	def toS(from_num, to_num):
		if from_num >= to_num:
			return from_num - to_num
		if (not can_cross):
			return get_world_size()
		return from_num - (to_num - get_world_size())
	def toE(from_num, to_num):
		return toN(from_num, to_num)
	def toW(from_num, to_num):
		return toS(from_num, to_num)

	if len(target_list) == 0:
		return (current_pos_x, current_pos_y)
	for [target_pos_x, target_pos_y] in target_list:
		if (target_pos_x < 0) or (target_pos_x >= get_world_size()):
			continue
		if (target_pos_y < 0) or (target_pos_y >= get_world_size()):
			continue

		len_pos_x = (toE(current_pos_x, target_pos_x), toW(current_pos_x, target_pos_x))
		len_pos_y = (toN(current_pos_y, target_pos_y), toS(current_pos_y, target_pos_y))

		is_E = len_pos_x[0] <= len_pos_x[1]
		is_N = len_pos_y[0] <= len_pos_y[1]

		min_len_x = min(len_pos_x)
		min_len_y = min(len_pos_y)

		len_list.append((target_pos_x, target_pos_y, min_len_x + min_len_y, is_E, is_N))

	if len(len_list) == 0:
		return (current_pos_x, current_pos_y)

	best_path = (current_pos_x, current_pos_y, get_world_size() * get_world_size(), True, True)
	for x, y, l, is_E, is_N in len_list:
		if l < best_path[2]:
			best_path = (x, y, l, is_E, is_N)

	target_pos_x, target_pos_y, l, is_E, is_N = best_path
	if l == 0:
		return (target_pos_x, target_pos_y)
	previous_pos_x, previous_pos_y = -1, -1
	while True:
		current_pos_x, current_pos_y = get_pos_x(), get_pos_y()
		if (current_pos_x == previous_pos_x) and (current_pos_y == previous_pos_y):
			return (current_pos_x, current_pos_y)
		previous_pos_x, previous_pos_y = current_pos_x, current_pos_y
		if (current_pos_x == target_pos_x) and (current_pos_y == target_pos_y):
			return (target_pos_x, target_pos_y)
	
		if current_pos_x != target_pos_x:
			if (is_E):
				move(East)
			else:
				move(West)
		if current_pos_y != target_pos_y:
			if (is_N):
				move(North)
			else:
				move(South)

def go(target_pos_x, target_pos_y, can_cross = True):
	goNeat([[target_pos_x, target_pos_y]], can_cross)

def backBottom():
	go(get_pos_x(), 0)
	tap()

def backTop():
	go(get_pos_x(), get_world_size() - 1)
	tap()

def backLeft():
	go(0, get_pos_y())
	tap()

def backRight():
	go(get_world_size() - 1, get_pos_y())
	tap()

def backZero():
	backBottom()
	backLeft()
	
def pet():
	if random() > 0.5:
		do_a_flip()
	else:
		pet_the_piggy()