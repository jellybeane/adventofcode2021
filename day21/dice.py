import math
import itertools
from collections import Counter

#pos = [4,8] #given positions are 1-indexed
pos = [1,10]
score = [0,0]

roll = 0
while score[0] < 1000 and score[1] < 1000:
    index = roll % 2
    destination = pos[index]
    # each player rolls 3 times
    for i in range(3):
        roll += 1
        destination = (destination + roll) % 10 or 10
    pos[index] = destination
    score[index] += destination
    #print("player %s: %s %s" % (2-index, destination, score[index]))

# part 1: losing score times number of rolls
print("Part 1:", roll * min(score[0], score[1]))

# part 2: ???
# referenced https://github.com/mebeim/aoc/blob/master/2021/README.md#day-21---dirac-dice
pos = [4,8]
#pos = [1,10]
# all 27 possible outcomes
possiblerolls = list(map(sum, itertools.product(range(1,4), range(1,4), range(1,4))))
# map of sums to # of ways to roll that sum
waystoroll = Counter(possiblerolls)

threshold = 3
def diracdice(pos, score, otherpos, otherscore):
    if score >= threshold:
        return 1, 0 # i won, they lost
    if otherscore >= threshold:
        return 0, 1 # i lost, they won

    my_wins = 0
    other_wins = 0

    for roll in possiblerolls:
        newpos = (pos + roll) % 10 or 10
        newscore = score + newpos

        # the other player's turn
        othersubwins, mysubwins = diracdice(otherpos, otherscore, newpos, newscore)

        # update num wins
        my_wins += mysubwins
        other_wins += othersubwins

    return my_wins, other_wins

mywins, otherwins = diracdice(pos[0], 0, pos[1], 0)
print(mywins, otherwins)
