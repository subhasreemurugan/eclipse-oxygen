def sumMajorDiagonal(m):
    sum=0
    for i in range(len(m)):
        sum=sum+m[i][i]  
    print(sum)


def main():
    n=eval(input("enterthe no of row "))
    grid=[]
    for i in range(n):
        line=input("enter row").strip().split()
        grid.append([eval(x) for x in line])
    print(grid)
    sumMajorDiagonal(grid)
    
main()