class Soldat:

#ce init sert à modifier pour plus tard
    def __init__(self,point_de_vie=200,point_de_degats=20,point_endurance=13): 
        self.point_de_vie = point_de_vie
        self.point_de_degats = point_de_degats
        self.point_endurance = point_endurance
    
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

m1 = Soldat()
        
