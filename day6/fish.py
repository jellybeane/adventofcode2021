from collections import Counter

# input is one line of comma-separated numbers,
# denoting each fish's internal timer
#puzzinput = open("demo.txt")
puzzinput = open("input.txt")
line = puzzinput.readline()

# each incidence of a number in the line
# is a fish with that internal timer value
fish = dict(Counter(map(int, line.split(','))))
# fill in the rest of the dictionary just in case
for i in range(9):
	if i not in fish:
		fish[i] = 0

# demo
# numdays = 18
# Part 1: 80 days
# numdays = 80
# Part 2: 256 days
numdays = 256

for i in range(numdays):
	# when the fish counter reaches 0,
	# spawn a new fish and reset counter to 6
	spawns = fish[0]

	# bump all the fish 1 day
	for t in range(8):
		fish[t] = fish[t+1]

	fish[6] += spawns # the reset fish
	fish[8] = spawns # the new fish

totalfish = 0
for numfish in fish.values():
	totalfish += numfish

print("Total fish", totalfish)
