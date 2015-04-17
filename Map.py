# Créé par Cyprien, le 11/12/2014 en Python 3.2
from Case import *

class Map:

    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.liste_obstacles = []
        self.map =[]
        self.setsize(longueur, hauteur)


    def setsize(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.map = []
        for x in range(self.longueur):
            self.map.append([])
            for y in range(self.hauteur):
                self.map[x].append(Case())

    def getHauteur(self):
        return self.hauteur

    def getLongueur(self):
        return self.longueur

    def get(self, x, y):
        return self.map[x][y]

    def set_obstacle(self, x, y, valeur):
        case = self.get(x, y)
        case.set_obstacle(valeur)
        if valeur :
            self.liste_obstacles.append((x, y))
        else:
            self.liste_obstacles.remove((x, y))

    def is_obstacle(self):
        case = self.get(x, y)
        return case.get_obstacle()

    def getPositionObstacles(self):
        return self.liste_obstacles

    def obstacles_contains(self, x, y):
        return (x,y) in self.liste_obstacles

    def loadMatrice(self, matrice):
        longueur = len(matrice[0])
        hauteur = len(matrice)
        self.setsize(longueur, hauteur)
        nbObstacles = 0
        for x in range (longueur):
            for y in range (hauteur):
                if matrice[x][y] == 1:
                    self.set_obstacle(x, y, True)
                    nbObstacles += 1
        return nbObstacles



