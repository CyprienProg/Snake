# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *
from Controleur import *
from GUI import *

class Nourriture:
    def __init__(self, canvas, controleur, gui, pos_x, pos_y, taille, couleur = "white"):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.couleur = couleur
        self.taille = taille
        self.canvas = canvas
        self.controleur = controleur
        self.gui = gui
        self.id = self.canvas.create_oval(0, 0, self.taille, self.taille, fill = self.couleur)
        self.setposition(pos_x,pos_y)

    def nouvellePosition(self):
        x = randint(0, self.controleur.getLongueurMap())
        y = randint(0, self.controleur.getLargeurMap())
        self.setposition(x,y)

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def setposition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.gui.moveID(self.pos_x, self.pos_y, self.id, self.taille)
