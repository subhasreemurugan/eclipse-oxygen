class acc:
    def __init__(self,amt=100):
        self.amt=amt
    def getbal(self):
        print("your bal",self.amt)
    def withdraw(self,w):
        if (self.amt-w)>=0:
           self.amt -= w 
        else:
            print("insuffisient bal")
    def dep(self,d):
        self.amt += d
    def exit(self):
        print("thankyou")
def main():
    id1=eval(input("enter id"))
    while  id1<0 or id1>9 :
        id1=eval(input("invalid entry enter again"))
    a=acc()
    opt=1
    while opt <=4:
        opt=eval(input("Main menu 1: check balance 2: withdraw 3: deposit 4: exit"))  
        if opt==1: 
            a.getbal() 
        elif opt==2:
            w=eval(input("enter the amt to wihdraw")) 
            a.withdraw(w)
        elif opt==3:
            d=eval(input("enter the amt to deposit")) 
            a.dep(d)
        elif opt==4:
            a.exit()
            break
        else:
            print("thanku you invalid entry")  
main()
