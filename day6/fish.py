from collections import Counter

# input is one line of comma-separated numbers,
# denoting each fish's internal timer
#puzzinput = open("demo.txt")
puzzinput = open("input.txt")
line = puzzinput.readline()

# each incidence of a number in the line
# is a fish with that internal timer value
inputfish = list(map(int, line.split(',')))
# index is the timer num, value is # fish with that timer
fish = [inputfish.count(i) for i in range(9)]

# demo
# numdays = 18
# Part 1: 80 days
# numdays = 80
# Part 2: 256 days
numdays = 256

# for each day, decrement all the fish timers
# if they hit 0, spawn a new fish w/ timer 8, and reset timer to 6
for i in range(numdays):
	# left rotate all the fish by 1
	# the old fish[0] is now fish[8]
	fish = fish[1:] + fish[:1]

	#number of reset fish = number of new fish
	fish[6] += fish[8]

totalfish = sum(fish)

print("Total fish", totalfish)
