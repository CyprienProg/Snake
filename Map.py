# Créé par Cyprien, le 11/12/2014 en Python 3.2
class Map:

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.map =[]
        self.setsize(longueur, largeur)


    def setsize(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.map = []
        for y in range(self.largeur):
            self.map.append([])
            for x in range(self.longueur):
                self.map[y].append(Case())

    def getLargeur(self):
        return self.largeur

    def getLongueur(self):
        return self.longueur

    def get(self, x, y):
        return map[x][y]
