class Arbre:

    def __init__(self, valeur=None, fils_gauche=None, fils_droit=None):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit
    
    def modif_fils_gauche(self, fg):
        self.fils_gauche = fg

    def modif_fils_droit(self, fd):
        self.fils_droit = fd    

    def est_vide(self):
        return self.valeur is None and self.fils_droit is None and self.fils_gauche is None

    def inserer_element(self, element):
        if self.valeur is None:
            self.valeur = element
        else:
            if element < self.valeur:
                if self.fils_gauche is None:
                    self.fils_gauche = Arbre(element)
                else:
                    self.fils_gauche.inserer_element(element)
            else:
                if self.fils_droit is None:
                    self.fils_droit = Arbre(element)
                else:
                    self.fils_droit.inserer_element(element)

    def afficher_arbre_prefixe(self):
        if not self.est_vide():
            print(self.valeur)
            if self.fils_gauche:
                self.fils_gauche.afficher_arbre_prefixe()
            if self.fils_droit:
                self.fils_droit.afficher_arbre_prefixe()
    

    def afficher_arbre_infixe(self):
        if not self.est_vide():
            if self.fils_gauche:
                self.fils_gauche.afficher_arbre_infixe()
            print(self.valeur)
            if self.fils_droit:
                self.fils_droit.afficher_arbre_infixe()
    
    def afficher_arbre_postfixe(self):
        if not self.est_vide():
            if self.fils_gauche:
                self.fils_gauche.afficher_arbre_postfixe()
            if self.fils_droit:
                self.fils_droit.afficher_arbre_postfixe()
            print(self.valeur)
    
    def maxi(self):
        max = self.valeur

        if not self.est_vide():
            if self.fils_droit:
                if self.valeur > max:
                    return max
                else:
                    return self.fils_droit.maxi()
        else:
            return 0
        
        return max
    
    def mini(self):
        min = self.valeur

        if not self.est_vide():
            if self.fils_gauche:
                if self.valeur < min:
                    return min
                else:
                    return self.fils_gauche.mini()
        else: 
            return 0




#chercher si un element est present ou pas
def est_element_present(abr: Arbre, element) -> bool:
    # Si l'arbre est vide
    if abr is None or abr.est_vide():
        return False

    # Si l'élément est trouvé à la racine
    if element == abr.valeur:
        return True

    # Si l'élément est plus petit que la valeur actuelle, chercher dans le sous-arbre gauche
    if element < abr.valeur:
        if abr.fils_gauche is not None:
            return est_element_present(abr.fils_gauche, element)
        else:
            return False

    # Si l'élément est plus grand que la valeur actuelle, chercher dans le sous-arbre droit
    if element > abr.valeur:
        if abr.fils_droit is not None:
            return est_element_present(abr.fils_droit, element)
        else:
            return False




# Test de l'arbre
abr = Arbre()
abr.inserer_element(5)
abr.inserer_element(3)
abr.inserer_element(7)
abr.inserer_element(2)
abr.inserer_element(4)
abr.inserer_element(6)
abr.inserer_element(8)

abr.afficher_arbre_prefixe()

if est_element_present(abr,-1):
    print("il existe")
else:
    print("il n'existe pas")



min(abr)
