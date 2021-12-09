#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
digits = 0
for line in puzzinput:
    splitline = line.split(" | ")
    fourdigits = splitline[1].split()
    # print("fourdigits ", fourdigits)

    #for signal in tensignals:
    for signal in fourdigits:
        numsegments = len(signal)
        if numsegments == 2 or numsegments == 3 or numsegments == 4 or numsegments == 7:
            digits += 1

print("digits ", digits)