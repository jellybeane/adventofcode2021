# Is the sum of a sliding window of 3 values, 
# greater than the previous sum?
puzzinput = open('input')

numdeeper = 0
threeSums = [0, 0, 0]
i = 0
for line in puzzinput:
    depth = int(line)

    if i > 2: # we have completed sums to compare
        prev = i%3 # this one finished last line
        curr = (i+1) % 3 # this one finished this line
        nxt = (i+2)%3 # this one will finish next line

        threeSums[curr] += depth
        threeSums[nxt] += depth

        if threeSums[curr] > threeSums[prev]:
            numdeeper +=1

        # don't need the previous value anymore, start building up the next   
        threeSums[prev] = depth

    else: # building it up the first time
        for j in range(0,  i+1):
            threeSums[j] += depth
        
    i += 1

print(numdeeper)

# This one tripped me up! Off by one errors