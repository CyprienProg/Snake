# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *
from Map import *

class Nourriture:
    def __init__(self, canvas, map, pos_x, pos_y, taille, couleur = "white"):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.couleur = couleur
        self.taille = taille
        self.canvas = canvas
        self.map = map
        self.id = self.canvas.create_oval(0, 0, self.taille, self.taille, fill = self.couleur)
        self.setposition(pos_x,pos_y)

    def nouvellePosition(self):
        x = randint(0, self.map.getlongueur())
        y = randint(0, self.map.getlargeur())
        self.setposition(x,y)

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def setposition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map.updateposition(self.pos_x, self.pos_y, self.id, self.taille)
