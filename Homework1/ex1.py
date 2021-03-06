class ConnectFour:

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""

        initialValue = self.board[x][y]
        #checks a cell to see if there is a piece there
        if initialValue != 0:
            #loops though 3 times in a certain direction to see
            #if there is a winning configuration
            for i in range(3):
                xIndex = x + (dx * (i+1))
                yIndex = y + (dy * (i+1))
                if (-1 < xIndex < self.h) and (-1 < yIndex < self.w):
                    if initialValue == self.board[xIndex][yIndex]:
                        continue
                    else:
                        return False
                else:
                    return False
            return True
        else:
            return False


    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        # Your code here, use isAnyLineAt()

        #Function loops through every cell on the board and checks
        #if that cell is part of a 4 in a row configuration
        for x in range(self.h):
            for y in range(self.w):
                #print("{} and {}".format(x, y))
                if self.isAnyLineAt(x, y):
                    return self.board[x][y]

        return 0



    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome()
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")

W = 7
H = 6
BOARD1 = [
    [0,0,0,0,0,0,2],
    [0,0,0,1,1,0,2],
    [0,0,0,1,2,0,2],
    [1,0,2,2,1,2,1],
    [1,0,0,1,0,1,2],
    [1,0,1,0,0,0,1]
]

c = ConnectFour(BOARD1, W, H)
c.printOutcome()
