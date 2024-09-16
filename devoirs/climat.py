class JourClimatique:
    def __init__(self,date,température,précipitations):
        self.date = date
        self.température = température
        self.précipitations = précipitations
    

    def infos(self):
        print("Date : " + str(self.date) + " Température : " + str(self.température) + " Précipitations : " + str(self.précipitations))


class AnalyseurClimatique:
    def __init__(self):
        self.jours = []

    def ajouter(self,jour):
        self.jours.append(jour)
    

    def moyenne(self):
        total = 0
        nb = 0
        for i in self.jours:
            nb += 1
            total = total + i.température
        moy=total/nb
        print("La moyenne est de " + str(round(moy)) + " °C")


    def precipitations(self):
        max=0
        dateg=0
        for i in self.jours:
            if int(i.précipitations) > int(max):
                max = i.précipitations
                dateg=i.date
        print("Plus de précipitations le " + str(dateg))

    
    def tous(self):
        for i in self.jours:
            i.infos()

j1 = JourClimatique("12/09/2024",12,95)
j3 = JourClimatique("13/09/2024",20,20)
j2 = JourClimatique("14/09/2024",15,60)
#j1.infos()
m1 = AnalyseurClimatique()
m1.ajouter(j1)
m1.ajouter(j2)
m1.ajouter(j3)
#m1.moyenne()
#m1.precipitations()
m1.tous()
