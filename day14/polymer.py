from collections import Counter

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

template = ""
atrules = False
rules = {}
for line in puzzinput:
    if atrules:
        pair, insert = line.strip().split(" -> ")
        rules[pair] = insert
    elif len(line.strip()) == 0:
        atrules = True
    else:
        template = line.strip()

steps = 10
for step in range(steps):
    buildup = ""
    lastletter = template[-1:]
    for i in range(len(template)-1):
        pair = template[i:i+2]
        buildup += pair[0] + rules[pair]

    template = buildup + lastletter

#print(template)

# Part 1: subtract the quantity of the least common element
# from the quantity of the most common element
counts = Counter(template).most_common()
most = counts[0]
print("most", most)
least = counts[len(counts)-1]
print("least", least)

print("part 1:", most[1]-least[1])

