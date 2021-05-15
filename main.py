from Board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.userLookupTable = {}
    def start(self):
        playing = True
        currentPlayer = "A"
        playerAName = input("Please type player A's name:")
        playerBName = input("Please type player B's name:")
        self.userLookupTable["A"] = playerAName
        self.userLookupTable["B"] = playerBName
        while playing:
            print(self.board)
            print(self.userLookupTable[currentPlayer] +"'s turn \n")
            inputStr = input("specify position i,j:")
            inputList = inputStr.split(",")
            i = int(inputList[0])
            j = int(inputList[1])
            didWin = self.board.putCoin(currentPlayer, i, j)
            if didWin:
                print("Player " + self.userLookupTable[currentPlayer] + " won!!!!!")
                exit()
            if currentPlayer == "A":
                currentPlayer = "B"
            else:
                currentPlayer = "A"
            










Game().start()