# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from random import *


class GUI:
    def __init__(self, largeur, hauteur):
        self.fenetre = Tk()
        self.__hauteur = hauteur
        self.__largeur =largeur
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height = self.__hauteur, width = self.__largeur)
        self.canvas.pack(padx = 10, pady = 10)
        self.var = "Down"

        self.map = Map(self.canvas, 31, 23, 25)

        self.nourriture = Nourriture(self.canvas, self.map, 100, 100, 10)
        self.serpent = Serpent(self.canvas, self.map)
        self.fenetre.bind("<Left>", self.go_left)
        self.fenetre.bind("<Right>", self.go_right)
        self.fenetre.bind("<Up>", self.go_up)
        self.fenetre.bind("<Down>", self.go_down)
        self.nourriture.nouvellePosition()


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


class Corps:
    def __init__(self, canvas, map, pos_x, pos_y, taille, couleur = "green"):
        self.taille = taille
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.canvas = canvas
        self.map = map
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = self.couleur)
        self.setposition(pos_x, pos_y)

    def move_left(self):
        self.pos_x -= 1
        self.update()

    def move_right(self):
        self.pos_x += 1
        self.update()

    def move_up(self):
        self.pos_y -= 1
        self.update()

    def move_down(self):
        self.pos_y += 1
        self.update()

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def setposition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.update()

    def update(self):
        self.map.updateposition(self.pos_x, self.pos_y, self.id, self.taille)

class Serpent:
    taille = 25
    pos_x = 0
    pos_y = 0
    def __init__(self, canvas, map):
        self.liste = []
        self.canvas = canvas
        self.map = map
        for i in range (3):
            corps = Corps(self.canvas, self.map, self.pos_x + i, self.pos_y, self.taille)
            self.liste.append(corps)

    def go_left(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0]-1, pos[1])
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_right(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0]+1, pos[1])
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_up(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0], pos[1]-1)
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def go_down(self):
        dernier_corps = self.liste.pop()
        self.liste.insert(0, dernier_corps)
        pos = self.liste[1].getposition()
        pos = (pos[0], pos[1]+1)
        dernier_corps.setposition(pos[0], pos[1])
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def possible_left(self):
        pos = self.liste[0].getposition()
        pos = (pos[0]-1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_right(self):
        pos = self.liste[0].getposition()
        pos = (pos[0]+1, pos[1])
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_up(self):
        pos = self.liste[0].getposition()
        pos = (pos[0], pos[1]-1 )
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def possible_down(self):
        pos = self.liste[0].getposition()
        pos = (pos[0], pos[1]+1 )
        for corps in self.liste:
            pos_corps = corps.getposition()
            if pos[0] == pos_corps[0] and pos[1] == pos_corps[1] :
                return False
        return True

    def getposition(self):
        return (self.pos_x, self.pos_y)

class Nourriture:
    def __init__(self, canvas, map, pos_x, pos_y, taille, couleur = "white"):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.couleur = couleur
        self.taille = taille
        self.canvas = canvas
        self.map = map
        self.id = self.canvas.create_oval(0, 0, self.taille, self.taille, fill = self.couleur)
        self.setposition(pos_x,pos_y)

    def nouvellePosition(self):
        x = randint(0, self.map.getlongueur())
        y = randint(0, self.map.getlargeur())
        self.setposition(x,y)

    def getposition(self):
        return (self.pos_x, self.pos_y)

    def setposition(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map.updateposition(self.pos_x, self.pos_y, self.id, self.taille)

class Map:
    def __init__(self, canvas, longueur, largeur, taille):
        self.canvas = canvas
        self.longueur = longueur
        self.largeur = largeur
        self.map =[]
        self.taille = taille
        self.setsize(longueur, largeur)


    def setsize(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.map = []
        for y in range(self.largeur):
            self.map.append([])
            for x in range(self.longueur):
                self.map[y].append(0)

    def afficher(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                print(self.map[x][y], end=" ")
            print()

    def updateposition (self, pos_x, pos_y, id, taille):
        x0 = pos_x * self.taille + self.taille/2.0 - taille/2.0
        y0 = pos_y * self.taille + self.taille/2.0 - taille/2.0
        x1 = pos_x * self.taille + taille + self.taille/2.0 - taille/2.0
        y1 = pos_y * self.taille + taille + self.taille/2.0 - taille/2.0
        self.canvas.coords(id, x0, y0, x1, y1)

    def getlargeur(self):
        return self.largeur

    def getlongueur(self):
        return self.longueur




x = GUI(800,600)
x.run()