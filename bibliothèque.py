#créer 2 class : 1 qui représente un livre, 2 qui représente une bibliotheque - titre, pages, auteur - tableau de livres (liste)
#méthode métier pour afficher les détails du lire et la bibli ajouter un livre ajouter et afficher

class Livre:
    def __init__(self,titre,auteur,pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
    
    def infos(self):
        print("Titre : " + str(self.titre) + " , auteur : " + str(self.titre) + " et " + str(self.pages) + " pages.")

class Bibli:
    def __init__(self):
        self.livres = []
    
    def ajouter(self,livre):
        if not isinstance(livre,Livre):
            print("Ce n'est pas un livre.")
            return
        self.livres.append(livre)


    def afficher_livres(self):
        for livre in self.livres:
            livre.afficher()
    

l1 = Livre("machin", "bidule", 45)
l2 =Livre("Big", "Bharat", 233)
l3 =Livre("Time", "Clem", 3)

bib = Bibli()
bib.ajouter(l1)
bib.ajouter(l2)
bib.ajouter(l3)
