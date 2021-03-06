import tkinter as tk   # python3

TITLE_FONT = ("Helvetica", 18, "bold")

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, LogIn, Option, Editeur):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Jouer en ligne",
                            command=lambda: controller.show_frame("LogIn"))
        button2 = tk.Button(self, text="Options",
                            command=lambda: controller.show_frame("Option"))
        button3 = tk.Button(self, text="Editeur", command=lambda: controller.show_frame("Editeur"))
        button1.pack()
        button2.pack()
        button3.pack()


class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.entryIP = tk.Entry(self)
        self.entryIP.grid(row = 0, column = 1, columnspan = 2)
        
        self.msgIP = tk.Label(self, text ="Adresse IP")
        self.msgIP.grid(row = 0, column = 0)
        
        self.entryPort = tk.Entry(self)
        self.entryPort.grid(row = 1, column = 1, columnspan = 2)
        
        self.msgPort = tk.Label(self, text = "Port")
        self.msgPort.grid(row = 1, column = 0)
        
        self.bou_salon = tk.Button(self, text = "Connexion", command = lambda: controller.show_frame("Chargement"))
        self.bou_salon.grid(row = 2, column = 1)
        
        button = tk.Button(self, text="Retour",
                           command=lambda: controller.show_frame("Menu"))
        button.grid(row=2, column=0)


class Chargement(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label

class Salon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Patientez...", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        

class Option(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Les options", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Aller au menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

class Editeur(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text = "Editeur de jeu", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady =10)
        button = tk.Button(self, text = "Aller au menu", command=lambda : controller.show_frame("Menu"))
        button.pack()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
