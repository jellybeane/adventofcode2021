from collections import deque

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# the corresponding close/open characters
closers = {')':'(', ']':'[', '}':'{', '>':'<'}
openers = {'(':')', '[':']', '{':'}', '<':'>'}

# Part 1: find the corrupted lines and sum their score
p1points = {')':3, ']':57, '}':1197, '>':25137}
part1 = 0
# Part 2: complete the incomplete lines, then take the middle score
p2points = {')':1, ']':2, '}':3, '>':4}
part2scores = []
for line in puzzinput:
	toclose = deque()
	corrupted = False
	for c in line.strip():
		if c in closers:
			lastopen = toclose.pop()
			# corrupted line
			if lastopen != closers[c]:
				#print("Tried to close %s with %s" % (lastopen, c))
				part1 += p1points[c]
				corrupted = True
				break

		else:
			toclose.append(c)

	if corrupted:
		continue

	# incomplete line
	score = 0
	while len(toclose) > 0:
		score = score * 5 + p2points[openers[toclose.pop()]]
	if score > 0:
		part2scores.append(score)

print("part1 ", part1)

part2answer = sorted(part2scores)[int(len(part2scores)/2)]
print("part 2", part2answer)