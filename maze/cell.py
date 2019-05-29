class Cell:
	UP=0
	DOWN=1
	LEFT=2
	RIGHT=3

	def __init__(self, position):
		self.position = position
		self.walls=[1,1,1,1]
		self.isEnd=-1
		self.visited = False

	def addWall(self, side):
		self.walls[side] = 1

	def removeWall(self, side):
		self.walls[side] = 0

	def setStart(self):
		self.isEnd = 0

	def setEnd(self):
		self.isEnd = 1

	def getX(self):
		return self.position[0]

	def getY(self):
		return self.position[1]

	def visit(self):
		self.visited = True

	def isVisit(self):
		return self.visited

	def draw(self, plt, x, y, h):
		dh = h/3
		if self.walls[Cell.UP]==1:
			plt.plot([x, x+h], [y+h, y+h], 'k-', lw=1)
		if self.walls[Cell.DOWN]==1:
			plt.plot([x, x+h], [y, y], 'k-', lw=1)

		if self.isEnd==0:
			plt.plot([x, x], [y, y + dh], 'k-', lw=1)
			plt.plot([x, x], [y+h-dh, y + h], 'k-', lw=1)
		elif self.walls[Cell.LEFT]==1:
			plt.plot([x, x], [y, y+h], 'k-', lw=1)

		if self.isEnd==1:
			plt.plot([x+h, x+h], [y, y + dh], 'k-', lw=1)
			plt.plot([x+h, x+h], [y+h-dh, y + h], 'k-', lw=1)
		elif self.walls[Cell.RIGHT]==1:
			plt.plot([x+h, x+h], [y, y+h], 'k-', lw=1)

