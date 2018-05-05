import math

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    def dist(self,point):
#         print(point.x,point.y)
        dist=math.sqrt((point.x-self.x)**2+(point.y-self.y)**2)
        return dist
    def nearby(self,point):
        d=self.dist(point)
        if d <=5:
            print(self.__str__(),"closer",point.__str__())
        else:
            print(self.__str__()," not closer",point.__str__())  
    def __str__(self):
        return (self.x,self.y)

def main():
    p1=point(0,0)
    p2=point(2,2)
    print(p1.dist(p2))
    p1.nearby(p2)
   
    
main()
