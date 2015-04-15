# Créé par Haccuria, le 13/04/2015 en Python 3.2
from random import *
from Nourriture import *
from Serpent import *
from Map import *
from Obstacle import *
from GUI import *


class Controleur:

    def __init__(self):
        self.map = Map(31, 23)
        self.nourriture = Nourriture()
        self.serpent = Serpent()
        self.block = Obstacle()
        self.oriente = "Down"
        self.serpent.setPosition(5,5, "Left")


    def getPositionBlock(self):
        return self.block.getPosition()

    def getLongueurMap(self):
        return self.map.getLongueur()

    def getLargeurMap(self):
        return self.map.getLargeur()

    def getPositionSerpent(self):
        return self.serpent.getPosition()

    def getPositionNourriture(self):
        return self.nourriture.getPosition()

    def checkEat(self):
        if self.nourriture.getPosition() == self.serpent.getPosition():
            self.serpent.agrandir(1)
            self.gui.ajouterID_corps()
            self.nouvellePositionNourriture()

    def checkCollision(self):
        if self.serpent.getPosition() == self.block.getPosition():
            print ("Mort")

    def getRandom(self, start, end):
        return randint(start, end)

    def getRandomFree(self):        #Trop aléatoire, DANGER !
        pos = (self.getRandom(0, self.getLongueurMap()), self.getRandom(0, self.getLargeurMap()))
        while self.checkCollision_corps(pos[0], pos[1]):
            pos = (self.getRandom(0, self.getLongueurMap()), self.getRandom(0, self.getLargeurMap()))
        return pos

    def serpent_goLeft(self):
        self.serpent.move_left()

    def serpent_goRight(self):
        self.serpent.move_right()

    def serpent_goUp(self):
        self.serpent.move_up()

    def serpent_goDown(self):
        self.serpent.move_down()

    def nouvellePositionNourriture(self):
        pos = self.getRandomFree()
        self.nourriture.setPosition(pos[0], pos[1])
        self.gui.afficherNourriture()

    def link(self, gui):
        self.gui = gui
        self.gui.ajouterID_corps(3)
        self.nouvellePositionNourriture()

    def getListeCorpsSerpent(self):
        return self.serpent.getListeCorps()


    def move (self):
        if self.oriente == "Left":
            if self.possible_left():
                self.serpent_goLeft()
            else:
                print("Mort")
        elif self.oriente == "Right":
            if self.possible_right():
                self.serpent_goRight()
            else :
                print("Mort")
        elif self.oriente == "Up":
            if self.possible_up():
                self.serpent_goUp()
            else :
                print("Mort")
        elif self.oriente == "Down":
            if self.possible_down():
                self.serpent_goDown()
            else :
                print("Mort")
        self.lock = False
        self.gui.afficherSerpent()
        self.gui.afficherNourriture()

    def possible_left(self):
        pos = self.serpent.getPosition()
        pos = (pos[0]-1, pos[1])
        return not self.checkCollision_corps(pos[0], pos[1])

    def possible_right(self):
        pos = self.serpent.getPosition()
        pos = (pos[0]+1, pos[1])
        return not self.checkCollision_corps(pos[0], pos[1])

    def possible_up(self):
        pos = self.serpent.getPosition()
        pos = (pos[0], pos[1]-1 )
        return not self.checkCollision_corps(pos[0], pos[1]) #and not checkCollision_block(pos[0], pos[1])

    def possible_down(self):
        pos = self.serpent.getPosition()
        pos = (pos[0], pos[1]+1 )
        return not self.checkCollision_corps(pos[0], pos[1])

    def oriente_serpent_left(self, event):
        if self.oriente != "Right" and self.lock == False and self.oriente != "Left":
            self.set_var("Left")
            self.lock = True

    def oriente_serpent_right(self, event):
        if self.oriente != "Left" and self.lock == False and self.oriente != "Right":
            self.set_var("Right")
            self.lock = True

    def oriente_serpent_up(self, event):
        if self.oriente != "Down" and self.lock == False and self.oriente != "Up":
            self.set_var("Up")
            self.lock = True

    def oriente_serpent_down(self, event):
        if self.oriente != "Up" and self.lock == False and self.oriente != "Down":
            self.set_var("Down")
            self.lock = True

    def set_var(self, var):
        self.oriente = var

    def checkCollision_corps(self, pos_x, pos_y):
        return self.serpent.contains(pos_x, pos_y)

    def switch(self, event):
        self.gui.switchToMenu()



