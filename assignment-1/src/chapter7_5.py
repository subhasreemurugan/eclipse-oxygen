import math

class RegularPolygon:
    
    def __init__(self,n=3,side=1,x=0,y=0):
        self.n = n
        self.side = side
        self.x = x 
        self.y = y
    
    def getPer(self):
        return(self.n*self.side)
    
    def getarea(self):
        return((self.n*self.side*self.side)/4*math.tan(math.pi/4))
    
a=RegularPolygon()
print(a.getPer())
print(a.getarea())
b=RegularPolygon(4,3)
print(b.getPer())
print(b.getarea())
c=RegularPolygon(12,4,5.6,7.8)
print(c.getPer())
print(c.getarea())