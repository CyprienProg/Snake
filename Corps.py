# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *
from GUI import *

class Corps:
    def __init__(self, canvas, gui, pos_x, pos_y, taille, couleur = "green"):
        self.taille = taille
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.canvas = canvas
        self.gui = gui
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = self.couleur)
        self.setposition(pos_x, pos_y)

    def move_left(self):
        self.pos_x -= 1
        self.update()

    def move_right(self):
        self.pos_x += 1
        self.update()

    def move_up(self):
        self.pos_y -= 1
        self.update()

    def move_down(self):
        self.pos_y += 1
        self.update()

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def setposition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.update()

    def update(self):
        self.gui.moveID(self.pos_x, self.pos_y, self.id, self.taille)
