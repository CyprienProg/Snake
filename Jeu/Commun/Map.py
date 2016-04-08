# Créé par Cyprien, le 11/12/2014 en Python 3.2
from Case import *
from random import *

class Map:

    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.liste_obstacles = []
        self.map =[]
        self.setsize(longueur, hauteur)

    def getRandomFree(self, space=0):
        found = False
        while not found:
            x = randint(0, self.longueur)
            y = randint(0, self.hauteur)
            if self.__isFree(x, y, space):
                found = True
        return (x, y)
    
    def __isFree(self,x, y, space):
        for i in range(x, (x+space)%self.longueur):
            if self.is_obstacle(self.correctCoord(i, y)):
                return False
        for i in range(x-space, x):
            if self.is_obstacle(self.correctCoord(i, y)):
                return False
        for i in range(y, y+space):
            if self.is_obstacle(self.correctCoord(x, i)):
                return False
        for i in range(y-space, y):
            if self.is_obstacle(self.correctCoord(x, i)):
                return False
        return True

    def correctCoord(self, x, y):
        if x>=0:
            x = x % self.longueur
        else:
            x = self.longueur + x
        if y>=0:
            y = y % self.hauteur
        else:
            y = self.hauteur + y
        return (x,y)
            

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

    def is_obstacle(self, pos):
        case = self.get(pos[0], pos[1])
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
        for i in range (hauteur):
            for j in range (longueur):
                if matrice[i][j] == 1:
                    self.set_obstacle(j, i, True)
                    nbObstacles += 1
        return nbObstacles







        



