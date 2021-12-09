# puzzinput = open("oneline.txt")
# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# Part 2: Decode the four-digit values and sum them
sumofvals = 0
for line in puzzinput:
    splitline = line.split(" | ")
    tensignals = splitline[0].split()
    fourdigits = splitline[1].split()
    # print("fourdigits ", fourdigits)

    # Note: letter ordering isn't guaranteed to be the same
    # between tensignals and fourdigits
    numbers = [""] * 10 # the number-to-letters mapping for this line

    # 1478
    for signal in tensignals:
        numsegments = len(signal)
        # 1 = cf
        if numsegments == 2:
            numbers[1] = signal
        # 7 = acf
        elif numsegments == 3:
            numbers[7] = signal
        # 4 = bcdf
        elif numsegments == 4:
            numbers[4] = signal
        # 8 = abcdefg
        elif numsegments == 7:
            numbers[8] = signal

    # print("1478 %s %s %s %s" % (numbers[1], numbers[4], numbers[7], numbers[8]))

    # 9 0 6 | 1478
    set1 = set(numbers[1])
    set4 = set(numbers[4])
    for signal in tensignals:
        numsegments = len(signal)
        if numsegments == 6:
            signalset = set(signal)
            # 9 is the only 6-segment that containts a superset of 4
            if signalset > set4:
                numbers[9] = signal
            # 0 is a superset of 1 but not 4
            elif signalset > set1:
                numbers[0] = signal
            # otherwise, it's 6
            else:
                numbers[6] = signal

    # 3 5 2 | 0146789
    set6 = set(numbers[6])
    for signal in tensignals:
        numsegments = len(signal)
        # 2 = acdeg
        # 3 = acdfg
        # 5 = abdfg
        if numsegments == 5:
            signalset = set(signal)
            # 3 is a superset of 1
            if signalset > set1:
                numbers[3] = signal
            # 5 is a subset of 6
            elif signalset < set6:
                numbers[5] = signal
            # otherwise it's 2
            else:
                numbers[2] = signal

    # the four digits
    multiplier = 1000
    output = 0
    for signal in fourdigits:
        for i in range(10):
            if set(signal) == set(numbers[i]):
                output += i * multiplier
                break
        multiplier /= 10
    
    # print("output ", output)
    sumofvals += output

print("sumofvals ", sumofvals)
