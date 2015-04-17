# Créé par Haccuria, le 17/04/2015 en Python 3.2

class FileMap:

    def __init__(self):
        self.liste = []


    def loadFromFile(self, path):
        fichier = open( path, 'r')
        ligne = fichier.readline()
        while ligne != "":
            self.liste.append( self.changerLignes(ligne) )
            ligne = fichier.readline()
        return self.liste


    def changerLignes(self, ligne):
        listeID = ligne.split(" ")
        listeID.pop()                   # Retire le dernier élément (/n)
        for i in range (len(listeID)):
            listeID[i] = int(listeID[i])
        return listeID
