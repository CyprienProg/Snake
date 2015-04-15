# Créé par Haccuria, le 15/04/2015 en Python 3.2
from tkinter import *
from random import *
from GUI import *
#from Controleur import *

class Case:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def getPosition(self):
        return (self.pos_x, self.pos_y)

    def setPosition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y




