﻿# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *
from Corps import *
from GUI import *


class Serpent:
    taille = 25
    pos_x = 0
    pos_y = 0
    def __init__(self, canvas, gui):
        self.liste = []
        self.canvas = canvas
        self.gui = gui
        self.agrandir(3)

    def go_left(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0]-1, pos[1])
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_right(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0]+1, pos[1])
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_up(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0], pos[1]-1)
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_down(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0], pos[1]+1)
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def possible_left(self):
        pos = self.liste[0].getposition()
        pos = (pos[0]-1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_right(self):
        pos = self.liste[0].getposition()
        pos = (pos[0]+1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_up(self):
        pos = self.liste[0].getposition()
        pos = (pos[0], pos[1]-1 )
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_down(self):
        pos = self.liste[0].getposition()
        pos = (pos[0], pos[1]+1 )
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def agrandir(self, nombre):
        for i in range (nombre):
            corps = Corps(self.canvas, self.gui, self.pos_x + i, self.pos_y, self.taille)
            self.liste.append(corps)
