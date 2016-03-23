from Serveur import *
from tkinter import *
import time

class Interface():
    def __init__(self):
        self.serveur = None
        self.fenetre = Tk()
        self.canvas = Canvas(self.fenetre, bg = 'dark gray', height =600, width =800)
        self.canvas.pack(padx = 10, pady = 10)
        self.number_players = Label(self.fenetre, text = "0 Joueurs")
        self.bou_launch = Button(self.canvas, text = "Launch !", command = self.launch)
        self.bou_launch.pack(side = TOP)
        self.number_players.pack()        


    def launch(self):
        self.bou_launch.config(state="disabled")
        self.serveur = Serveur(self)
        self.serveur.start()
        print("Lancement...")
        time.sleep(3)
        if self.serveur.isrunning():
            self.bou_launch.config(text="Stop !", command = self.stop)
        else:
            self.serveur = None
        self.bou_launch.config(state="normal")


    def stop(self):
        self.bou_launch.config(state="disabled")                            #state="disabled" ne fonctionne pas     
        self.bou_launch.config(text="Launch !", command = self.launch)
        self.serveur.stop()
        self.serveur = None
        self.bou_launch.config(state="normal")                               #pareil
    

    def updatePlayers(self):
        if self.serveur != None:
            #self.number_players.config(text  = "99 Joueurs")
            print(self.serveur.getSizeConnected())
