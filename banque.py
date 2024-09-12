# classe pour un compte banquaire - nom titulaire et solde, 3 méthodes: déposer, retirer, afficher

class Compte:
    def __init__(self,nom="Clément",solde=1000):
        self.nom = nom
        self.solde = solde
        
    def depot(self,depot):
        self.solde = self.solde + depot
    
    def retrait(self, retrait):
        if self.solde - retrait <= 0:
            print("Vous n'avez pas assez d'argent")
        else:
            self.solde = self.solde - retrait
    
    def afficher(self):
        if self.nom == "Elbarto" or "Bharat":
            print("Bharat tu es un clodo.")
        elif self.nom == "djebz" or "lamenace.exe" or "lamenace" or "Djebril":
            print("Djebz, voler n'est pas bon.")
        else:    
            print("Vous disposez de " + str(self.solde) + " € sur le compte de Mr. " + self.nom)

m1=Compte()
m2=m1.retrait(120)
m3=m1.afficher()
