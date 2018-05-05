def isPrime(number):
    i=2
    while i<=number/2:
        if number%i==0:
            return 'false'
        i=i+1
#     print(number)
    return 'true' 

def main():
    count=0
    for i in range(1,10000):
        if isPrime(i)=='true':
            count=count+1
    print("total",count)
    
main()