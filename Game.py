# Créé par Haccuria, le 06/12/2015 en Python 3.2
from Client import *
class Jeu:
    def __init__(self, client):
        client = Client()

    def deplacerJoueur (self, nom, pos):
        joueurs[nom].set_position(pos)

    def apparitionNourriture(self, pos):
        nourriture.set_position(pos)

    def set_obstacles(self, pos, value):
        map.set_obstacles(pos, value)

    def newPlayer(self, name, pos, color, length):
        joueurs[name] = Joueur(name, pos, color, length)


