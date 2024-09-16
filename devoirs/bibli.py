class Livre:
    def __init__(self,titre,auteur,date):
        self.titre = titre
        self.auteur = auteur
        self.date = date
    
    def infos(self):
        print("Titre : " + str(self.titre) + " Auteur : " + str(self.auteur) + " Date : " + str(self.date))
    

class Bibliothèque:
    def __init__(self):
        self.collection = []
    
    def ajouter(self,livre):
        self.collection.append(livre)
    
    def supprimer(self,titre):
        for i in self.collection:
            if i.titre == titre:
                self.collection.remove(i)
                break
    
    def chercher(self,titre):
        for i in self.collection:
            if i.titre == titre:
                i.infos()
                break

    def tous(self):
        for i in self.collection:
            i.infos()


l1=Livre("Clem","Clement",2024)
l2=Livre("Djebz","Djebz",2025)
l3=Livre("toto","Bharat",2010)

b1 = Bibliothèque()
b1.ajouter(l1)
b1.ajouter(l2)
b1.ajouter(l3)
b1.tous()
