from collections import deque

# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# the corresponding close/open characters
closers = {')':'(', ']':'[', '}':'{', '>':'<'}

# Part 1: find the corrupted lines and sum their score
points = {')':3, ']':57, '}':1197, '>':25137}
score = 0
for line in puzzinput:
	toclose = deque()
	for c in line:
		if c in closers:
			lastopen = toclose.pop()
			# stop on the first illegal closer
			if lastopen != closers[c]:
				print("Tried to close %s with %s" % (lastopen, c))
				score += points[c]
				break

		else:
			toclose.append(c)

print("score ", score)