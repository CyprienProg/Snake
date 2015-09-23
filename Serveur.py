# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys

class Serveur():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind(('',33033))
            print("Serveur connecté, attente de client...")
        except socket.error:
            print("La liaison du socket à l'adresse choisie à échouée.")
            sys.exit

    def run(self):
        while 1:
            self.socket.listen(2)
            connexion, adresse = self.socket.accept()
            print("Client connecté, adresse IP", adresse[0],", port",adresse[1])


if "__main__" == __name__:
    serv=Serveur()
    serv.run()
