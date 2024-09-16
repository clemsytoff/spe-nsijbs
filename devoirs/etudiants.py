class Etudiant:

    def __init__(self,nom,age,notes):
        self.nom = nom
        self.age = age
        self.notes = notes

    def infos(self):
        print("Nom: " + str(self.nom) + " Age: " + str(self.age) + " Notes: " + str(self.notes))
    
    def moyenne(self):
        moy = 0
        nbn = 0
        for i in self.notes:
            nbn += 1
            moy = moy + self.notes[i]
        moye = moy / nbn
        print("La moyenne est " + str(moye))


class GestionEtudiants:
    def __init__(self):
        self.liste=[]
    
    def ajouter(self,Etudiant):
        self.liste.append(Etudiant)
        #print(self.liste[0].notes)
    
    def supprimer_nom(self,nom):
        for i in self.liste:
            if i.nom == nom:
                self.liste.remove(i)


    def find(self,nom):
        for i in self.liste:
            if i.nom == nom:
                i.infos()
    
    def afficher_tous(self):
        for i in self.liste:
            i.infos()



g1=GestionEtudiants()

g1.ajouter(Etudiant("Clément",17,{"anglais":12,"nsi":19,"maths":14}))
g1.ajouter(Etudiant("Djebz",16,{"anglais":16,"nsi":15,"maths":11}))

#m1=Etudiant("Clément",17,{"anglais":12,"nsi":19,"maths":14})
#m1.moyenne()
#g1.find("Djebz")

g1.afficher_tous()
