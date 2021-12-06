from collections import Counter

# input is one line of comma-separated numbers,
# denoting each fish's internal timer
#puzzinput = open("demo.txt")
puzzinput = open("input.txt")
line = puzzinput.readline()

fish = dict(Counter(map(int, line.split(','))))
# fill in the rest of the dictionary just in case
for i in range(9):
	if i not in fish:
		fish[i] = 0

# numdays = 18
numdays = 80

for i in range(numdays):
	# when the fish counter reaches 0,
	# spawn a new fish and reset counter to 6
	spawns = fish[0]
	fish[0] = fish[1]
	fish[1] = fish[2]
	fish[2] = fish[3]
	fish[3] = fish[4]
	fish[4] = fish[5]
	fish[5] = fish[6]
	fish[6] = fish[7] + spawns # the reset fish
	fish[7] = fish[8]
	fish[8] = spawns # the new fish

totalfish = 0
for numfish in fish.values():
	totalfish += numfish

print("Total fish", totalfish)
