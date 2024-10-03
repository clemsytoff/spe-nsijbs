class File:
    def __init__(self, valeur=None, suivant=None):
        # Le constructeur initialise une cellule de la file avec une valeur et un pointeur vers l'élément suivant.
        # `valeur` représente la donnée stockée dans le nœud.
        # `suivant` (ou `queue` en tant que dernier élément de la file) pointe vers le nœud suivant dans la file.
        self.valeur = valeur
        self.suivant = suivant
        self.queue = suivant
        # Le pointeur vers le suivant et la queue sont initialisés à la même valeur.
    
    def enfiler(self, valeur):
        # Cette méthode ajoute un élément à la file.
        if self.est_vide():
            # Si la file est vide, on met à jour la valeur de l'élément courant et on crée un nouveau nœud vide à la suite.
            self.valeur = valeur
            self.queue = File()  # La queue devient une nouvelle instance de File vide.
            self.suivant = self.queue  # L'élément suivant pointe aussi vers la queue.
        else:
            # Si la file n'est pas vide, on ajoute la nouvelle valeur à la fin (dans `self.queue`).
            self.queue.valeur = valeur  # La valeur est ajoutée dans la queue actuelle.
            self.queue.suivant = File()  # Un nouveau nœud vide est créé pour être la nouvelle queue.
            self.queue = self.queue.suivant  # La queue est mise à jour pour pointer vers le nouveau nœud vide.
    
    def defiler(self):
        # Cette méthode retire et renvoie l'élément en tête de la file (FIFO).
        valeur = self.valeur  # On sauvegarde la valeur courante qui est en tête de la file.
        self.valeur = self.suivant.valeur  # La valeur de l'élément suivant devient la nouvelle valeur de la tête.
        self.suivant = self.suivant.suivant  # Le suivant de l'élément actuel devient le suivant de l'ancien suivant.
        return valeur  # On retourne la valeur de l'élément qui a été retiré de la file.
    
    def est_vide(self):
        # Cette méthode vérifie si la file est vide.
        # La file est vide si `suivant` est `None`.
        return self.suivant is None
    
    def copy(self):
        return File(self.valeur,self.suivant)


def afficher_file(f:File) :

    copy = File(f.valeur,f.suivant)
    if f.est_vide():
        print("la file est vide")

    else:
        while not copy.est_vide():
            print(copy.defiler())


'''
Exercice 1 :  Écrire les fonctions minimum et maximum.
'''

def mini_maxi(f:File) :
    if f.est_vide():
        return ValueError("la file est vide")
    
    fc = f.copy()
    mini = f.valeur
    maxi = f.valeur
    while not fc.est_vide():
        valeur = fc.defiler()
        if valeur < mini :
            mini = valeur
        if valeur > maxi:
            maxi = valeur

    return mini , maxi
'''
Exercice 2. Écrire la fonction trier, qui renvoie une copie triée de la file.
3.2.4. Écrire la fonction fusionne, fusionnant deux files triées en une file triée. On pourra 
auparavant rajouter une méthode lire_sommet à la classe File qui renvoie le sommet 
d’une file sans le défiler



'''
#Exercice 3 : Vérifier si deux files sont égales
#Écrivez une fonction sont_egales(file1, file2) qui prend deux files en entrée et renvoie True si elles sont identiques (même nombre d'éléments et mêmes éléments dans le même ordre), sinon False.

def sont_egales(file1:File, file2:File) -> bool :

    if file1.est_vide() and file2.est_vide():
        return True
    
    if file1.est_vide() and not file2.est_vide() or file2.est_vide() and not file1.est_vide():
        return False

    fc1 = file1.copy()
    fc2 = file2.copy()

    while not fc1.est_vide() and not fc2.est_vide():
        if fc1.defiler() != fc2.defiler():
            return False    
    
    return True

#Exercice 2 : Compter les éléments d'une file
#Écrivez une fonction compter_elements(file) qui parcourt la file et renvoie le nombre d'éléments qu'elle contient sans modifier la file.

def compter_element(file:File) -> int :
    if file.est_vide():
        return 0

    copy = file.copy()

    count = 0

    while not copy.est_vide():
        count += 1
        copy.defiler()
    
    return count

#exercice 4 bis : fusionner deux files
def fusion_file(f1:File,f2:File) -> File:
    if f1.est_vide():
        return f2
    if f2.est_vide():
        return f1 

    
    fc1 = f1.copy()
    fc2 = f2.copy()

    fres = fc1

    while not fc2.est_vide():
        val = fc2.defiler()
        fres.empiler(val)   
    
    return fres

#exercice 4 : Fusionner deux files, la file qui a la plus petite taille precede la
# file qui a une taille plus grand qu'elle

def fusion_file_taille_sup(f1 : File, f2: File) -> File :
    if f1.est_vide():
        return f2
    if f2.est_vide():
        return f1 
    
    if compter_element(f1) > compter_element(f2):
        fres = File
        fc1 = f1.copy()
        fc2 = f2.copy()
        #to be continued

    return


#exercice 5 : supprimer un element de la file
def supprimer_element(f:File, element) -> File :
    
    fc = f.copy()
    fres = File()

    while not fc.est_vide():
        val = fc.defiler()
        if val != element:
            fres.enfiler(val)
    
    return fres

#exercice 6 : tri de file rudimentaire en utilisant mini_maxi
def tri_file(f:File) -> File :
    if f.est_vide():
        return File()
    
    fc = f.copy()
    ftriee = File()

    while not fc.est_vide():
        mini , _  = mini_maxi(fc)
        ftriee.enfiler(mini)
        fc = supprimer_element(fc,mini)

    return ftriee

f1 = File()
f1.enfiler(1)
f1.enfiler(4)
f1.enfiler(9)
f1.enfiler(3)

ftr = tri_file(f1)



afficher_file(f1)
mini, maxi = mini_maxi(f1)
print("la valeur minimale est : ",mini,"maximum : ",maxi)

f2 = File()
f2.enfiler(1)
f2.enfiler(2)
f2.enfiler(3)

if sont_egales(f1,f2) :
    print("les files sont egales")
else:
    print("elles ne sont PAS egales")


print("taille = ",compter_element(f1))

afficher_file(ftr)