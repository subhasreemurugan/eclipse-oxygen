import random
def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0,1),end=" ")
        print()
def main():
    n=eval(input("enter a no"))
    printMatrix(n)
main()      