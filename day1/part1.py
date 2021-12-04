# Advent Of Code Day 1
# For each line, is it greater than the previous?

puzzinput = open('input')

numdeeper = 0
prev = 10_000
for line in puzzinput:
    depth = int(line)
    if depth > prev:
        numdeeper += 1
    prev = depth

print(numdeeper)