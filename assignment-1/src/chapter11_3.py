class matrixadd:
    def __init__(self):
        self.grid = []
    def getgrid(self):
        n =eval(input("enter the row and col number"))
        for i in range(n):
            line = input("enter the row").strip().split()
            self.grid.append([eval(x) for x in line])
        return self.grid
    def add(self,m2=[]): 
        m3 =[]    
        print(self.grid,m2.grid)
        i=0
        for i in range(len(self.grid)):
            m3.append([])
            for j in range(len(m2.grid)):
                m3[i].append(self.grid[i][j]+m2.grid[i][j]) 
        print(m3)
def main():
    m1 = matrixadd()
    m2 = matrixadd()
    m1.getgrid()
    m2.getgrid()
    m1.add(m2)
main()