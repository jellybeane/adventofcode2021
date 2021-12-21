from collections import Counter

puzzinput = open("demo.txt")
# puzzinput = open("input.txt")

# first line: image enhancement algorithm
# blank line
# grid
alg, gridlines = puzzinput.read().split('\n\n')
gridlines = gridlines.split('\n')

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

def enhance(grid):
    lit = 0
    enhanced = ['.'*(len(grid[0])+2)]
    for i, row in enumerate(grid):
        e = '.'
        for j, pixel in enumerate(row):
            s = ''
            # the 3x3 grid
            minrow = max(0, i-1)
            maxrow = min(i+1, len(grid)-1)
            mincol = max(0, j-1)
            maxcol = min(j+1, len(row)-1)
            if i == 0:
                s += '...'
            for ni in range(minrow, maxrow+1):
                if j == 0:
                    s += '.'
                for nj in range(mincol, maxcol+1):
                    s += grid[ni][nj]
                if j == maxcol:
                    s += '.'
            if i == maxrow:
                s += '...'

            indexstr = s.replace('.', '0').replace('#','1')
            index = int(indexstr, 2)
           # print(i, j, s, index)
            e += alg[index]
        e += '.'

        lit += Counter(e)['#']
        enhanced.append(e)

    enhanced.append('.'*(len(grid[0])+2))

    return enhanced, lit

enhanced, lit = enhance(grid)
# why doesn't this match the example :(
for row in enhanced:
    print(row)

print("lit", lit)

enhanced, lit = enhance(enhanced)

for row in enhanced:
    print(row)

print("lit", lit)