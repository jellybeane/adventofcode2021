# Step forward, up, or down
puzzinput = open('input.txt')

horizontal = 0
depth = 0
for line in puzzinput:
    # format is eg "forward 8"
    command, value = line.split()
    value = int(value)
    # command = step[0]
    # value = int(step[1])

    if (command == "forward"):
        horizontal += value
    elif (command == "up"):
        depth -= value
    elif (command == "down"):
        depth += value

print("Horizontal ", horizontal)
print("Depth ", depth)
print(horizontal*depth)