# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *
from Nourriture import *
from Serpent import *
from Corps import *
from Controleur import *

class GUI:
    def __init__(self, controleur):
        self.fenetre = Tk()
        self.__hauteur = 600
        self.__largeur = 800
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height = self.__hauteur, width = self.__largeur)
        self.canvas.pack(padx = 10, pady = 10)
        self.var = "Down"
        self.taille = 25
        self.controleur = controleur

        self.nourriture = Nourriture(self.canvas, self.controleur, self, 100, 100, 10)
        self.serpent = Serpent(self.canvas, self)
        self.fenetre.bind("<Left>", self.go_left)
        self.fenetre.bind("<Right>", self.go_right)
        self.fenetre.bind("<Up>", self.go_up)
        self.fenetre.bind("<Down>", self.go_down)
        self.nourriture.nouvellePosition()

        self.id_serpent = self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = "blue")



    def go_left(self, event):
        if self.var != "Right" and self.lock == False and self.var != "Left":
            self.set_var("Left")
            self.lock = True

    def go_right(self, event):
        if self.var != "Left" and self.lock == False and self.var != "Right":
            self.set_var("Right")
            self.lock = True

    def go_up(self, event):
        if self.var != "Down" and self.lock == False and self.var != "Up":
            self.set_var("Up")
            self.lock = True

    def go_down(self, event):
        if self.var != "Up" and self.lock == False and self.var != "Down":
            self.set_var("Down")
            self.lock = True

    def set_var(self, var):
        self.var = var

    def move (self):
        if self.var == "Left":
            if self.serpent.possible_left():
                self.serpent.go_left()
                self.controleur.serpent_goLeft()
            else:
                print("Mort")
        elif self.var == "Right":
            if self.serpent.possible_right():
                self.serpent.go_right()
                self.controleur.serpent_goRight()
            else :
                print("Mort")
        elif self.var == "Up":
            if self.serpent.possible_up():
                self.serpent.go_up()
                self.controleur.serpent_goUp()
            else :
                print("Mort")
        elif self.var == "Down":
            if self.serpent.possible_down():
                self.serpent.go_down()
                self.controleur.serpent_goDown()
            else :
                print("Mort")
        self.lock = False
        pos = self.controleur.getPositionSerpent()
        self.moveID(pos[0], pos[1], self.id_serpent, self.taille)

    def movement(self):
        self.move()
        self.checkcollision()
        self.fenetre.after(100, self.movement)

    def run(self):
        self.fenetre.after(100, self.movement)
        self.fenetre.mainloop()

    def checkcollision(self):
        pos_serpent = self.serpent.getposition()
        pos_nourriture = self.nourriture.getposition()
        if pos_serpent == pos_nourriture:
            self.nourriture.nouvellePosition()
            self.serpent.agrandir(1)

    def moveID(self, pos_x, pos_y, id, taille):
        x0 = pos_x * self.taille + self.taille/2.0 - taille/2.0
        y0 = pos_y * self.taille + self.taille/2.0 - taille/2.0
        x1 = pos_x * self.taille + taille + self.taille/2.0 - taille/2.0
        y1 = pos_y * self.taille + taille + self.taille/2.0 - taille/2.0
        self.canvas.coords(id, x0, y0, x1, y1)



