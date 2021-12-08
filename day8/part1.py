#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# the baseline mapping of number to letters
segments = [
    "abcefg", #0
    "cf", #1
    "acdeg", #2
    "acdfg", #3
    "bcdf", #4
    "abdfg", #5
    "abdefg", #6
    "acf", #7
    "abcdefg", #8
    "abcdfg", #9
]

# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
digits = 0
for line in puzzinput:
    splitline = line.split(" | ")
    tensignals = splitline[0].split()
    fourdigits = splitline[1].split()
    print("fourdigits ", fourdigits)

    one = ""
    four = ""
    seven = ""
    eight = ""

    #for signal in tensignals:
    for signal in fourdigits:
        numsegments = len(signal)
        if numsegments == 2:
            digits += 1
            #one = signal
        elif numsegments == 3:
            digits += 1
            #seven = signal
        elif numsegments == 4:
            digits += 1
            #four = signal
        elif numsegments == 7:
            digits += 1
            #eight = signal

    # if one in fourdigits or four in fourdigits or seven in fourdigits or eight in fourdigits:
    #     digits += 1

print("digits ", digits)