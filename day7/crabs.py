import statistics

def totalfuel(pos, crabs):
	sum = 0
	for crab in crabs:
		sum += abs(pos - crab)

	return sum

# input is one line of comma-separated numbers,
# denoting each crab's horizontal position
#puzzinput = open("demo.txt")
puzzinput = open("input.txt")
line = puzzinput.readline()

crabs = list(map(int, line.split(',')))
print(crabs)

mean = statistics.mean(crabs)

print("mean ", mean)
print("totalfuel ", totalfuel(mean, crabs))

# part 1: the median of the crabs
median = statistics.median(crabs)
print("median ", median)
print("totalfuel", totalfuel(median, crabs))