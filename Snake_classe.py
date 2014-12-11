# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *

class GUI:
    def __init__(self, hauteur, largeur):
        self.fenetre = Tk()
        self.__hauteur = hauteur
        self.__largeur =largeur
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height = self.__hauteur, width = self.__largeur)
        self.canvas.pack(padx = 10, pady = 10)


        self.serpent = Serpent(self.canvas)
        self.fenetre.bind("<Left>", self.serpent.go_left)
        self.fenetre.bind("<Right>", self.serpent.go_right)
        self.fenetre.bind("<Up>", self.serpent.go_up)
        self.fenetre.bind("<Down>", self.serpent.go_down)




    def run(self):
        self.fenetre.mainloop()

class Corps:
    def __init__(self, canvas, pos_x, pos_y, taille):
        self.taille = taille
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille, fill = 'green')

    def move_left(self):
        self.pos_x -= self.taille
        self.canvas.coords(self.id, self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille)

    def move_right(self):
        self.pos_x += self.taille
        self.canvas.coords(self.id, self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille)

    def move_up(self):
        self.pos_y -= self.taille
        self.canvas.coords(self.id, self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille)

    def move_down(self):
        self.pos_y += self.taille
        self.canvas.coords(self.id, self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille)




class Serpent:
    taille = 25
    pos_x = 50
    pos_y = 50
    def __init__(self, canvas):
        self.liste = []
        self.canvas = canvas
        for i in range (5):
            corps = Corps(self.canvas, self.pos_x + self.taille*i, self.pos_y, self.taille)
            self.liste.append(corps)


    def go_left(self, event):
        for body in self.liste:
            body.move_left()

    """
    def go_left(self, event):
        dernier_corps = liste.pop()
        liste.insert(0, dernier_corps)

        x = liste[1].get_x() - self.taille
        y = liste[1].get_y()
        dernier_corps.set_x( x )
        dernier_corps.set_y( y )
    """

    def go_right(self, event):
        for body in self.liste:
            body.move_right()

    def go_up(self, event):
        for body in self.liste:
            body.move_up()

    def go_down(self, event):
        for body in self.liste:
            body.move_down()




















x = GUI(800,600)
x.run()