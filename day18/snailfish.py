import math

class SnailNum():

    def depth(self):
        if self.parent is None:
            return 0
        
        return 1 + self.parent.depth()

    def magnitude(self):
        return NotImplemented # should be overridden (?)

    def __add__(self, other):
        return SnailPair(self, other)

class SnailPair(SnailNum):
    def __init__(self, left, right):
        self.left = left
        self.left.parent = self

        self.right = right
        self.right.parent = self

        self.parent = None

    def setleft(self, left):
        self.left = left
        self.left.parent = self

    def setright(self, right):
        self.right = right
        self.right.parent = self

    def magnitude(self):
        return 3*self.left.magnitude() + 2*self.right.magnitude()

    def explode(self):
        # the left neighbor
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
        return SnailNum(0)

class SnailRegular(SnailNum):
    def __init__(self, val):
        self.val = val
        self.parent = None

    def magnitude(self):
        return self.val

    def split(self):
        leftval = int(math.floor(self.val/2))
        rightval = int(math.ceil(self.val/2))
        return SnailPair(leftval,rightval)