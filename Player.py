# Créé par Haccuria, le 06/12/2015 en Python 3.2
class Joueur:
    def __init__(self, name, pos, color, length):
        self.name = name
        self.pos = pos
        self.color = color
        self.length = length

    def getPosition(self):
        return self.liste[0].getPosition()

    def agrandir(self, nombre):
        for i in range (nombre):
            corps = Corps()
            self.liste.append(corps)
            corps.setPosition(self.getPosition()[0], self.getPosition()[1])

    def getListeCorps(self):
        return self.liste

    def contains(self, pos_x, pos_y):
        for corps in self.liste:
            if pos_x == corps.getPosition()[0] and pos_y == corps.getPosition()[1]:
                return True
        return False

    def setPosition(self, pos_x, pos_y, direction="Left"):
        for corps in self.liste:
            corps.setPosition(pos_x, pos_y)
            if direction == "Left":
                pos_x -= 1
            elif direction == "Right":
                pos_x += 1
            elif direction == "Down":
                pos_y += 1
            elif direction == "Up":
                pos_y -= 1

    def set_movment_up(self):
        self.direction ="up"

    def set_movment_down(self):
        self.direction = "down"

    def set_movment_left(self):
        self.direction = "left"

    def set_movment_right(self):
        self.direction = "right"

