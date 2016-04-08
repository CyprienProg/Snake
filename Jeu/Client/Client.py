# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading
import json


class Client(threading.Thread):
    def __init__(self, ip, port, name, controller):
        threading.Thread.__init__(self)
        self.ip = str(ip)
        self.port = int(port)
        self.name = str(name)
        self.controller = controller
        self.running = False
        

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))           #localhost = 127.0.0.1
            return True
        except socket.error:
            return False
    def get_map(self):
        self.send("load map")

    def run(self):
        self.running = True
        while self.running:
            try :
                message = self.socket.recv(1024).decode("Utf8")
                if not message or message.upper() == "FIN":
                    self.stop()
                else:
                    self.analyse(message)
            except socket.error:
                self.stop()
                print("Le client est déconnecté")

    def analyse(self, message):
        message = json.loads(message)

        if message["type"] == "load map":
            self.controller.frames["Jeu"].set_map( message["data"] )
        else:
            print("Type inconnu", message["type"], message["data"])

    def send(self, types, data = ""):
        message = {}
        message["type"] = types
        message["data"] = data
        message = json.dumps(message)
        self.socket.send(message.encode("Utf8"))
        

    def stop(self):
        self.running = False
























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

