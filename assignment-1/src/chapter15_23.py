def per(str1,l,r):
    if l==r:
        print(str1)
    else:
        for i in (l,r):
            str1[l] , str1[i] = str1[i] , str1[l]
            per(str1,l+1,r)
            str1[l] , str1[i] = str1[i] , str1[l]
str1="abc"
per(list(str1),0,(len(str1)-1))