import math
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
    print("player %s: %s %s" % (2-index, destination, score[index]))

# part 1: losing score times number of rolls
print(roll * min(score[0], score[1]))

 # part 2: ???

# map roll total to # ways 3 rolls can sum to it
testrolls = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            testrolls.append(i+j+k)
waystoroll = Counter(testrolls)

threshold = 2
#for turn in range(threshold*2):

