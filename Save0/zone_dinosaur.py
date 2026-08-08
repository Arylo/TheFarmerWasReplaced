from world import newWorld

def start(start = 0, zone_size = get_world_size()):
	world = newWorld(start, zone_size)
	go = world["go"]

	def init():
		clear()
		change_hat(Hats.Dinosaur_Hat)

	def loop():
		for _ in range(get_world_size() / 2):
			pos = measure()
			if pos != None:
				x, y = pos
				quick_print("loop", x, y)
				go(x, y, False)
			else:
				return

	def end():
		change_hat(Hats.Carrot_Hat)

	init()
	loop()
	end()

def entities():
	return []