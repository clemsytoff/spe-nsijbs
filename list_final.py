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

    def estVide(self): # retourne un booleen
        return self.tete is None and self.reste is None 

    def obtenirTete(self):
        if self.estVide():
            raise ValueError("La liste est vide")
        return self.tete

    def resteListe(self):
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


    #ajouter un element a la fin d'une liste
    def ajouter_fin(self, val) -> None:
        if self.estVide():
            # Si la liste est vide, on modifie la tête et le reste
            self.modifTete(val)
            self.modifReste(Liste.consVide())
        else:
            current = self
            # On parcourt la liste jusqu'à atteindre la fin
            while not current.reste.estVide():
                current = current.resteListe()
            # Insérer à la fin
            current.modifReste(Liste.cons(val, Liste.consVide()))


#--------main---------

def afficher_liste(liste):
    if not isinstance(liste, Liste):
        raise ValueError("Ce n'est pas une liste chaînée")
    
    if liste.estVide():
        print("La liste est vide")
        return

    while not liste.estVide():
        print(liste.obtenirTete())
        liste = liste.resteListe()


def taille_liste(liste):
    if not isinstance(liste, Liste):
        raise ValueError("Ce n'est pas une liste chaînée")
    
    if liste.estVide():
        print("La liste est vide")
        return 0

    n = 0
    while not liste.estVide():
        n += 1
        liste = liste.resteListe()

    return n

    
def trouver_element(liste,element):
    if not isinstance(liste, Liste):
        raise ValueError("Ce n'est pas une liste chaînée")
    
    if liste.estVide():
        print("La liste est vide")
        return False
    
    while not liste.estVide():
        if element == liste.tete:
            return True
        liste = liste.reste

    return False


def somme_liste(liste):
    if not isinstance(liste, Liste):
        raise ValueError("Ce n'est pas une liste chaînée")
    
    if liste.estVide():
        print("La liste est vide")
        return 0
    
    s = 0
    while not liste.estVide():
        s += liste.obtenirTete()
        liste = liste.resteListe()
    
    return s

def find_and_replace(liste, a_trouver, a_remplacer):
    if not isinstance(liste, Liste):
        raise ValueError("Ce n'est pas une liste chaînée")
    
    if liste.estVide():
        print("La liste est vide")
        return

    current = liste
    while not current.estVide():
        if current.obtenirTete() == a_trouver:
            current.modifTete(a_remplacer)
        current = current.resteListe()


def inverser_liste(L):
    if not isinstance(L,Liste):
        return ValueError("L n'est pas une liste")

    if L.estVide() and L.reste.estVide():
        print("L est vide ")
    
    
    L_res = Liste.consVide() # creer une nouvelle liste
    
    while not L.estVide():
        L_res = Liste.cons(L.tete,L_res)
        L = L.reste

    return L_res


def fusion(L1: Liste, L2: Liste) -> Liste:
    if L1.estVide():
        return L2
    if L2.estVide():
        return L1
    
    # Créer une nouvelle liste pour stocker le résultat
    current_L1 = L1
    resultat = Liste.cons(current_L1.obtenirTete(), Liste.consVide())
    current_result = resultat

    # Parcourir L1 et ajouter ses éléments à la nouvelle liste
    current_L1 = current_L1.resteListe()
    while not current_L1.estVide():
        current_result.modifReste(Liste.cons(current_L1.obtenirTete(), Liste.consVide()))
        current_result = current_result.resteListe()
        current_L1 = current_L1.resteListe()

    # Parcourir L2 et ajouter ses éléments à la nouvelle liste
    current_L2 = L2
    while not current_L2.estVide():
        current_result.modifReste(Liste.cons(current_L2.obtenirTete(), Liste.consVide()))
        current_result = current_result.resteListe()
        current_L2 = current_L2.resteListe()

    return resultat

#filtrer
def filtre(L: Liste, condition) :
    resultat = Liste.consVide()
    current = L
    
    # Parcours de la liste
    while not current.estVide():
        if condition(current.tete):
            resultat = Liste.cons(current.obtenirTete(), resultat)
        current = current.resteListe()

    # Inverser la liste pour la remettre dans l'ordre
    resultat_reverse = inverser_liste(resultat)
   

    return resultat_reverse


def supprime(L: Liste, val) -> Liste:
    if L.estVide():
        return L
    
    # Créer une nouvelle liste pour stocker le résultat
    nouvelle_liste = Liste.consVide()
    courant = L
    
    # Parcourir la liste d'origine
    while not courant.estVide():
        if courant.tete != val:
            nouvelle_liste = Liste.cons(courant.tete, nouvelle_liste)
        else:
            # Ignorer la première occurrence de val
            courant = courant.reste
            break
        courant = courant.reste
    
    # Ajouter le reste de la liste après la suppression
    while not courant.estVide():
        nouvelle_liste = Liste.cons(courant.tete, nouvelle_liste)
        courant = courant.reste
    
    # Inverser la liste pour obtenir l'ordre correct
    resultat =  inverser_liste(nouvelle_liste)
    
    return resultat


#trouver la valeur maximale de la liste:
def maxlist(L):
    if not isinstance(L,Liste):
        return ValueError("L n'est pas une liste")

    if L.estVide() and L.reste.estVide():
        print("L est vide ")
    
    maxi = L.tete
    while not L.estVide():    
        if L.tete > maxi:
            maxi = L.tete
        L = L.reste
        
    return maxi


# Test du code
maliste = Liste.consVide()
maliste = Liste.cons(3, maliste)
maliste = Liste.cons(2, maliste)
maliste = Liste.cons(1, maliste)

l2 = Liste.consVide()
l2 =  Liste.cons(6, l2)
l2 =  Liste.cons(5, l2)
l2 =  Liste.cons(4, l2)

print("L1")
afficher_liste(maliste)

print("L2")
afficher_liste(l2)

r = fusion(maliste,l2)
print("L1 + L2")
afficher_liste(r) 

# Exemple de condition : on veut filtrer les éléments pairs
def est_pair(x):
    return x % 2 == 0

# Appel de la fonction filtre avec la condition "est_pair"
f = filtre(r, est_pair)
print("filtered : ")
afficher_liste(f)

print("taille : ",taille_liste(f))

f.ajouter_fin(9)
afficher_liste(f)