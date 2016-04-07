# Créé par Haccuria, le 13/04/2015 en Python 3.2
from random import *
from Nourriture import *
from Serpent import *
from Map import *
from GUI import *
from FileMap import *


class Controleur:

    def __init__(self):
        self.map = Map(31, 23)
        self.nourriture = Nourriture()
        self.serpent = Serpent()
        self.oriente = "Down"
        self.vie = True

    def initialize(self):
        self.serpent.setPosition(5,5, "Left")
        self.gui.ajouterID_corps(3)
        self.nouvellePositionNourriture()
        file = FileMap()
        matrice = file.loadFromFile("map.txt")
        valeur = self.map.loadMatrice(matrice)
        self.gui.ajouterID_obstacles(valeur)

    def getPositionBlock(self):
        return self.block.getPosition()

    def getLongueurMap(self):
        return self.map.getLongueur()

    def getHauteurMap(self):
        return self.map.getHauteur()

    def getPositionSerpent(self):
        return self.serpent.getPosition()

    def getPositionNourriture(self):
        return self.nourriture.getPosition()

    def checkEat(self):
        if self.nourriture.getPosition() == self.serpent.getPosition():
            self.serpent.agrandir(1)
            self.gui.ajouterID_corps()
            self.nouvellePositionNourriture()



    def getRandom(self, start, end):
        return randint(start, end)

    def getRandomFree(self):        #Trop aléatoire, DANGER !
        pos = (self.getRandom(0, self.getLongueurMap()-1), self.getRandom(0, self.getHauteurMap()-1))
        while self.checkCollision(pos[0], pos[1]):
            pos = (self.getRandom(0, self.getLongueurMap()), self.getRandom(0, self.getHauteurMap()))
        return pos

    def serpent_goLeft(self):
        self.serpent.move_left(self.getLongueurMap())

    def serpent_goRight(self):
        self.serpent.move_right(self.getLongueurMap())

    def serpent_goUp(self):
        self.serpent.move_up(self.getHauteurMap())

    def serpent_goDown(self):
        self.serpent.move_down(self.getHauteurMap())

    def nouvellePositionNourriture(self):
        pos = self.getRandomFree()
        self.nourriture.setPosition(pos[0], pos[1])
        self.gui.afficherNourriture()

    def link(self, gui):
        self.gui = gui
        self.initialize()



    def getListeCorpsSerpent(self):
        return self.serpent.getListeCorps()


    def move (self):
        if self.vie:
            if self.oriente == "Left":
                if self.possible_left():
                    self.serpent_goLeft()
                else:
                    self.serpentMort()
            elif self.oriente == "Right":
                if self.possible_right():
                    self.serpent_goRight()
                else :
                    self.serpentMort()
            elif self.oriente == "Up":
                if self.possible_up():
                    self.serpent_goUp()
                else :
                    self.serpentMort()
            elif self.oriente == "Down":
                if self.possible_down():
                    self.serpent_goDown()
                else :
                    self.serpentMort()
            self.gui.afficherSerpent()
            self.gui.afficherNourriture()
        else:
            print("Mort")

    def possible_left(self):
        pos = self.serpent.getPosition()
        pos = (pos[0]-1, pos[1])
        return not self.checkCollision(pos[0], pos[1])

    def possible_right(self):
        pos = self.serpent.getPosition()
        pos = ((pos[0]+1) %self.getLongueurMap(), pos[1])
        return not self.checkCollision(pos[0], pos[1])

    def possible_up(self):
        pos = self.serpent.getPosition()
        pos = (pos[0], pos[1]-1 )
        return not self.checkCollision(pos[0], pos[1])

    def possible_down(self):
        pos = self.serpent.getPosition()
        pos = (pos[0], (pos[1]+1)%self.getHauteurMap() )
        return not self.checkCollision(pos[0], pos[1])

    def oriente_serpent_left(self, event):
        if self.oriente != "Right":
            self.set_var("Left")

    def oriente_serpent_right(self, event):
        if self.oriente != "Left":
            self.set_var("Right")

    def oriente_serpent_up(self, event):
        if self.oriente != "Down":
            self.set_var("Up")

    def oriente_serpent_down(self, event):
        if self.oriente != "Up":
            self.set_var("Down")

    def set_var(self, var):
        self.oriente = var

    def checkCollision_corps(self, pos_x, pos_y):
        return self.serpent.contains(pos_x, pos_y)

    def switch(self, event):
        self.gui.switchToMenu()

    def getPositionObstacles(self):
        liste_pos = self.map.getPositionObstacles()
        return liste_pos

    def ajouterObstacles(self, x, y, valeur):
        self.map.set_obstacle(x, y, valeur)
        self.gui.ajouterID_obstacles()


    def checkCollision_obstacles(self, x, y):
        return self.map.obstacles_contains(x, y)

    def checkCollision(self, x, y):
        return self.checkCollision_corps(x, y) or self.checkCollision_obstacles(x, y)

    def serpentMort(self):
        self.vie = False




