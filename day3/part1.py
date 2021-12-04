# Advent Of Code Day 3 

puzzinput = open('input')

# We are given binary numbers
# Gamma rate: a binary number where each digit is the most common bit for each input digit
# Epsilon rate: a binary number where each digit is the least common bit for each input digit

numdigits = 12
digits=[0] * numdigits

numlines = 0
for line in puzzinput:
    for i in range(0,12):
        if line[i]=="1":
            digits[i]+=1
    numlines += 1

print(digits)

gamma = "0b"
epsilon = "0b"
for i in range(0,12):
    # 1 was more common
    if digits[i] > numlines / 2.0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Gamma", gamma)
print("Epsilon", epsilon)

power = int(gamma,2) * int(epsilon,2)
print(power)
