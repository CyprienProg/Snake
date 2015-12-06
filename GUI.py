# Créé par Cyprien, le 11/12/2014 en Python 3.2
from tkinter import *
from Controleur import *

class GUI:
    def __init__(self, controleur):
        self.__hauteur = 600
        self.__largeur = 800
        self.taille = 25
        self.color_serpent = "green"
        self.color_nourriture = "white"
        self.color_obstacle = "black"

        self.fenetre = Tk()
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height = self.__hauteur, width = self.__largeur)
        self.canvas.pack(padx = 10, pady = 10)
        self.controleur = controleur
        self.fenetre.bind("<Left>", self.controleur.oriente_serpent_left)
        self.fenetre.bind("<Right>", self.controleur.oriente_serpent_right)
        self.fenetre.bind("<Up>", self.controleur.oriente_serpent_up)
        self.fenetre.bind("<Down>", self.controleur.oriente_serpent_down)
        self.fenetre.bind("<Escape>", self.controleur.switch)
        self.id_nourriture = self.canvas.create_oval(0, 0, self.taille, self.taille, fill = self.color_nourriture)
        self.liste_id_corps =[]
        self.liste_id_obstacle = []

    def movement(self):
        self.controleur.move()
        self.controleur.checkEat()
        self.fenetre.after(100, self.movement)

    def run(self):
        self.fenetre.after(100, self.movement)
        self.fenetre.mainloop()

    def moveID(self, pos_x, pos_y, id, taille):
        x0 = pos_x * self.taille + self.taille/2.0 - taille/2.0
        y0 = pos_y * self.taille + self.taille/2.0 - taille/2.0
        x1 = pos_x * self.taille + taille + self.taille/2.0 - taille/2.0
        y1 = pos_y * self.taille + taille + self.taille/2.0 - taille/2.0
        self.canvas.coords(id, x0, y0, x1, y1)

    def afficherSerpent(self):
        li = self.controleur.getListeCorpsSerpent()
        for i in range ( len(li) ):
            pos = li[i].getPosition()
            self.moveID(pos[0], pos[1], self.liste_id_corps[i], self.taille)

    def ajouterID_corps(self, nombre =1):
        for i in range (nombre):
            self.liste_id_corps.append(self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = self.color_serpent))
        self.afficherSerpent()

    def afficherNourriture(self):
        pos = self.controleur.getPositionNourriture()
        self.moveID(pos[0], pos[1], self.id_nourriture, self.taille/2)

    def switchToMenu(self):
        self.canvas_menu.pack()

    def afficherObstacle(self):
        liste_pos = self.controleur.getPositionObstacles()
        for i in range (len(liste_pos)):
            pos = liste_pos[i]
            self.moveID(pos[0], pos[1], self.liste_id_obstacle[i], self.taille)

    def ajouterID_obstacles(self, nombre =1):
        for i in range (nombre):
            self.liste_id_obstacle.append(self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = self.color_obstacle))
        self.afficherObstacle()



