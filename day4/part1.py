# Bingo!

class BoardEntry:
    def __init__(self, num):
        self.num = num
        self.called = False

class Board:
    def __init__(self, lines, index):
        assert len(lines) == 5
        
        # the index in the original list of boards
        self.index = index
        # a list of lists: each list is a row
        self.entries = []
        for line in lines:
            boardline = []
            for i, val in enumerate(line.split()):
                boardline.append(BoardEntry(int(val)))
            self.entries.append(boardline)
    
    def __str__(self) -> str:
        s = ""
        for line in self.entries:
            linestring = ""
            for entry in line:
                linestring += "%s, " % entry.num
            s += linestring + "\n"
        return s

    # if draw is among the entries, set Called to True
    def update(self, draw):
        foundval = False
        for line in self.entries:
            for entry in line:
                if entry.num == draw:
                    entry.called = True
                    foundval = True
                    break
            if foundval:
                break
    
    # rows & columns win
    def iswinner(self):
        colwinners=[True] * 5
        for line in self.entries:
            linewinner = True
            for i, entry in enumerate(line):
                if entry.called == False:
                    linewinner = False
                    colwinners[i] = False
            if linewinner:
                return True

        return True in colwinners 
    
    # the sum of the unmarked numbers
    def score(self):
        sum = 0
        for line in self.entries:
            for entry in line:
                if entry.called == False:
                    sum += entry.num
        print("Sum of unmarked numbers", sum)
        return sum

# puzzinput = open("demo.txt")
puzzinput = open("input.txt")

# The first line is the order in which to draw numbers
draws = [int(d) for d in puzzinput.readline().split(',')]

# a blank line
puzzinput.readline()

# the rest of the file is bingo boards
bingoboards = []
boardlines = []
for line in puzzinput:
    # an empty divider line
    if len(line.split()) == 0:
        # we should have just completed a board
        assert len(boardlines) == 0
        continue

    boardlines.append(line)
    
    if (len(boardlines) == 5):
        board = Board(boardlines, len(bingoboards))
        # print ("Board finished \n", board)
        bingoboards.append(board)
        boardlines = []

    
# play bingo!
# Part 1: find the first board to win
# foundwinner = False
# for draw in draws:
#     # update all boards
#     for board in bingoboards:
#         board.update(draw)

#     # did anybody win?
#     for i, board in enumerate(bingoboards):
#         if board.iswinner():
#             print("Winner! Board %s on draw %s" % (i, draw))
#             print(board)
#             print("Score: ", draw * board.score())
#             foundwinner = True
#             break
#     if foundwinner:
#         break

# Part 2: find the last board to win
for draw in draws:

    # update all boards
    for board in bingoboards:
        board.update(draw)

    # did anybody win?
    winners = [] # more than one board may win per turn
    for i, board in enumerate(bingoboards):
        if board.iswinner():
            print("Winner! Board %s on draw %s" % (board.index, draw))
            print(board)
            print("Score: ", draw * board.score())
            print("\n")
            winners.append(i) # the list index, not the original index
    # if a board won, remove it from the list
    if (len(winners) > 0):
        for i in sorted(winners, reverse=True):
            del bingoboards[i]
    
    if len(bingoboards) == 0:
        break
        

