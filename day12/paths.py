import copy
from collections import Counter

# puzzinput = open("smallcave.txt")
# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# input is connections between caves, separated by -
connections = {}
for line in puzzinput:
    a, b = line.strip().split('-')
    if a not in connections:
        connections[a] = []
    if b not in connections:
        connections[b] = []
    connections[a].append(b)
    connections[b].append(a)

print("connections ", connections)


# Part 1: find all the paths that visit small caves at most once
def dfs(connections, curcave, curpath, paths):
    curpath.append(curcave)

    if curcave == "end":
            print(curpath)
            paths.append(curpath)
            return

    for nextcave in connections[curcave]:
        if not nextcave in curpath or nextcave.isupper():
            dfs(connections, nextcave, copy.deepcopy(curpath), paths)

# Part 2: may visit one small cave twice
def part2(connections, curcave, curpath, paths):
    curpath.append(curcave)

    if curcave == "end":
            #print(curpath)
            paths.append(curpath)
            return

    for nextcave in connections[curcave]:
        # always add new or uppercase caves
        if not nextcave in curpath or nextcave.isupper():
            part2(connections, nextcave, copy.deepcopy(curpath), paths)
        # re-add a lowercase only if there are no double-visit lowercases
        elif not nextcave == "start":
            counts = Counter(curpath)
            for cave, count in counts.items():
                if cave.islower() and count == 2:
                    break
            else:
                part2(connections, nextcave, copy.deepcopy(curpath), paths)

# paths = []
# dfs(connections, "start", [])
# print("num paths", len(paths))

paths = []
part2(connections, "start", [], paths)
print("num paths", len(paths))
