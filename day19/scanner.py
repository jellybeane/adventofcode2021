import numpy as np

puzzinput = open("twod.txt")
#puzzinput = open("demo.txt")
#puzzinput = open("input.txt")

pings = []
scanner = None
for line in puzzinput:
    line = line.strip()
    if 'scanner' in line:
        scanner = []
    elif len(line) == 0:
        pings.append(scanner)
        scanner = None
    else:
        # 2D example
        x,y = map(int, line.split(','))
        scanner.append(np.array([x,y]))
        # x,y,z = map(int, line.split(','))
        # scanner.append([x,y,z])
# in case there wasn't an empty line after the last scanner
if scanner is not None:
    pings.append(scanner)

print(pings)

# distance between beacons, with scanner 0's indices
offsets = []
for i in range(len(pings[0])):
    itoj = []
    # just the upper triangle?
    for j in range(i, len(pings[0])):
        p1 = pings[0][i]
        print("p1", p1)
        p2 = pings[0][j]
        print("p2", p2)
        print("p1 to p2", p2 - p1)
        itoj.append(p2 - p1)
    print(itoj)
    offsets.append(itoj)

zerotoone = {}
for i in range(len(pings[1])):
    itoj = []
    # just the upper triangle?
    for j in range(i, len(pings[1])):
        p1 = pings[1][i]
        p2 = pings[1][j]
        o = p2 - p1
        print("o", o)

        # check if seen before?
        for oi, row in enumerate(offsets):
            for oj, offset in enumerate(row):
                print("offset", offset)
                if np.array_equal(o, offset):
                    zerotoone[pings[0][oi]] = pings[1][i]
                    zerotoone[pings[0][oj]] = pings[1][j]
                elif np.array_equal(o, -offset):
                    zerotoone[pings[0][oi]] = pings[1][j]
                    zerotoone[pings[0][oj]] = pings[1][i]

print(zerotoone)