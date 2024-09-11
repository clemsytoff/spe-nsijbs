class Soldat:
    def __init__(self):
        self.point_de_vie = 200
        self.point_de_degats = 20
        self.point_endurance = 12

#ce init sert à modifier pour plus tard
    def __init__(self,point_de_vie,point_de_degats,point_endurance): 
        self.point_de_vie = 200
        self.point_de_degats = 20
        self.point_endurance = 12
    
    def bombe(self):
        print("Djebz est dans la place")
    
    def kitdesoins(self):
        self.point_de_vie=200
    
    def deplacements(touche_clavier):
        if (deplacements.direction == "haut"):
            self.y = y + 10
        elif (deplacements.direction == "bas"):
            self.y = y - 10
        elif (deplacements.direction == "droite"):
            self.y = x + 10
        elif (deplacements.direction == "gauche"):
            self.y = x - 10

m1 = Soldat(40,50,11)
m1.bombe()
