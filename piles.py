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
    
def comparer_pile_egales(p1:Pile, p2:Pile) -> bool:

    if p1 == p2 :
        return True

    if p1.est_vide() and not p2.est_vide() or  p2.est_vide() and not p1.est_vide():
        return False

    while not p1.est_vide() and not p2.est_vide():
        if p1.valeur() != p2.valeur():
            return False

    # pas fini, a finir car il manque des use case avant
    return True

#veifier si une chaine de caractere est un palindrome
def est_palindrome(chaine: str) -> bool :
    p = Pile()
    for titouan in chaine :
        p.empiler(titouan)
    # pause
    
    
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

'''
  -------       -------       -------       ------- 
 | valeur | --> | valeur | --> | valeur | --> None  
 |   30   |     |   20   |     |   10   |           
  -------       -------       -------             
    |             |             |
   Suivant      Suivant        Suivant
    ↓             ↓             ↓
    '''