from datetime import datetime
import time

class Time:
    
    def __init__(self,h = datetime.now().hour,min1=datetime.now().minute,sec1=datetime.now().second):
        self.h = h
        self.min1 = min1
        self.sec1 = sec1 
    
    def CurrTime(self):
        return(self.h,self.min1,self.sec1)
       
    def setTime(self):
        elapsedtime = eval(input("Enter elapsed time"))
        return(elapsedtime)
        
    def getElapse(self):
        t=self.setTime()
        h=round(t/(60*60)%24)
        m=round(t/(60)%60)
        s=(round(t%60))
        return(h,m,s)
a = Time()
print(" Curr Time is",a.CurrTime())
print("Elapse time is:",a.getElapse())


