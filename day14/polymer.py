from collections import Counter

#puzzinput = open("demo.txt")
puzzinput = open("input.txt")

template, _, *rules = puzzinput.read().split('\n')
print(rules)
rules = dict(r.split(" -> ") for r in rules)

numpairs = {}
letters = {}

# from the original template
for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair not in numpairs:
            numpairs[pair] = 1
        else:
            numpairs[pair] += 1
for letter in template:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1

#part 1
#steps = 10
#part 2
steps = 40
for step in range(steps):
    newpairs = {}
    for pair, num in numpairs.items():
        middle = rules[pair]
        # the first half
        newpair1 = pair[0] + middle
        if newpair1 not in newpairs:
            newpairs[newpair1] = num
        else:
            newpairs[newpair1] += num
        # the second half
        newpair2 = middle + pair[1]
        if newpair2 not in newpairs:
            newpairs[newpair2] = num
        else:
            newpairs[newpair2] += num

        if middle not in letters:
            letters[middle] = num
        else:
            letters[middle] += num

    numpairs = newpairs

# # counting up the letters
# for pair, num in numpairs.items():
#     letters[pair[0]] += num
#     letters[pair[1]] += num

# # internal letters are doublecounted,
# # but the first and last are single-counted
# letters[template[0]] += 1
# letters[template[-1]] += 1

print(letters)

# find the difference between the quantity of the most
# and least common elements
mostcommonletter = ""
mostcommonnum = 0
leastcommonletter = ""
leastcommonnum = len(template) ** steps

for letter, num in letters.items():
    if num < leastcommonnum:
        leastcommonletter = letter
        leastcommonnum = num
    if num > mostcommonnum:
        mostcommonletter = letter
        mostcommonnum = num

print("most common: %s %s" % (mostcommonletter, mostcommonnum))
print("least common: %s %s" % (leastcommonletter, leastcommonnum))
print("difference", mostcommonnum - leastcommonnum)
