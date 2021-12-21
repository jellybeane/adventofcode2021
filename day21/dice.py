#pos = [3,7] given positions are 1-indexed
pos = [0,9]
score = [0,0]

roll = 0
while score[0] < 1000 and score[1] < 1000:
    index = roll % 2
    sum = 0
    destination = pos[index]
    # each player rolls 3 times
    for i in range(3):
        roll += 1
        destination = (destination + roll) % 10
    pos[index] = destination
    # the board is 1-indexed
    score[index] += destination+1
    print("player %s: %s %s" % (2-index, destination+1, score[index]))

# part 1: losing score times number of rolls
print(roll * min(score[0], score[1]))
