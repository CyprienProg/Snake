from Client import *
from Jeu import *

TITLE_FONT = ("Helvetica", 18, "bold")

class Interface(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.client = None

        self.frames = {}
        for F in (Menu, LogIn, Chargement, Jeu, Option, Editeur):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        if self.client != None:
            self.client.stop()
        self.destroy()


class Menu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Menu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Jouer en ligne",
                            command=lambda: controller.show_frame("LogIn"))
        button2 = Button(self, text="Options",
                            command=lambda: controller.show_frame("Option"))
        button3 = Button(self, text="Editeur", command=lambda: controller.show_frame("Editeur"))
        button1.pack()
        button2.pack()
        button3.pack()


class LogIn(Frame):

    def __init__(self, parent, controller): 
        Frame.__init__(self, parent)
        self.controller = controller
        
        self.entryIP = Entry(self)
        self.entryIP.grid(row = 0, column = 1, columnspan = 2)
        
        self.msgIP = Label(self, text ="Adresse IP")
        self.msgIP.grid(row = 0, column = 0)
        
        self.entryPort = Entry(self)
        self.entryPort.grid(row = 1, column = 1, columnspan = 2)
        
        self.msgPort = Label(self, text = "Port")
        self.msgPort.grid(row = 1, column = 0)
        
        self.entryName = Entry(self)
        self.entryName.grid(row = 2, column = 1, columnspan = 2)

        self.msgName = Label(self, text = "Identifiant")
        self.msgName.grid(row = 2, column = 0)
        
        self.bou_salon = Button(self, text = "Connexion", command = self.connexion)
        self.bou_salon.grid(row = 3, column = 1)

        button = Button(self, text="Retour",
                           command=lambda: controller.show_frame("Menu"))
        button.grid(row=3, column=0)

    def connexion (self, event=None):
        self.controller.show_frame("Chargement")
        self.update()
        self.controller.client = Client(self.entryIP.get(), self.entryPort.get(), self.entryName.get(), self.controller)
        if(self.controller.client.connect()):
            self.controller.show_frame("Jeu")
            self.controller.client.start()
            self.controller.frames["Jeu"].initialisation()
        else:
            self.controller.client = None
            self.controller.show_frame("LogIn")
            self.message = Label(self, text = "Erreur de connexion !")
            self.message.grid(row=4)
        

class Chargement(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Patientez...", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)



class Option(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Les options", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Aller au menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

class Editeur(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text = "Editeur de jeu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady =10)
        button = Button(self, text = "Aller au menu", command=lambda : controller.show_frame("Menu"))
        button.pack()



        
