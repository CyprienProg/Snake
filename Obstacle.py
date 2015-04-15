# Créé par Haccuria, le 15/04/2015 en Python 3.2
from tkinter import *
from random import *
from GUI import *
#from Controleur import *

class Obstacle:
    def __init__(self):             #controleur
        #self.controleur = controleur
        self.pos_x = 0                              #randint(0, self.controleur.getLongueurMap())
        self.pos_y = 0                              #randint(0, self.controleur.getLargeurMap())
        #self.id_block = self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = "black")
        #self.nouvelObstacle(3)

    def getPosition(self):
        return (self.pos_x, self.pos_y)

    def setPosition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        #self.gui.moveID(self.pos_x, self.pos_y, self.id_block, 25)

    #def nouvelObstacle(self, nombre):
        #x = randint(0, self.controleur.getLongueurMap())
        #y = randint(0, self.controleur.getLargeurMap())
        #self.setposition(x,y)



