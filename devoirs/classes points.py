class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def translation(self,direction): #1=haut, 2=bas, 3=gauche, 4=droite - y haut, x long
        if (direction == 1):
            self.y = self.y+10
            print(self.y)
        elif (direction == 2):
            self.y = self.y - 10
            print(self.y)
        elif (direction == 3):
            self.x = self.x - 10
            print(self.x)
        elif (direction == 4):
            self.x = self.x + 10
            print(self.x)
        
    def position(self, xo, yo):
        #calcul x
        if xo > self.x:
            self.grandx = xo
            self.petitx = self.x
        else:
            self.grandx = self.x
            self.petitx = xo
        self.resultx = self.grandx - self.petitx
        
        #calcul y
        if yo > self.y:
            self.grandy = yo
            self.petity = self.y
        else:
            self.grandy = self.y
            self.petity = yo
        self.resulty = self.grandy - self.petity
        
        #resultat
        self.resultatxy = self.resulty + self.resultx + 100 #on ajoute le 0 vu qu'on bouge en 10 par 10
        print("La distance entre le joueur et l'objectif est de " + str(self.resultatxy) + " pixels.")
        print("La distance entre le joueur et l'objectif est de " + str(self.resultx + 100) + " X et " + str(self.resulty + 100) + " Y.")



point1= Point(10,20)
point1.translation(1)
point1.position(50,70) #on met les coo du point où on veux aller, x puis y