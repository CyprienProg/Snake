# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *

class Map:
    def __init__(self, canvas, longueur, largeur, taille):
        self.canvas = canvas
        self.longueur = longueur
        self.largeur = largeur
        self.map =[]
        self.taille = taille
        self.setsize(longueur, largeur)


    def setsize(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.map = []
        for y in range(self.largeur):
            self.map.append([])
            for x in range(self.longueur):
                self.map[y].append(0)

    def afficher(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                print(self.map[x][y], end=" ")
            print()

    def updateposition (self, pos_x, pos_y, id, taille):
        x0 = pos_x * self.taille + self.taille/2.0 - taille/2.0
        y0 = pos_y * self.taille + self.taille/2.0 - taille/2.0
        x1 = pos_x * self.taille + taille + self.taille/2.0 - taille/2.0
        y1 = pos_y * self.taille + taille + self.taille/2.0 - taille/2.0
        self.canvas.coords(id, x0, y0, x1, y1)

    def getlargeur(self):
        return self.largeur

    def getlongueur(self):
        return self.longueur
