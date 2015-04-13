# Créé par Haccuria, le 13/04/2015 en Python 3.2
from Corpss import *

class Serpentt:
    def __init__(self):
        self.liste = []
        self.agrandir(3)

    def move_left(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0]-1, pos[1])
        dernier_corps.setPosition(pos[0], pos[1])

    def move_right(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0]+1, pos[1])
        dernier_corps.setPosition(pos[0], pos[1])

    def move_up(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0], pos[1]-1)
        dernier_corps.setPosition(pos[0], pos[1])

    def move_down(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getPosition()
        pos = (pos[0], pos[1]+1)
        dernier_corps.setPosition(pos[0], pos[1])

    def possible_left(self):
        pos = self.liste[0].getPosition()
        pos = (pos[0]-1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getPosition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_right(self):
        pos = self.liste[0].getPosition()
        pos = (pos[0]+1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getPosition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_up(self):
        pos = self.liste[0].getPosition()
        pos = (pos[0], pos[1]-1 )
        for corps in self.liste:
            pos_corps = corps.getPosition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_down(self):
        pos = self.liste[0].getPosition()
        pos = (pos[0], pos[1]+1 )
        for corps in self.liste:
            pos_corps = corps.getPosition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def getPosition(self):
        pos = self.liste[0].getPosition()
        return (pos[0], pos[1])

    def agrandir(self, nombre):
        for i in range (nombre):
            corps = Corpss()
            self.liste.append(corps)
