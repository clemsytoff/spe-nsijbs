class Pile:
    
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant
    
    def empiler(self, nouvelle_valeur):
        nouveau_noeud = Pile(self.valeur, self.suivant)  # Sauvegarde l'ancien état de la pile
        self.valeur = nouvelle_valeur  # Attribue la nouvelle valeur en haut de la pile
        self.suivant = nouveau_noeud  # Met à jour le suivant
    
    def depiler(self):
        if self.est_vide():
           # print("La pile est vide!")
            return None
        valeur = self.valeur  # Sauvegarde la valeur actuelle
        self.valeur = self.suivant.valeur if self.suivant else None  # Passe au suivant
        self.suivant = self.suivant.suivant if self.suivant else None  # Met à jour la suite de la pile
        return valeur
        
    def est_vide(self):
        return self.valeur is None  # Si la valeur est None, la pile est vide
    
    def copy_pile(self):
        if self.est_vide():
            return None
        
        copy = Pile(self.valeur,self.suivant)
        return copy
    

def copier_pile_m2(p: Pile) -> Pile :
    p2 = Pile()
    pr = Pile()
    copy = p.copy_pile()

    while not copy.est_vide():
        valeur = copy.depiler()
        p2.empiler(valeur)
    
    while not p2.est_vide():
        valeur = p2.depiler()
        pr.empiler(valeur)
    
    return pr

def afficher_pile(p:Pile):

    copy = p.copy_pile()
    while not copy.est_vide():
        print(copy.valeur,end="->")
        copy.depiler()
    
    print("None")


def inverser_pile(p:Pile) -> Pile :
    copy = p.copy_pile()
    new_pile = Pile()
    while not copy.est_vide():
        valeur = copy.depiler()
        new_pile.empiler(valeur)
        
    
    return new_pile

#exercice : verification de parenthese valide ou pas 
# exemple de parenthese valide -> (2*2)(2x+1) ou bien (2*(2+x))(2x+1)

def verifier_parenthese_valide(chaine : str) -> bool :

    p = Pile()
    for cyril in chaine :
        if cyril == '(':
           p.empiler(cyril)
        elif cyril == ')':
            if p.est_vide() :
                return False
            else :
                p.depiler()


    return p.est_vide()

def profondeur_pile(p:Pile) -> int :

    copy = p.copy_pile()

    count = 0
    while not copy.est_vide():
        count += 1
        copy.depiler()

    return count


def comparer_pile_egales(p1:Pile, p2:Pile) -> bool:

    if p1 == p2 :
        return True

    if p1.est_vide() and not p2.est_vide() or  p2.est_vide() and not p1.est_vide():
        return False

    if profondeur_pile(p1) != profondeur_pile(p2):
        return False

    copy1 = p1.copy_pile()
    copy2 = p2.copy_pile()

    while not copy1.est_vide() and not copy2.est_vide():
        if copy1.valeur != copy2.valeur:
            return False
        
        copy1.depiler()
        copy2.depiler()

    # si on sors de la boucle, cela veut dire que les deux piles sont identiques
    return True

#veifier si une chaine de caractere est un palindrome
def est_palindrome(chaine: str) -> bool :
    p = Pile()
    for titouan in chaine :
        p.empiler(titouan.lower())

    inv = inverser_pile(p)    
    return comparer_pile_egales(p,inv)


def est_croissant_pile(p:Pile) -> bool:
    copy = p.copy_pile()

    while not copy.suivant.est_vide():
        val = copy.depiler()
        val2 = copy.depiler()
        if val > val2:
            return False
    
    return True
#valeur maximale et minimale d'une pile
def min_max_pile(p:Pile) -> Pile :
    copy = p.copy_pile()
    mini = copy.valeur
    maxi = copy.valeur

    while not copy.est_vide():
        valeur = copy.depiler()
        if valeur < mini :
            mini = valeur
        if valeur >  maxi :
            maxi = valeur
    
    return mini, maxi

def convert_tableau_en_pile(tableau: list) -> Pile : 
    pile = Pile()

    count = len(tableau) -1
    while count >= 0 :
        pile.empiler(tableau[count])
        count -= 1

    #only in python pour inverser un tableau
    #for i in tableau[::-1]:
     #   pile.empiler(i)

    return pile

#Exercice 5 : Écrire une fonction switch renvoyant une copie de la pile en inversant ses éléments du sommet et du bas.
def switch_val_pile(p:Pile) -> Pile :
    copy = p.copy_pile()

    new_pile = Pile()
    tab = []

    bas = copy.valeur

    while not copy.suivant.est_vide():
        n = copy.depiler()
        tab.append(n)
    
    haut = copy.valeur
    new_pile.empiler(bas)

    for val in range(1,len(tab)):
        new_pile.empiler(tab[-val])
    
    new_pile.empiler(haut)

    return new_pile

# Exemple d'utilisation
pile = Pile()
pile.empiler(10)
pile.empiler(20)
pile.empiler(30)
afficher_pile(pile)  # Affiche: 30 -> 20 -> 10 -> None

print("------------------------------")
pile = inverser_pile(pile)
afficher_pile(pile)

s = "(2*2)(2x+1)("
print(verifier_parenthese_valide(s))  # Affiche: True

pile_copy = copier_pile_m2(pile)
print("----------pile--------")
afficher_pile(pile)
print("----------pile copy--------")
afficher_pile(pile_copy)


mini, maxi = min_max_pile(pile)
print(mini,maxi)

chaine = "kayak"
if est_palindrome(chaine):
    print(f"La chaine {chaine} est un palindrome")
else :
    print(f"La chaine {chaine} n'est PAS un palindrome")

inv = inverser_pile(pile)
afficher_pile(inv)
print(est_croissant_pile(inv))

tab = [1,2,3,4,5,6,7,8,9,10,"yo"]
ptab = convert_tableau_en_pile(tab)
afficher_pile(ptab)

switch_pile = switch_val_pile(ptab)
afficher_pile(switch_pile)

'''
  -------       -------       -------       ------- 
 | valeur | --> | valeur | --> | valeur | --> None  
 |   30   |     |   20   |     |   10   |           
  -------       -------       -------             
    |             |             |
   Suivant      Suivant        Suivant
    ↓             ↓             ↓
    '''

