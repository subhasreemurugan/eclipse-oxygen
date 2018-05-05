class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
             
    def isSolvable(self):
        return(self.a*self.d-self.b*self.c !=0)

    
    def getX(self):
        return((self.e*self.d - self.b*self.f)/(self.a*self.d- self.b*self.c))
        
    
    def getY(self):
        return((self.a*self.f - self.e*self.c)/(self.a*self.d - self.b*self.c))
    
def getPoints(a,b,c,d,e,f,g,h):
    a1=(c-a)/(b-d)
    b1=1
    c1=(c*b-a*d)/(c-a)
    a2=(g-e)/(f-h)
    b2=1
    c2=(g*f-e*h)/(g-e)
    return(a1,b1,a2,b2,c1,c2)

a,b,c,d=eval(input("Enter the endpoints of the first line segment"))
e,f,g,h=eval(input("Enter the endpoints of the second line segment"))

x1,y1,z1,x2,y2,z2=getPoints(a,b,c,d,e,f,g,h)
L= LinearEquation(x1,y1,z1,x2,y2,z2)
if(L.isSolvable() == True):
    print("The intersecting point is")
    print(L.getX())
    print(L.getY())
else:
    print("no solutions")