class Produit:
    def __init__(self,nom,prix,quantité):
        self.nom = nom
        self.prix = prix
        self.quantité = quantité
    
    def infos(self):
        print("Nom: " + str(self.nom) + " Prix: " + str(self.prix) + " Quantité: " + str(self.quantité))


class Magasin:
    def __init__(self):
        self.inventaire = {}

    def ajouter(self,produit):
        self.inventaire[produit.nom]=produit

    def supprimer(self,nom):
        for cle in self.inventaire.keys():
            if cle == nom:
                del self.inventaire[cle]
                break
    
    def chercher(self,nom):
        for cle in self.inventaire.keys():
            if cle == nom:
                print(self.inventaire[cle].infos())
    
    def tous(self):
        for i in self.inventaire.values():
            i.infos()






p1 = Produit("Coca",5,"85")
p2 = Produit("Cahier",2,"75")
p3 = Produit("Pomme",1,"25")
#p1.infos()

m1=Magasin()
m1.ajouter(p1)
m1.ajouter(p2)
m1.ajouter(p3)
#m1.supprimer("Coca")
#m1.chercher("Coca")
m1.tous()
