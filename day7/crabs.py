import statistics
import math

def totalfuel(pos, crabs):
	return sum(abs(pos - crab) for crab in crabs)

# input is one line of comma-separated numbers,
# denoting each crab's horizontal position
#puzzinput = open("demo.txt")
puzzinput = open("input.txt")
line = puzzinput.readline()

crabs = list(map(int, line.split(',')))
#print(crabs)

mean = statistics.mean(crabs)

print("mean ", mean)
print("totalfuel ", totalfuel(mean, crabs))

# part 1: the median of the crabs
median = statistics.median(crabs)
print("median ", median)
print("totalfuel", totalfuel(median, crabs))

# part 2: each change of 1 step in horizontal position
# costs 1 more unit of fuel than the last: 
# the first step costs 1, the second step costs 2, 
# the third step costs 3, and so on.
def part2fuel(pos, crabs):
	fuel = 0
	for crab in crabs:
		distance = abs(pos - crab)
		# the sum of {1, 2, .., distance}
		fuel += (distance**2 + distance)/2
	return fuel

# the mean is close to the best answer
mincrab = math.floor(mean) - 1
maxcrab = math.ceil(mean) + 1

# ??? exhaustive search
# there's not that many positions
lowestcost = part2fuel(maxcrab, crabs)
bestpos = maxcrab
for pos in range(mincrab, maxcrab):
	cost = part2fuel(pos, crabs)
	if cost < lowestcost:
		lowestcost = cost
		bestpos = pos

print("bestpos ", bestpos)
print("fuel cost", lowestcost)
