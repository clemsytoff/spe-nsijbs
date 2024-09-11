users = [{"nom":"Clément","age":24,"sexe":"homme","vacciné":True},{"nom":"Djebz","age":16,"sexe":"homme","vacciné":True},{"nom":"Elbarto","age":90,"sexe":"homme","vacciné":False},{"nom":"Reda","age":14,"sexe":"femme","vacciné":True},{"nom":"Emma","age":18,"sexe":"femme","vacciné":False}]



def majeur(x):
    majeur = []
    for i in x:
        if i["age"] >= 18:
            majeur.append(i["nom"])
    print(majeur)

def mineur(x):
    mineurs = []
    for i in x:
        if i["age"] <= 18:
            mineurs.append(i["nom"])
    print(mineurs)

def vaccinésmajeurs(x):
    vm = []
    for i in x:
        if i["age"] >= 18 and i["vacciné"] == True:
            vm.append(i["nom"])
    print(vm)

def vaccinésmineurs(x):
    vmi = []
    for i in x:
        if i["age"] <= 18 and i["vacciné"] == True:
            vmi.append(i["nom"])
    print(vmi)
            

majeur(users)
mineur(users)
vaccinésmajeurs(users)        
vaccinésmineurs(users)
