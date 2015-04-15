# Créé par Cyprien, le 11/12/2014 en Python 3.2

from GUI import *


controleur = Controleur()
gui = GUI(controleur)
controleur.link(gui)
gui.run()


"""
controleur = Controleur()

gui = GUI( controleur )
modele = Modele( controleur )

controleur.link(gui)
controleur.link(modele)

controleur.run()
"""