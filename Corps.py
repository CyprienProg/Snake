# Créé par Haccuria, le 13/04/2015 en Python 3.2

class Corps:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def move(self, x, y):
        self.pos_x += x
        self.pos_y += y

    def getPosition(self):
        return (self.pos_x, self.pos_y)

    def setPosition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
