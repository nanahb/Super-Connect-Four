"""
8 by 8 board
each turn, either player A or player B
board has squares. Each square can be blank, have an A coin, or have a B coin.

For A's turn, A can place a coin in a cell if the cell is empty and the square beneath it is NOT empty.
Winning condition: Player X (A or B) has 4 diagonal, horizontal, or vertical neighboring squares filled with their coins.

[
[None, None, None],
[None, None, None],
[None, None, None]
]
"""
      


class Board:
    def __init__(self, printer):
        self.squares = list(list(None for i in range(8)) for j in range(8))
        self.printer = printer

    """
    putCoin takes playerChar and i, j. Places coin in position (i,j) of the board if self.canPlace(self, i, j) returns true.
    """
    def putCoin(self, playerChar, i, j):
        if self.canPlace(i, j):
            self.squares[i][j] = playerChar
            didWin = self.checkWin(i, j)
            return didWin

    def checkWin(self, i, j):
        # check vertical
        verticalWin = self.countConsecutive(i, j, -1, 0) + self.countConsecutive(i, j, 1, 0) > 2
        if verticalWin:
            return True
        horizontalWin = self.countConsecutive(i, j, 0, -1) + self.countConsecutive(i,j, 0, 1) > 2
        if horizontalWin:
            return True
        diagonalLowerRight = self.countConsecutive(i, j, -1, -1) + self.countConsecutive(i,j, 1,1)>2
        if diagonalLowerRight:
            return True
        diagonalLowerLeft = self.countConsecutive(i,j, -1, 1) + self.countConsecutive(i,j, 1, -1)>2
        if diagonalLowerLeft:
            return True
        return False

    def indexValid(self, i, j):
        return i>=0 and i<8 and j>= 0 and j<8
    def countConsecutive(self, i, j, x, y):
        count = 0
        currentI, currentJ = i + x, j + y
        while self.indexValid(currentI, currentJ) and self.squares[currentI][currentJ] == self.squares[i][j]:
            count += 1
            currentI += x
            currentJ += y
        return count

    def canPlace(self, i, j):
        return self.squares[i][j] == None and ( i==7 or self.squares[i+1][j] != None )
    def size(self):
        return len(self.squares)
    def __str__(self):

        s = ""
        for i, row in enumerate(self.squares):
            s += str(i) + ":" + self.printer.printRow(row) + '\n'
        s += "   "
        
        for i in range(self.size()):
            s += str(i) + " "
        return s