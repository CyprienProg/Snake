# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading

class Client(threading.Thread):
    def __init__(self, ip, port, name):
        threading.Thread.__init__(self)
        self.ip = str(ip)
        self.port = int(port)
        self.name = str(name)
        

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip, self.port))           #localhost = 127.0.0.1
            return True
        except socket.error:
            return False



































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

