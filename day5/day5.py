# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# 1000 x 1000 grid
coords = [ [0]*1000 for i in range(1000) ]
# Count the number of lines that include each point
for line in puzzinput:
    # format: 0,9 -> 5,9
    endpoints = line.split(" -> ")
    x1, y1 = map(int, endpoints[0].split(','))
    x2, y2 = map(int, endpoints[1].split(','))

    # Part 1: only consider vertical & horizontal lines
    # vertical lines
    if (x1 == x2):
        # not guaranteed to be in increasing order
        for i in range(min(y1,y2), max(y1,y2)+1):
            coords[x1][i] += 1
    # horizontal lines
    elif (y1 == y2):
        for i in range(min(x1,x2), max(x1,x2)+1):
            coords[i][y1] += 1
    # diagonal
    else:
        # for conveniece, impose that we start at the smaller x value
        if (x1<x2):
            start = (x1,y1)
            stop = (x2,y2)
        else:
            start = (x2,y2)
            stop = (x1,y1)
        # slope will be +=1
        slope = int((stop[1]-start[1])/(stop[0]-start[0]))
        # print("Slope: ", slope)
        for i in range(0, stop[0]-start[0]+1):
            x = start[0]+i
            y = start[1]+(slope * i)
            coords[x][y] += 1

# number of points where at least two lines overlap
overlaps = 0
for row in coords:
    for point in row:
        if point > 1:
            overlaps += 1

print("Overlaps: ", overlaps)