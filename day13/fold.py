from collections import Counter

# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

dotlines, instructionlines = puzzinput.read().split('\n\n')
dotlines = dotlines.split('\n')
instructionlines = instructionlines.split('\n')

dots = [tuple(map(int, line.strip().split(','))) for line in dotlines]
instructions = []
for line in instructionlines:
    axis, val = line.strip().split()[2].split('=')
    instructions.append((axis, int(val)))
        
maxx, maxy = map(max, zip(*dots))
maxx += 1
maxy += 1

# the array goes [row][col], so [y][x]
unfolded = [['.' for x in range(maxx)] for y in range(maxy)]
for x,y in dots:
    unfolded[y][x] = '#'

# for row in unfolded:
#     print(row)
part1 = 0
for instruction in instructions:
    foldline = instruction[1]
    #print("foldline", foldline)
    if instruction[0] == 'y':
        # horizontal fold
        folded = [['.' for x in range(maxx)] for y in range(foldline)]
        # from row 0 to the fold, it's the same
        for y in range(0, foldline):
            for x in range(maxx):
                folded[y][x] = unfolded[y][x]
        # from foldline+1 to the end, it's reversed
        for i in range(1, maxy - foldline):
            for x in range(maxx):
                if unfolded[foldline + i][x] == '#':
                    folded[foldline - i][x] = '#'
        maxy = foldline
    else:
        # vertical fold
        folded = [['.' for x in range(foldline)] for y in range(maxy)]
        for y in range(maxy):
            # from col 0 to the fold, it's the same
            for x in range(0, foldline):
                folded[y][x] = unfolded[y][x]
            # from foldline+1 to the end, it's reversed
            for i in range(1, maxx - foldline):
                if unfolded[y][foldline+i] == '#':
                    folded[y][foldline-i] = '#'
        maxx = foldline

    # Part 1: count the number of dots after the first fold
    if part1 == 0:
        for row in folded:
            counts = Counter(row)
            part1 += counts['#']
        print("Part 1", part1)

    unfolded = folded

# Part 2: what does it look like after folding?
for row in folded:
    s=""
    for c in row:
        s += c
    print(s)
