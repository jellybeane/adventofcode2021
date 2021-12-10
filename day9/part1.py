# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

heightmap = []

for line in puzzinput:
	heightmap.append(list(map(int, (c for c in line if c.isdigit()))))

# for row in heightmap:
# 	print(row for row in heightmap)
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
		# The risk level of a low point is 1 plus its height
		risksum += 1 + loc

print("risksum ", risksum)