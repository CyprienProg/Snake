from tkinter import *
import sys
sys.path.append("../Commun")
from Map import *

class Jeu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller= controller
        self.data = None
        self.map = None
        self.canvas = Canvas(self, bg = 'dark gray', height = 600, width = 800)
        self.canvas.pack(padx = 10, pady = 10)
        self.liste_id_obstacle=[]
        self.taille = 25
        self.color_obstacle = "black"

        
    def initialisation(self):
        self.data = {self.controller.client.name:{"color":"red", "position":[(1,2)]}}
        self.map = Map(10,10)
        self.controller.client.get_map()
        
    def updateAffichage(self):
        self.afficherObstacle()
        '''
        for name in self.data:
            temp = self.data[name]
            pos = temp["position"]
            color = temp["color"]
            for n in pos:
                self.drawCarre(n, color, name)
                '''
    def set_map(self, dico):
        width = dico["width"]
        height = dico["height"]
        numbers = dico["numbers"]
        obstacles = dico["obstacles"]
        self.map = Map(width, height)
        for i in obstacles:
            self.map.set_obstacle(i[0], i[1], True)
        self.ajouterID_obstacles(numbers)

    def moveID(self, pos_x, pos_y, id, taille):
        x0 = pos_x * self.taille + self.taille/2.0 - taille/2.0
        y0 = pos_y * self.taille + self.taille/2.0 - taille/2.0
        x1 = pos_x * self.taille + taille + self.taille/2.0 - taille/2.0
        y1 = pos_y * self.taille + taille + self.taille/2.0 - taille/2.0
        self.canvas.coords(id, x0, y0, x1, y1)    

    def afficherObstacle(self):
        liste_pos = self.map.getPositionObstacles()
        for i in range (len(liste_pos)):
            pos = liste_pos[i]
            self.moveID(pos[0], pos[1], self.liste_id_obstacle[i], self.taille)

    def ajouterID_obstacles(self, nombre =1):
        for i in range (nombre):
            self.liste_id_obstacle.append(self.canvas.create_rectangle(0, 0, self.taille, self.taille, fill = self.color_obstacle))
        self.afficherObstacle()

    def drawCarre(self, n, color, name):
        print (n, color)
        print (name)
