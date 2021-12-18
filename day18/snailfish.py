import math
from copy import deepcopy

class SnailNum():

    def depth(self):
        if self.parent is None:
            return 0
        
        return 1 + self.parent.depth()

    def __add__(self, other):
        return SnailPair(lst=None, left=deepcopy(self), right=deepcopy(other))

class SnailPair(SnailNum):
    def __init__(self, lst=None, left=None, right=None):
        # initializing from list
        if not lst is None:
            if isinstance(lst[0], int):
                self.left = SnailRegular(lst[0])
            else:
                self.left = SnailPair(lst[0])
            if isinstance(lst[1], int):
                self.right = SnailRegular(lst[1])
            else:
                self.right = SnailPair(lst[1])
        else: # initializing from left/right
            self.left = left
            self.right = right

        self.left.parent = self
        self.right.parent = self

        self.parent = None

    def setleft(self, left):
        self.left = left
        self.left.parent = self

    def setright(self, right):
        self.right = right
        self.right.parent = self

    def explode(self, depth):
        # check if the children need to explode
        if depth < 4:
            # explode left to right
            leftexplode = self.left.explode(depth+1)
            if leftexplode[0]:
                if not leftexplode[1] is None:
                    # the left child needs to be replaced
                    self.setleft(leftexplode[1])
                return True, None
            # only explore right if there were none on left
            rightexplode = self.right.explode(depth+1)
            if rightexplode[0]:
                if not rightexplode[1] is None:
                    # the right child needs to be replaced
                    self.setright(rightexplode[1])
                return True, None
            # came back, no explodes needed
            return False, None

        # otherwise, this is the one to explode

        # find the left neighbor
        curr = self
        # go up until you can go left
        while not curr.parent is None and curr == curr.parent.left:
            curr = curr.parent
        # the pair's left value is added to the first regular number
        # to the left of the exploding pair (if any)
        if not curr.parent is None:
            assert curr == curr.parent.right
            curr = curr.parent.left
            # go right until you hit a regular number
            while isinstance(curr, SnailPair):
                curr = curr.right
            # exploding pairs will always consist of 2 regular numbers
            curr.val += self.left.val

        # the right neighbor
        curr = self
        # go up until you can go right
        while not curr.parent is None and curr == curr.parent.right:
            curr = curr.parent
        # the pair's right value is added to the first regular number
        # to the right of the exploding pair (if any)
        if not curr.parent is None:
            assert curr == curr.parent.left
            curr = curr.parent.right
            # go left until you hit a regular number
            while isinstance(curr, SnailPair):
                curr = curr.left
            # exploding pairs will always consist of 2 regular numbers
            curr.val += self.right.val

        # replacement for self
        return True, SnailRegular(0)

    def split(self):
        leftsplit = self.left.split()
        if leftsplit[0]: # did a split happend down the left branch?
            if not leftsplit[1] is None:
                # the left child needs to be replaced
                self.setleft(leftsplit[1])
                return True, None
            return leftsplit
        rightsplit = self.right.split()
        if rightsplit[0]: # did a split happend down the right branch?
            if not rightsplit[1] is None:
                # the right child needs to be replaced
                self.setright(rightsplit[1])
                return True, None
            return rightsplit
        # no splits needed
        return False, None
    
    def reduce(self):
        while True:
            exploded = self.explode(self.depth())
            if not exploded[0]:
                splitted = self.split()
                if not splitted[0]:
                    # if nothing exploded or split, we're done
                    break
    
    def magnitude(self):
        return 3*self.left.magnitude() + 2*self.right.magnitude()

    def __str__(self):
        return '['+ str(self.left) + ',' + str(self.right) + ']'
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


class SnailRegular(SnailNum):
    def __init__(self, val):
        self.val = val
        self.parent = None

    def split(self):
        if self.val < 10:
            return False, None

        leftval = SnailRegular(int(math.floor(self.val/2)))
        rightval = SnailRegular(int(math.ceil(self.val/2)))
        return True, SnailPair(lst=None, left=leftval,right=rightval)
    
    def explode(self, depth):
        return False, None

    def magnitude(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result


#puzzinput = open("smalldemo.txt")
# puzzinput = open("demo.txt")
puzzinput = open("input.txt")
lines = puzzinput.readlines()

# Part 2: find the largest magnitude of the sum of any two snailnums
snails = [SnailPair(lst=eval(line.strip())) for line in lines]

magnitude = 0
for i in range(len(snails)-2):
    for j in range(i+1, len(snails)-1):
        # snail addition is not commutative
        s1 = snails[i] + snails[j]
        s1.reduce()
        m1 = s1.magnitude()
        if m1 > magnitude:
            magnitude = m1

        s2 = snails[j] + snails[i]
        s2.reduce()
        m2 = s2.magnitude()
        if m2 > magnitude:
            magnitude = m2

print(magnitude)