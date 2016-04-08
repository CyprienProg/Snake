# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading
from Interface import *
import json
from FileMap import *
from Serpent import *
import sys
sys.path.append("../Commun")
from Map import *

class Serveur(threading.Thread):
    def __init__(self, interface):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.interface = interface

        self.map = Map(1,1)
        file = FileMap()
        matrice = file.loadFromFile("map.txt")
        valeur = self.map.loadMatrice(matrice)
        self.running = True
        self.updateMovement()           #Faire classe thread

        #valeurs


    def run(self):
        try:
            self.socket.bind(('',33033))
            print("Serveur connecté, attente de player...")
            self.running = True
            while self.running:
                self.socket.listen(3)
                socket, adresse = self.socket.accept()
                print("Player connecté, adresse IP", adresse[0],", port",adresse[1])
                player = Player(socket, self, self.interface)
                pos = self.map.getRandomFree(3)
                player.setPosition(pos[0], pos[1])
                nom = player.getName()
                self.sockets[nom]=player
                player.start()
                self.interface.updatePlayers()                
                                                             
        except:
            print("La liaison du socket a été interrompue.")
            self.running = False
            self.socket.close()
            print ("Unexpected error:", sys.exc_info())

    def updateMovement(self):
        liste_pos = []
        for name in self.sockets:
            player = self.sockets[name]
            player.updateMovement()
            liste_pos.append(player.getPosition())

        self.send("all", "update players", liste_pos)
        if (self.running):
            self.interface.fenetre.after(200, self.updateMovement)
    
    def isrunning(self):
        return self.running

    def getSizeConnected(self):
        return len(self.sockets)

    def stop(self):
        self.running = False
        self.socket.close()

    def analyse(self, name, message):
        message = json.loads(message)
        if message["type"] == "load map":
            obstacles = self.map.getPositionObstacles()
            data = {"width" : self.map.getLongueur(), "height": self.map.getHauteur(), "numbers":len(obstacles), "obstacles":obstacles}
            self.send(name, "load map", data)
        else:
            print("Type inconnu", message["type"], message["data"])

    def send(self, name, types, data = ""):
        message = {}
        message["type"] = types
        message["data"] = data
        message = json.dumps(message)
        if name == "all":
            for name in self.sockets:
                self.sockets[name].socket.send(message.encode("Utf8"))
        else:
            self.sockets[name].socket.send(message.encode("Utf8"))

    def playerDeconnecte(self, name):
        self.sockets.pop(name)
        print ("Player", name,"déconnecté")
        self.interface.updatePlayers()

class Player(threading.Thread):                 #Couper écoute
    def __init__(self, socket, serveur, interface):
        threading.Thread.__init__(self)
        self.socket = socket
        self.interface = interface
        self.serveur = serveur

        self.serpent = Serpent()

    def setPosition(self, x, y):
        self.serpent.setPosition(x, y)

    def getPosition(self):
        return self.serpent.getPosition()

    def updateMovement(self):
        self.serpent.updateMovement()

    def run(self):
        thread_name = self.getName()
        stop = False
        while not stop:
            try :
                message = self.socket.recv(1024).decode("Utf8")
                if not message or message.upper() == "FIN":
                    break
                else:
                    self.serveur.analyse(thread_name, message)
            except socket.error:
                stop = True
                self.serveur.playerDeconnecte(thread_name)

    def __del__(self):
        self.socket.close()





