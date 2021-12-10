from collections import deque

# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

heightmap = []

for line in puzzinput:
	nums = list(map(int, (c for c in line if c.isdigit())))
	heightmap.append(nums)

# find the low points
lowpoints = []
maxi = len(heightmap) - 1
maxj = len(heightmap[0]) - 1
risksum = 0
for i, row in enumerate(heightmap):
	for j, loc in enumerate(row):

		# check that loc is less than the positions up, down, left, right
		if (i > 0 and loc >= heightmap[i-1][j]):
			continue
		if (i < maxi and loc >= heightmap[i+1][j]):
			continue
		if (j > 0 and loc >= heightmap[i][j-1]):
			continue
		if (j < maxj and loc >= heightmap[i][j+1]):
			continue
		
		lowpoints.append((i,j))

# spread out from the lowpoint until we hit a 9
basinsizes = []
for lowpoint in lowpoints:
	print(lowpoint)
	neighbors = deque()
	neighbors.append(lowpoint)
	size = 0
	while len(neighbors) > 0:
		row, col = neighbors.popleft()
		# check if already dealt with
		if heightmap[row][col] == 9:
			continue
		#print("%s , %s" % (row,col))

		if (row > 0 and heightmap[row-1][col] < 9):
			#print("up")
			neighbors.append((row-1, col))
		if (row < maxi and heightmap[row+1][col] < 9):
			#print("down")
			neighbors.append((row+1, col))
		if (col > 0 and heightmap[row][col-1] < 9):
			#print("left")
			neighbors.append((row, col-1))
		if (col < maxj and heightmap[row][col+1] < 9):
			#print("right")
			neighbors.append((row, col+1))

		# mark we've already dealt with this
		heightmap[row][col] = 9 
		size += 1

	print("basin size ", size)
	basinsizes.append(size)

threebiggest = sorted(basinsizes)[-3:]
print("three biggest ", threebiggest)

answer = 1
for basin in threebiggest:
	answer *= basin

print("answer ", answer)







