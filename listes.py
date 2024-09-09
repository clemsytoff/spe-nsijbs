import random

def generer_tableau():
    table = []
    i = 0
    for i in range(0,15):
        table.append(random.randint(0,100))
        i = i+1
    return(table)

generer_tableau()
nombres=generer_tableau()

def main(tab):
    paires=[]
    impaire=[]
    for i in tab:
        if i%2==0:
            paires.append(i)
        else:
            impaire.append(i) 
    print(paires, impaire)
    


main(nombres)
