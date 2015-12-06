# Créé par Haccuria, le 23/09/2015 en Python 3.2
import socket, sys, threading

class Serveur(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        try:
            self.socket.bind(('',33033))
            print("Serveur connecté, attente de client...")
        except socket.error:
            print("La liaison du socket à l'adresse choisie à échouée.")
            sys.exit

    def run(self):
        while 1:
            self.socket.listen(3)
            socket, adresse = self.socket.accept()
            print("Client connecté, adresse IP", adresse[0],", port",adresse[1])
            client = Client(socket, self)
            nom = client.getName()
            self.sockets[nom]=client
            client.start()

    def analyse(self, name, message):
        player = self.players[name]
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
                self.sockets[cle].socket.send(message.encode("Utf8"))

    def send_pos(self, pos):
        print("")


class Client(threading.Thread):         #Couper écoute
    def __init__(self, socket, serv):
        threading.Thread.__init__(self)
        self.socket = socket
        self.serv = serv

    def run(self):
        thread_name = self.getName()
        stop = False
        while not stop:
            try :
                message = self.socket.recv(1024).decode("Utf8")
                if not message or message.upper() == "FIN":
                    break
                else:
                    self.serv.analyse(thread_name, message)
            except socket.error:
                self.serv.sockets.pop(thread_name)
                stop = True

    def __del__(self):
        self.socket.close()
        print ("Client", self.getName(),"déconnecté")


if "__main__" == __name__:
    serv=Serveur()
    serv.run()

