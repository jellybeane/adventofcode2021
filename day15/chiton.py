from queue import PriorityQueue

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

risk = []

for line in puzzinput:
	nums = list(map(int, (c for c in line.strip())))
	risk.append(nums)

maxrow = len(risk)
maxcol = len(risk[0])

# Part 1: the total risk of the lowest-risk path
# from top left(0,0) to bottom right (maxrow, maxcol)

# Part 2: The entire cave is actually five times larger in both dimensions; 
# the area you originally scanned is just one tile in a 5x5 tile area that forms the full map.
# Your original map tile repeats to the right and downward; 
# each time the tile repeats to the right or downward, 
# all of its risk levels are 1 higher than the tile immediately up or left of it. 
# Risk levels above 9 wrap back around to 1.
bigger = [[0]*5*maxcol for i in range(5*maxrow)]
for i, row in enumerate(risk):
		for j, val in enumerate(row):
			bigger[i][j] = val

for down in range(0, 5):
	for right in range(0, 5):
		if down == 0 and right == 0:
			continue

		if down == 0:
			prevdown = 0
			prevright = right - 1
		elif right == 0:
			prevdown = down - 1
			prevright = 0
		else:
			prevdown = down
			prevright = right - 1

		for row in range(0, maxrow):
			for col in range(0, maxcol):
				newval = bigger[row + maxrow*prevdown][col + maxcol*prevright] + 1
				if newval > 9:
					newval = 1

				bigger[row + maxrow*down][col + maxcol*right] = newval

# helpers

# 4 neighbors: cannot move diagonally
def getneighbors(pos, maxrow, maxcol):
	row, col = pos
	neighbors = []
	if row > 0:
		neighbors.append((row-1,col))
	if col > 0:
		neighbors.append((row, col-1))
	if row < maxrow-1:
		neighbors.append((row+1, col))
	if col < maxcol-1:
		neighbors.append((row, col+1))
	return neighbors

# estimated cost to the end
def heuristic(pos):
	row, col = pos
	return 5 * (maxrow - row + maxcol - col)

# A*
def astar(risk):
	frontier = PriorityQueue()
	frontier.put((0,0), 0)
	came_from = {}
	came_from[(0,0)] = None
	cost_so_far = {}
	cost_so_far[(0,0)] = 0

	maxrow = len(risk)
	maxcol = len(risk[0])

	while not frontier.empty():
		current = frontier.get()
		row, col = current

		# have we gotten to the end?
		if row==maxrow-1 and col==maxcol-1:
			break

		for neighbor in getneighbors(current, maxrow, maxcol):
			nrow,ncol = neighbor
			newcost = cost_so_far[current] + risk[nrow][ncol]
			if neighbor not in cost_so_far or newcost < cost_so_far[neighbor]:
				cost_so_far[neighbor] = newcost
				priority = newcost + heuristic(neighbor)
				frontier.put(neighbor, priority)
				came_from[neighbor] = current
	return cost_so_far[(maxrow-1, maxcol-1)]

print("Part 1", astar(risk))
print("Part 2", astar(bigger))
