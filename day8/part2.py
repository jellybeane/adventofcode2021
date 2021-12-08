# puzzinput = open("oneline.txt")
# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# Part 2: Decode the four-digit values and sum them
sumofvals = 0
for line in puzzinput:
    splitline = line.split(" | ")
    tensignals = splitline[0].split()
    fourdigits = list(map(set, splitline[1].split()))
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

    tensignals.remove(numbers[1])
    tensignals.remove(numbers[4])
    tensignals.remove(numbers[7])
    tensignals.remove(numbers[8])

    # the mapping of baseline letters to this line's letters
    letters = {}
    # a is the difference between 1 and 7
    # this is how you unpack single-element sets apparently
    (letters['a'],) = set(numbers[7]).difference(set(numbers[1]))

    # 9 | 1478
    set4 = set(numbers[4])
    for signal in tensignals:
        numsegments = len(signal)
        if numsegments == 6:
            signalset = set(signal)
            # 9 is the only 6-segment that containts a superset of 4
            if signalset > set4:
                numbers[9] = signal
                 # g is whichever one isn't a
                (letters['g'],) = signalset.difference(set4).difference({letters['a']})
                tensignals.remove(signal)
                break
    # 3 | 14789
    set1 = set(numbers[1])
    for signal in tensignals:
        numsegments = len(signal)
        # 2 = acdeg
        # 3 = acdfg
        # 5 = abdfg
        if numsegments == 5:
            signalset = set(signal)
            # 3 is the only one that contains cf, we know that 1 is cf
            if signalset > set1:
                numbers[3] = signal
                # d is the one that isn't a or g
                ag = {letters['a'], letters['g']}
                adg = signalset.difference(set1)
                (letters['d'], ) = adg.difference(ag)
                tensignals.remove(signal)
                break
    
    # 06 | 134789
    for signal in tensignals:
        numsegments = len(signal)
        # 0 = abcefg
        # 6 = abdefg
        # 6 has d but 0 doesn't. 9 was previously removed
        if numsegments == 6:
            if (letters['d'] in signal):
                numbers[6] = signal
            else:
                numbers[0] = signal
    
    tensignals.remove(numbers[0])
    tensignals.remove(numbers[6])

    # 25 | 01346789
    set6 = set(numbers[6])
    for signal in tensignals:
        # 5 is a subset of 6
        if set(signal) < set6:
            numbers[5] = signal
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
