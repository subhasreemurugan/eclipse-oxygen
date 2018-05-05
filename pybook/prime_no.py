def isPrimeNum():
    count = 0
    #if j > 1:  
    # check for factors
    for j in range(1,10000):
        flag='true'
        for i in range(2,j):
            if (j % i) == 0:
                flag='false'
                break
            #else:
            else:
                flag='true'
        if(flag=='true'):
#             print(j)
            count=count+1        
            #elif (j % j) == 0:

    print("Count: ", count)
                    
isPrimeNum()
