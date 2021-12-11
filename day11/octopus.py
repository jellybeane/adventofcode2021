# puzzinput = open("smaller.txt")
# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

octopi = []

for line in puzzinput:
	octopi.append(list(map(int, (c for c in line if c.isdigit()))))

numoctopi = len(octopi) * len(octopi[0])

#print("Initial state")
#print(octopi)

# numsteps = 2
# numsteps = 10
# numsteps = 100
numsteps = 2000

# Part 1: total flashes over all steps
totalflashes = 0
# Part 2: when do all octopi flash simultaneously
allflash = -1
for step in range(numsteps):
    checkflash = False # Do we need to propagate flashes??
    flashes = 0 # flashes this step

    # First, the energy level of each octopus increases by 1
    for i, row in enumerate(octopi):
        for j, octopus in enumerate(row):
            octopi[i][j] += 1
            # Octopi that flash from the baseline energy increase
            if octopi[i][j] > 9:
                checkflash = True
    #print("After adding 1")
    print(octopi)

    # need to propagate flashes
    while checkflash:
        #print("Propagating")
        checkflash = False
        for i, row in enumerate(octopi):
            for j, octopus in enumerate(row):
                if octopi[i][j] > 9:
                    # flashed octopi get set to 0
                    octopi[i][j] = 0
                    flashes += 1
                    # increment neighbors
                    minrow = max(0, i-1)
                    maxrow = min(i+1, len(octopi)-1)
                    mincol = max(0, j-1)
                    maxcol = min(j+1, len(row)-1)
                    # print("minrow %s maxrow %s" % (minrow, maxrow))
                    # print("mincol %s maxcol %s" % (mincol, maxcol))
                    for ni in range(minrow, maxrow+1):
                        for nj in range(mincol, maxcol+1):
                            # ignore any that have already flashed
                            if octopi[ni][nj] == 0:
                                continue
                            octopi[ni][nj] += 1
                            # if the neighbor will also flash
                            if octopi[ni][nj] > 9:
                                checkflash = True # need to propagate

    #print("After step ", step)
    # print(octopi)
    totalflashes += flashes
    # find the first time all octopi flash
    if flashes == numoctopi:
        allflash = step + 1 # the step nums are 1-indexed
        break
    
print("totalflashes ", totalflashes)
print("synchronized flashes", allflash)