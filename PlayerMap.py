class PlayerMap:
    def __init__(self, name):
        self.board = self.createBoard()
        self.name = name
        self.damage = 0
    def createBoard(self):
        boardX = []
        for x in range(10):
            boardY = []
            for y in range(10):
                boardY.append('-')
            boardX.append(boardY)
        return boardX
    def setShip(self, x, y, size, direc):
        if(direc == 'K'):
            for i in range(size):
                self.setPoint(x-i,y)
        elif(direc == 'G'):
            for i in range(size):
                self.setPoint(x+i,y)
        elif(direc == 'B'):
            for i in range(size):
                self.setPoint(x,y-i)
        elif(direc == 'D'):
            for i in range(size):
                self.setPoint(x,y+i)
    def setPoint(self, x, y):
        self.board[x][y] = 'O'

    def printForMe(self):
        screen = "   0  1  2  3  4  5  6  7  8  9\n"
        i =0
        for x in self.board:
            screen += str(i)+' '
            j=0
            for y in x:
                screen += ("["+y+"]")
                j += 1
            screen += '\n'
            i += 1
        print(screen)

    def printForEnemy(self):
        screen = "   0  1  2  3  4  5  6  7  8  9\n"
        i = 0
        for row in self.board:
            screen += str(i) + " "
            j = 0
            for col in row:
                for item in col:
                    if item == 'O':
                        screen += '[?]'
                        j += 1
                    elif item == 'X':
                        screen += '[X]'
                    elif item == '*':
                        screen += '[*]'
                    else:
                        screen += '[?]'
            i += 1
            screen += '\n'
        print(screen)



    def fire(self,x,y):
        if self.board[x][y] == 'O':
            self.board[x][y] = 'X'
            self.damage += 1
            print("hit")
        else:
            print("miss")
            self.board[x][y] = '*'
