from collections import Counter

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# first line: image enhancement algorithm
# blank line
# grid
alg, gridlines = puzzinput.read().split('\n\n')
gridlines = gridlines.split('\n')

alternate = False
if alg[0] == '#':
    alternate = True

grid = []

for line in gridlines:
    row = '..' + line.strip() + '..'

    if len(grid) < 1:
        grid.append('.'*len(row))
        grid.append('.'*len(row))

    grid.append(row)

grid.append('.'*len(grid[0]))
grid.append('.'*len(grid[0]))

for row in grid:
    print(row)

def enhance(grid, generation, alternate):
    # if alternating, odd generations will have infinite #s
    if alternate and generation%2 == 1:
        blanks = '#'
        prev = '.'
    else:
        blanks = '.'
        prev = '#'

    lit = 0
    enhanced = [blanks*(len(grid[0])+2)]
    for i, row in enumerate(grid):
        e = blanks
        for j, pixel in enumerate(row):
            s = ''
            # the 3x3 grid
            minrow = max(0, i-1)
            maxrow = min(i+1, len(grid)-1)
            mincol = max(0, j-1)
            maxcol = min(j+1, len(row)-1)
            if i == 0:
                s += prev*3
            for ni in range(minrow, maxrow+1):
                if j == 0:
                    s += prev
                for nj in range(mincol, maxcol+1):
                    s += grid[ni][nj]
                if j == maxcol:
                    s += prev
            if i == maxrow:
                s += prev*3

            indexstr = s.replace('.', '0').replace('#','1')
            index = int(indexstr, 2)
           # print(i, j, s, index)
            e += alg[index]
        e += blanks

        lit += Counter(e)['#']
        enhanced.append(e)

    enhanced.append(blanks*(len(grid[0])+2))

    return enhanced, lit

# part 1: the number of lit cells after two iterations
enhanced, lit = enhance(grid, 1, alternate)
for row in enhanced:
    print(row)

print("lit", lit)

enhanced, lit = enhance(enhanced, 2, alternate)

for row in enhanced:
    print(row)

print("lit", lit)