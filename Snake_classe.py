# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *

class GUI:
    def __init__(self, hauteur, largeur):
        self.fenetre = Tk()
        self.__hauteur = hauteur
        self.__largeur =largeur
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height = self.__hauteur, width = self.__largeur)
        self.canvas.pack(padx = 10, pady = 10)
        self.var = "Down"

        self.nourriture = Nourriture(self.canvas, 100, 100, 10)
        self.serpent = Serpent(self.canvas)
        self.fenetre.bind("<Left>", self.go_left)
        self.fenetre.bind("<Right>", self.go_right)
        self.fenetre.bind("<Up>", self.go_up)
        self.fenetre.bind("<Down>", self.go_down)

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
            else:
                print("Mort")
        elif self.var == "Right":
            if self.serpent.possible_right():
                self.serpent.go_right()
            else :
                print("Mort")
        elif self.var == "Up":
            if self.serpent.possible_up():
                self.serpent.go_up()
            else :
                print("Mort")
        elif self.var == "Down":
            if self.serpent.possible_down():
                self.serpent.go_down()
            else :
                print("Mort")
        self.lock = False

    def movement(self):
        self.move()
        self.fenetre.after(500, self.movement)

    def run(self):
        self.fenetre.after(500, self.movement)
        self.fenetre.mainloop()

class Corps:
    def __init__(self, canvas, pos_x, pos_y, taille, couleur = "green"):
        self.taille = taille
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.canvas = canvas
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille, fill = self.couleur)

    def move_left(self):
        self.pos_x -= self.taille
        self.update()

    def move_right(self):
        self.pos_x += self.taille
        self.update()

    def move_up(self):
        self.pos_y -= self.taille
        self.update()

    def move_down(self):
        self.pos_y += self.taille
        self.update()

    def get_x(self):
        return self.pos_x

    def get_y(self):
        return self.pos_y

    def set_x(self, x):
        self.pos_x = x
        self.update()

    def set_y(self, y):
        self.pos_y = y
        self.update()

    def update(self):
        self.canvas.coords(self.id, self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille)

class Serpent:
    taille = 25
    pos_x = 50
    pos_y = 50
    def __init__(self, canvas):
        self.liste = []
        self.canvas = canvas
        for i in range (10):
            corps = Corps(self.canvas, self.pos_x + self.taille*i, self.pos_y, self.taille)
            self.liste.append(corps)

    def go_left(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        x = self.liste[1].get_x() - self.taille
        y = self.liste[1].get_y()
        dernier_corps.set_x( x )
        dernier_corps.set_y( y )


    def go_right(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        x = self.liste[1].get_x() + self.taille
        y = self.liste[1].get_y()
        dernier_corps.set_x( x )
        dernier_corps.set_y( y )

    def go_up(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        x = self.liste[1].get_x()
        y = self.liste[1].get_y() - self.taille
        dernier_corps.set_x( x )
        dernier_corps.set_y( y )

    def go_down(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        x = self.liste[1].get_x()
        y = self.liste[1].get_y() + self.taille
        dernier_corps.set_x( x )
        dernier_corps.set_y( y )

    def possible_left(self):
        pos = (self.liste[0].get_x() - self.taille, self.liste[0].get_y())
        for corps in self.liste:
            if pos[0] == corps.get_x() and pos[1] == corps.get_y() :
                return False
        return True

    def possible_right(self):
            pos = (self.liste[0].get_x() + self.taille, self.liste[0].get_y())
            for corps in self.liste:
                if pos[0] == corps.get_x() and pos[1] == corps.get_y() :
                    return False
            return True

    def possible_up(self):
        pos = (self.liste[0].get_x(), self.liste[0].get_y() - self.taille)
        for corps in self.liste:
            if pos[0] == corps.get_x() and pos[1] == corps.get_y() :
                return False
        return True

    def possible_down(self):
        pos = (self.liste[0].get_x(), self.liste[0].get_y() + self.taille)
        for corps in self.liste:
            if pos[0] == corps.get_x() and pos[1] == corps.get_y() :
                return False
        return True

class Nourriture:
    def __init__(self, canvas, pos_x, pos_y, taille, couleur = "white"):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.couleur = couleur
        self.taille = taille
        self.canvas = canvas
        self.id = self.canvas.create_oval(self.pos_x, self.pos_y, self.pos_x+self.taille, self.pos_y+self.taille, fill = self.couleur)



x = GUI(800,600)
x.run()