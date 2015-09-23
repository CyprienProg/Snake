# Créé par Haccuria, le 17/04/2015 en Python 3.2
from GUI import *

class Menu(Canvas):
    def __init__(self, master=None):
        self.__hauteur = 600
        self.__largeur = 800
        Canvas.__init__(self, master, borderwidth = 2)
        self.master.title("Snake")

        self.pack(padx = 10, pady = 10)
        self.bou_play = Button(self, text = "Play !", command = self.play)
        self.bou_opt = Button(self, text = "Options", command = self.option)
        self.bou_edit = Button(self, text = "Editer une map", command = self.edit)
        self.bou_play.pack(side = TOP)
        self.bou_opt.pack()
        self.bou_edit.pack(side = BOTTOM)

    def play(self):
        controleur = Controleur()
        gui = GUI(controleur)
        controleur.link(gui)
        self.destroy()
        gui.run()

    def option(self):
        print("Option")

    def edit(self):
        print("Editer")
