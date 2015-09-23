# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect(('localhost', 33033))           #localhost = 127.0.0.1
            print("Connexion réussie")
        except socket.error:
            print ("La connexion a échouée.")
            sys.exit()
if "__main__" == __name__:
    client=Client()

