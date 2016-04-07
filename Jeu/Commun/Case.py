# Créé par Haccuria, le 17/04/2015 en Python 3.2

class Case:
    def __init__(self):
        self.obstacle = False

    def get_obstacle(self):
        return self.obstacle

    def set_obstacle(self, valeur):
        self.obstacle = valeur
