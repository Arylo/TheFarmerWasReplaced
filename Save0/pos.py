def is_top(world_size = get_world_size()):
	tap()
	return get_pos_y() == world_size - 1

def is_bottom(world_size = get_world_size()):
	tap()
	return get_pos_y() == 0

def is_left(world_size = get_world_size()):
	tap()
	return get_pos_x() == 0

def is_right(world_size = get_world_size()):
	tap()
	return get_pos_x() == world_size - 1

def is_top_left(world_size = get_world_size()):
	return is_top(world_size) and is_left(world_size)

def is_bottom_left(world_size = get_world_size()):
	return is_bottom(world_size) and is_left(world_size)

def is_top_right(world_size = get_world_size()):
	return is_top(world_size) and is_right(world_size)

def is_bottom_right(world_size = get_world_size()):
	return is_bottom(world_size) and is_right(world_size)

def is_up_side(world_size = get_world_size()):
	return get_pos_y() >= world_size / 2

def is_down_side(world_size = get_world_size()):
	return get_pos_y() < world_size / 2

def is_right_side(world_size = get_world_size()):
	return get_pos_x() >= world_size / 2

def is_left_side(world_size = get_world_size()):
	return get_pos_x() < world_size / 2

def newPos(start =  0, world_size = get_world_size()):
	top, bottom, left, right = start + world_size - 1, start, start, start + world_size - 1

	def isTop():
		tap()
		return get_pos_y() == top
	def isBottom():
		tap()
		return get_pos_y() == bottom
	def isLeft():
		tap()
		return get_pos_x() == left
	def isRight():
		tap()
		return get_pos_x() == right

	def isTopLeft():
		return isTop() and isLeft()
	def isBottomLeft():
		return isBottom() and isLeft()
	def isTopRight():
		return isTop() and isRight()
	def isBottomRight():
		return isBottom() and isRight()
	def getRelativeX():
		return get_pos_x() - start
	def getRelativeY():
		return get_pos_y() - start

	return isTop, isBottom, isLeft, isRight, isTopLeft, isBottomLeft, isTopRight, isBottomRight, getRelativeX, getRelativeY

isTop, isBottom, isLeft, isRight, isTopLeft, isBottomLeft, isTopRight, isBottomRight, getCurrentX, getPosY = newPos()