# Créé par Haccuria, le 13/04/2015 en Python 3.2
from random import *
from Nourrituree import *
from Serpentt import *
from Map import *


class Controleur:

    def __init__(self):
        self.map = Map(31, 23)
        self.nourriture = Nourrituree()
        self.serpent = Serpentt()

    def getLongueurMap(self):
        return self.map.getLongueur()

    def getLargeurMap(self):
        return self.map.getLargeur()

    def getPositionSerpent(self):
        return self.serpent.getPosition()

    def getPositionNourriture(self):
        return self.nourriture.getPosition()

    def checkEat(self):
        if nourriture.getPosition() == serpent.getPosition():
            serpent.agrandir(1)
            nourriture.setPosition(getRandom(0, getLongueurMap()), getRandom(0, getLargeurMap()))

    def getRandom(self, start, end):
        return randint(start, end)

    def serpent_goLeft(self):
        self.serpent.move_left()

    def serpent_goRight(self):
        self.serpent.move_right()

    def serpent_goUp(self):
        self.serpent.move_up()

    def serpent_goDown(self):
        self.serpent.move_down()


