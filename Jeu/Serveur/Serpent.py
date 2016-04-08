# Créé par Haccuria, le 13/04/2015 en Python 3.2
from Corps import *

class Serpent:
    def __init__(self):
        self.liste = []
        self.agrandir(3)
    def updateMovement(self):
        print("")

    def move_left(self, max):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0]-1, pos[1])
        if pos[0] >= 0:
            dernier_corps.setPosition(pos[0], pos[1])
        else:
            dernier_corps.setPosition(max, pos[1])

    def move_right(self, max):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = ((pos[0]+1)%max, pos[1])
        dernier_corps.setPosition(pos[0], pos[1])

    def move_up(self, max):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0], pos[1]-1)
        if pos[1] >= 0:
            dernier_corps.setPosition(pos[0], pos[1])
        else:
            dernier_corps.setPosition(pos[0], max)

    def move_down(self, max):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0], (pos[1]+1)%max)
        dernier_corps.setPosition(pos[0], pos[1])

    def getPosition(self):
        pos = self.liste[0].getPosition()
        return (pos[0], pos[1])

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




