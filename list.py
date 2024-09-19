class Liste:
    def __init__(self, tete=None, reste=None):
        self.tete = tete
        self.reste = reste


    @staticmethod
    def consVide():
        return Liste()

    @staticmethod
    def cons(e, lst):
        return Liste(e, lst)

    def estVide(self):
        return self.tete is None and self.reste is None

    def tete(self):
        if self.estVide():
            raise ValueError("La liste est vide")
        return self.tete

    def reste(self):
        if self.estVide():
            raise ValueError("La liste est vide")
        return self.reste

    def modifTete(self, val):
        if self.estVide():
            raise ValueError("La liste est vide")
        self.tete = val

    def modifReste(self, new_reste):
        if self.estVide():
            raise ValueError("La liste est vide")
        self.reste = new_reste

#-------------main--------------
def afficher_liste(L):
    if not isinstance(L,Liste):
        print("L n'est pas une liste")
        return
    
    if L.estVide():
        print("L est une liste vide")
    
    while not L.estVide() and not L.reste.estVide() :
        print(L.tete)
        L = L.reste# Créer une liste vide
ma_liste = Liste.consVide()

# Ajouter des éléments
ma_liste = Liste.cons(3, ma_liste)
ma_liste = Liste.cons(2, ma_liste)
ma_liste = Liste.cons(1, ma_liste)

# Afficher les éléments de la liste
print(ma_liste.tete)  # Affiche 1
print(ma_liste.reste.tete)  # Affiche 2
print(ma_liste.reste.reste.tete)  # Affiche 3

# Modifier la tête de la liste
ma_liste.modifTete(10)
print(ma_liste.tete)  # Affiche 10

# Modifier le reste de la liste
ma_liste.modifReste(Liste.cons(20, Liste.cons(30, Liste.consVide())))
print(ma_liste.reste.tete)  # Affiche 20
print(ma_liste.reste.reste.tete)  # Affiche 30
