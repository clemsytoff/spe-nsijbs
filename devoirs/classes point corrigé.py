from math import *

class Point:
    def __init__(self,x=3,y=10):
        self.x = x
        self.y = y
    
    def translation(self, vx, vy):
        self.x += vx
        self.y +=vy
    
    def distance(self, p):
        d = sqrt(pow(p.x - self.x,2) + pow(p.y - self.y,2))
        return d

p1=Point()
p2 = Point(45,78)
d = p1.distance(p2)
print(d)
#Elbarto le goat
