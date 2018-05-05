

class Acc:
    
    def __init__(self, id=0, bal=100, Rate=0):
        self.id = id
        self.bal = bal
        self.Rate = Rate
        
    def getMonthlyRate(self):
        return (self.Rate/12)/100
    
    def getInterest(self):
        return self.bal*((self.Rate/12)/100)
    
    def withdr(self, withdraw):
        self.bal = self.bal - withdraw
        return self.bal
        
    def dep(self, deposit):
        self.bal = self.bal + deposit
        return self.bal
        
Act = Acc(1000, 20000, 4.5)
Act.withdr(2500)
Act.dep(3000)
print(Act.id)
print(Act.bal)
print(Act.getMonthlyRate())
print(Act.getInterest())