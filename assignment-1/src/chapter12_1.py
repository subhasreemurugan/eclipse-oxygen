
class GeometricObject:
    def __init__(self,c='red',fill=True):
        self.__color=c
        self.__fill=fill
    def getcolor(self):
        return self.__color

    def setcolor(self,c):
#         print("c",c)
        self.__color=c 
    def isfill(self):
        return self.__fill
    def setfill(self,f):
        self.__fill=f
    def __str__(self):
        return  "color: " + self.__color +  " and filled: " + str(self.__fill)               
class triangle(GeometricObject):
    def __init__(self, s1 = 1, s2 = 1, s3 = 1):
        super().__init__()
        self.s1=s1
        self.s2=s2
        self.s3=s3
        
    def area(self):
        s=(self.s1+self.s2+self.s3)/2
        print(self.s1,"jj",s)
        a=(s*(s-self.s1)*(s-self.s2)*(s-self.s3))**0.5
#         print(a)
        return a
        
    def peri(self):
        p=(self.s1+self.s2+self.s3)
        return p
    def __str__(self):
        return "Triangle: side1 = " + str(self.s1) + " side2 = " + str(self.s2) + " side3 = " + str(self.s3)
def main():
    s1,s2,s3=eval(input("enter three side   of triangle s1,s2,s3"))
    f=eval(input("enter 1or 0 to show its filled or not"))
    t=triangle(s1,s2,s3)
    print(t)
    print(t.getcolor())
    t.setcolor('green')
    print(t.getcolor())
    print(t.area())
    print(t.peri())
    t.setfill(f)
main()