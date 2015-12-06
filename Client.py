# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect(('localhost', 33033))           #localhost = 127.0.0.1
            print("Connexion réussie")
        except socket.error:
            print ("La connexion a échouée.")
            sys.exit()

class EnvoiMessage(threading.Thread):
    def __init__(self, socket, message):
        threading.Thread.__init__(self)
        self.socket = socket
        self.message = message

    def run(self):
        self.socket.send(self.message.encode("Utf8"))

class ReceptionMessage(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        while 1:
            message = self.socket.recv(1024).decode("Utf8")
            print(message)

if "__main__" == __name__:
    client=Client()

    recoitM = ReceptionMessage(client.socket)
    recoitM.start()

    while 1:
        envoiM = EnvoiMessage(client.socket, input(""))
        envoiM.start()

