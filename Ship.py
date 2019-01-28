class Ship:

    def __init__(self, type, direc):
        if(type == 'battleship'):
            self.fieldSize = 4
        elif(type == 'cruiser'):
            self.fieldSize = 3
        elif(type == 'destroyer'):
            self.fieldSize = 2
        elif(type == 'submarine'):
            self.fieldSize = 1
        self.direction = direc