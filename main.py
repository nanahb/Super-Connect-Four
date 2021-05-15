from Board import Board
class Printer:
    def __init__(self, colMap={"A":"[0;37;41m", "B":"[6;30;42m"} ):
        self.colMap = colMap
    def printRow(self, r):
        res = "|"
        for x in r:
            if x==None:
                res += " " 
            else: 
                col = '\x1b'+self.colMap[x]
                res += col + x + '\x1b[0m'
            res += "|"
        return res
    def printMessage(self, playerChar, message):
        col = '\x1b'+self.colMap[playerChar]
        res = col + message + '\x1b[0m'
        print(res)

class Game:
    def __init__(self):
        self.printer = Printer()
        self.board = Board(self.printer)
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
            self.printer.printMessage(currentPlayer, self.userLookupTable[currentPlayer] +"'s turn")
            print("\n")
            # print(self.userLookupTable[currentPlayer] +"'s turn \n")
            inputStr = input("specify position i,j:")
            inputList = inputStr.split(",")
            i = int(inputList[0])
            j = int(inputList[1])
            didWin = self.board.putCoin(currentPlayer, i, j)
            if didWin:
                self.printer.printMessage(currentPlayer, "Player " + self.userLookupTable[currentPlayer] + " won!!!!!")
                exit()
            if currentPlayer == "A":
                currentPlayer = "B"
            else:
                currentPlayer = "A"
            










Game().start()