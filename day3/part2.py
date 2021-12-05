# Advent Of Code Day 3 

# Lessons learned: try the small example if the full input isn't working
#puzzinput = open('demo.txt')
#numdigits = 5

puzzinput = open('input')
numdigits = 12

lines = puzzinput.readlines()

# lol turns out i misread
# turns out we have to re-find the mode each time

def findCommonDigit(lines,pos):
    digit = 0
    for line in lines:
        if line[pos]=="1":
                digit+=1
    if digit >= len(lines) / 2.0:
        return "1"
    else:
        return "0"

# got stuck so i looked at the reddit thread
def findoxygen(candidates, pos=0):
    print("Candidates for position ", pos)
    print(candidates)

    # only one candidate left
    if len(candidates) == 1:
        return int(candidates[0],2)
    
    # otherwise, find the most common digit at this pos
    # among the remaining candidates
    digit = findCommonDigit(candidates, pos)
    # only keep the ones that match
    return findoxygen(
        [c for c in candidates if c[pos] == digit], pos+1)

def findcarbon(candidates, pos=0):
    # print("Candidates for position ", pos)
    # print(candidates)

    # only one candidate left
    if len(candidates) == 1:
        return int(candidates[0],2)

    # otherwise, find the most common digit at this pos
    # among the remaining candidates
    digit = findCommonDigit(candidates, pos)
    # only keep the ones that don't match
    return findcarbon(
        [c for c in candidates if c[pos] != digit], pos+1)

oxygen = findoxygen(lines,  0)
print(oxygen)

carbon = findcarbon(lines, 0)
print(carbon)

life = oxygen * carbon
print(life)

# Incorrect guess:
# oxygen matches  4
# oxygen line  000001000101
# carbon matches  12
# carbon line  111101110011
# life 272895

# mode [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1]
# anti [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0]
# oxygen matches  12
# oxygen line  000010111101

# carbon matches  11
# carbon line  111101000011

# 738423 // too low???

# an incorrect implementation, that thought we were looking for the overall mode

# modematches = 0
# oxygen = ""
# for line in lines:
#     matches = 0
#     for i in range(0,numdigits):
#         digit = int(line[i])
#         if digit == mode[i]:
#             matches += 1
#         else: # we broke the streak
#             # if matches > modematches:
#             #     modematches = matches
#             #     oxygen = line
#             break
#     if matches > modematches:
#         modematches = matches
#         oxygen = line
#         print(oxygen)

# print("oxygen matches ", modematches)
# antimatches = 0
# carbon = ""
# for line in lines:
#     matches = 0
#     for i in range(0,numdigits):
#         digit = int(line[i])
#         if digit == anti[i]:
#             matches += 1
#         else: # we broke the streak
#             # if matches > antimatches:
#             #     antimatches = matches
#             #     carbon = line
#             break
#     if matches > antimatches:
#         antimatches = matches
#         carbon = line
#         print(carbon)

# print("carbon matches ", antimatches)

# redundant methods
def countdigits(lines, pos):
    digit = 0
    for line in lines:
        if line[pos]=="1":
                digit+=1
            
    # print(digit)
    return digit

def findmode(digits, numlines):
    mode = ""
    anti = ""
    for i in range(0,numdigits):
        # 1 was more common
        if digits[i] >= numlines / 2.0:
            mode += "1"
            anti += "0"
        else:
            mode += "0"
            anti += "1"
    # print("mode", mode)
    # print("anti", anti)
    # mode ['0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1']
    # anti ['1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0']
    return mode