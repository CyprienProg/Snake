# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading
from Interface import *
import json
from FileMap import *
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

    def run(self):
        try:
            self.socket.bind(('',33033))
            print("Serveur connecté, attente de client...")
            self.running = True
            while self.running:
                self.socket.listen(3)
                socket, adresse = self.socket.accept()
                print("Client connecté, adresse IP", adresse[0],", port",adresse[1])
                client = Client(socket, self, self.interface)
                nom = client.getName()
                self.sockets[nom]=client
                client.start()
                self.interface.updatePlayers()                
                                                             
        except:
            print("La liaison du socket a été interrompue.")
            self.running = False
            self.socket.close()
            print ("Unexpected error:", sys.exc_info()[0])

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
        '''player = self.players[name]
        if message == "up":
            player.set_movment_up()
        elif message == "down":
            players.set_movment_down()
        elif message == "left":
            players.set_movment_left()
        elif message == "right":
            players.set_movment_right()
        message = nom + " " + message
        for cle in self.sockets:
            if cle != nom:
                self.sockets[cle].socket.send(message.encode("Utf8"))'''

    def send(self, name, types, data = ""):
        message = {}
        message["type"] = types
        message["data"] = data
        message = json.dumps(message)
        self.sockets[name].socket.send(message.encode("Utf8"))
        
    def send_pos(self, pos):
        print("")

    def clientDeconnecte(self, name):
        self.sockets.pop(name)
        print ("Client", name,"déconnecté")
        self.interface.updatePlayers()

class Client(threading.Thread):                 #Couper écoute
    def __init__(self, socket, serveur, interface):
        threading.Thread.__init__(self)
        self.socket = socket
        self.interface = interface
        self.serveur = serveur

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
                self.serveur.clientDeconnecte(thread_name)

    def __del__(self):
        self.socket.close()





