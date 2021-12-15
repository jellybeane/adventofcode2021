from queue import PriorityQueue

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

risk = []

for line in puzzinput:
	nums = list(map(int, (c for c in line.strip())))
	risk.append(nums)

maxrow = len(risk) - 1
maxcol = len(risk[0]) - 1

# Part 1: the total risk of the lowest-risk path
# from top left(0,0) to bottom right (maxrow, maxcol)

# helpers

# 4 neighbors: cannot move diagonally
def getneighbors(pos):
	row, col = pos
	neighbors = []
	if row > 0:
		neighbors.append((row-1,col))
	if col > 0:
		neighbors.append((row, col-1))
	if row < maxrow:
		neighbors.append((row+1, col))
	if col < maxcol:
		neighbors.append((row, col+1))
	return neighbors

# estimated cost to the end
def heuristic(pos):
	row, col = pos
	return 5 * (maxrow - row + maxcol - col)

# A*
frontier = PriorityQueue()
frontier.put((0,0), 0)
came_from = {}
came_from[(0,0)] = None
cost_so_far = {}
cost_so_far[(0,0)] = 0

while not frontier.empty():
	current = frontier.get()
	row, col = current

	# have we gotten to the end?
	if row==maxrow and col==maxcol:
		break

	for neighbor in getneighbors(current):
		nrow,ncol = neighbor
		newcost = cost_so_far[current] + risk[nrow][ncol]
		if neighbor not in cost_so_far or newcost < cost_so_far[neighbor]:
			cost_so_far[neighbor] = newcost
			priority = newcost + heuristic(neighbor)
			frontier.put(neighbor, priority)
			came_from[neighbor] = current

print("Final cost", cost_so_far[(maxrow, maxcol)])