# "up" and "down" now modify "aim"
# "forward" moves forward, but also depth by aim * value
puzzinput = open('input.txt')

horizontal = 0
depth = 0
aim = 0
for line in puzzinput:
    step = line.split()
    command = step[0]
    value = int(step[1])

    if (command == "forward"):
        horizontal += value
        depth += aim * value
    elif (command == "up"):
        aim -= value
    elif (command == "down"):
        aim += value

print("Horizontal ", horizontal)
print("Depth ", depth)
print(horizontal*depth)