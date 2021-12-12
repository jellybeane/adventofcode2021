import copy

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

paths = []

def dfs(connections, curcave, curpath):
    curpath.append(curcave)

    if curcave == "end":
            print(curpath)
            paths.append(curpath)
            return

    for nextcave in connections[curcave]:
        if not nextcave in curpath or nextcave.isupper():
            dfs(connections, nextcave, copy.deepcopy(curpath))

dfs(connections, "start", [])

print("num paths", len(paths))
