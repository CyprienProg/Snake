from tkinter import *
from Client import *

class Interface:
    def __init__(self):
        self.client = None
        self.fenetre = Tk()
        self.entryIP = Entry(self.fenetre)
        self.entryIP.grid(row = 0, column = 1, columnspan = 2)
        self.msgIP = Label(self.fenetre, text ="Adresse IP")
        self.msgIP.grid(row = 0, column = 0)
        self.entryPort = Entry(self.fenetre)
        self.entryPort.grid(row = 1, column = 1, columnspan = 2)
        self.msgPort = Label(self.fenetre, text = "Port")
        self.msgPort.grid(row = 1, column = 0)
        self.bou_jouer = Button(self.fenetre, text = "Jouer", command = self.play)
        self.bou_jouer.grid(row = 2, column = 1)

    def play(self):
        self.bou_jouer.config(state = "disabled")
        self.client = Client(self.entryIP.get(), int(self.entryPort.get()))
        self.client.start()
        #Switch to "page"
        #sur "page" avoir bouton pour revenir sur "menu"
