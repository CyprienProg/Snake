from tkinter import *
from Map import *

class Jeu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller= controller
        self.data = None
        self.map = None

        
    def initialisation(self):
        self.data = {self.controller.client.name:{"color":"red", "position":[(1,2)]}}
        self.map = Map(10,10)
        self.updateAffichage()
        
    def updateAffichage(self):
        for name in self.data:
            temp = self.data[name]
            pos = temp["position"]
            color = temp["color"]
            for n in pos:
                self.drawCarre(n, color, name)
        self.after(100, self.updateAffichage)



    def drawCarre(self, n, color, name):
        print (n, color)
        print (name)
