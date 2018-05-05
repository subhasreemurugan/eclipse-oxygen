s1='welcomeco'
print(len(s1),max(s1),min(s1),s1[-1],"come" in s1)
for i in range(0,len(s1)):
    print(s1[i])
for i in range(0,6,2):
    print(i,"",s1[i])
print(s1[::2])
print(s1[::-1])

print(s1.isalnum(),"anum")
print(s1.isalpha(),"alpha")
print(s1.isdigit(),"digit")
print(s1.isidentifier(),"identi")
print(s1.islower(),"lower")
print(s1.isupper(),"upper")
print(s1.isspace(),"space")

print(s1.endswith('come'),"ends")
print(s1.startswith('wel'),"starts")
print(s1.find("co"))
print(s1.rfind("co"))
print(s1.count("e"))

pali='abba'
palindrome='true'
j=len(pali)-1
print(j)
i=0
for i in range(len(pali)):
    if(pali[i]!=pali[j]):
        palindrom='false'
        break
    j=j-1
    
if palindrome=='true':
    print("pali")
else:
    print("not palin")
        