import curses
import random
import copy

"""curses.noecho()
curses.cbreak()"""

"""field = ["O"*40]*20

#test = "thisisatest"
field[10] = "O"*20 + "X" + "O"*19
x = 21
y = 10
"""
class field(object):
	def __init__(self, bushnum):
		self.bushnum = bushnum
		
	def gen(self):
		f = ["."*40]*20
		for i in range(self.bushnum):
			b = bush()
			f[b.y]="%sO%s" % (f[b.y][:b.x], f[b.y][b.x+1:])
		return f


class wanderer(object):
	def __init__(self, char):
		self.char = char
		self.x=20
		self.y=11

	def move(self):

		key = ""
		#stdscr = curses.initscr()
		#stdscr.border(0)
		f = field(3).gen()
		while key != "q":
			#stdscr.refresh()
			key = input()
			f2 = copy.deepcopy(f)
			if key == "w":
				self.y -=1
			elif key == "s":
				self.y +=1
			elif key == "a":
				self.x -=1
			elif key == "d":
				self.x +=1
			f2[self.y] = "%sX%s" % (f[self.y][:self.x], f[self.y][self.x+1:])
			for i in range(20):
				print(f2[i])
		#curses.endwin()


class bush(object):
	def __init__(self):
		self.x=random.randint(0,39)
		self.y=random.randint(0,19)


man = wanderer("X")
"""f2 = field(100).gen()
for i in range(20):
	print(f2[i])
"""
man.move()

"""
curses.nocbreak()
curses.echo()
curses.endwin()
"""

"""key = ""

while key != "q":
	key = input()
	if key == "w":
		y -=1
	elif key == "s":
		y +=1
	elif key == "a":
		x -=1
	elif key == "d":
		x +=1
	field = ["."*40]*20
	#distribute obstacles in the field

	field[y] = ("."*x) + "X" + ("."*(39-x))
	for i in range(20):
		print(field[i])"""

#print(random.randint(0,40))
#print(field)