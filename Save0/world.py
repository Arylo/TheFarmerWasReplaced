import pos
import action

def newWorld(start: int = 0, world_size: int = get_world_size()):
	isTop, isBottom, isLeft, isRight, isTopLeft, isBottomLeft, isTopRight, isBottomRight, getRelativeX, getRelativeY = pos.newPos(start, world_size)

	def left():
		if isLeft():
			action.go(start + world_size - 1, get_pos_y())
		else:
			action.go(get_pos_x() - 1, get_pos_y())
	def right():
		if isRight():
			action.go(start, get_pos_y())
		else:
			action.go(get_pos_x() + 1, get_pos_y())
	def up():
		if isTop():
			action.go(get_pos_x(), start)
		else:
			action.go(get_pos_x(), get_pos_y() + 1)
	def down():
		if isBottom():
			action.go(get_pos_x(), start + world_size - 1)
		else:
			action.go(get_pos_x(), get_pos_y() - 1)
	def goNext():
		tap()
		if isTopRight():
			action.go(start, start)
			return False
		if isTop():
			action.go(get_pos_x() + 1, start)
		else:
			action.go(get_pos_x(), get_pos_y() + 1)
		return True

	def goBottom():
		action.go(get_pos_x(), start)
	def goTop():
		action.go(get_pos_x(), start + world_size - 1)
	def goLeft():
		action.go(start, get_pos_y())
	def goRight():
		action.go(start + world_size - 1, get_pos_y())
	def goTopLeft():
		action.go(start, start + world_size - 1)
	def goTopRight():
		action.go(start + world_size - 1, start + world_size - 1)
	def goBottomLeft():
		action.go(start, start)
	def goBottomRight():
		action.go(start + world_size - 1, start)
	def goZero():
		goBottomLeft()
	def goNeat(target_list):
		tmp_target_list = target_list
		for i in range(len(tmp_target_list)):
			tmp_target_list[i] = [tmp_target_list[i][0] + start, tmp_target_list[i][1] + start]
		(target_pos_x, target_pos_y) = action.goNeat(tmp_target_list)
		return (target_pos_x - start, target_pos_y - start)
	def go(x, y):
		action.go(start + x, start + y)

	return {
		"isTop": isTop,
		"isBottom": isBottom,
		"isLeft": isLeft,
		"isRight": isRight,
		"isTopLeft": isTopLeft,
		"isBottomLeft": isBottomLeft,
		"isTopRight": isTopRight,
		"isBottomRight": isBottomRight,
		"getRelativeX": getRelativeX,
		"getRelativeY": getRelativeY,

		"goNext": goNext,
		"goBottom": goBottom,
		"goTop": goTop,
		"goLeft": goLeft,
		"goRight": goRight,
		"goTopLeft": goTopLeft,
		"goTopRight": goTopRight,
		"goBottomLeft": goBottomLeft,
		"goBottomRight": goBottomRight,
		"goZero": goZero,

		"left": left,
		"right": right,
		"up": up,
		"down": down,
		"go": go,
		"goNeat": goNeat,
	}
