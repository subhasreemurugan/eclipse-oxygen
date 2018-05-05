str=(input("enter a string"))
sentc=(input("enter a sentence"))

i=0
if str in sentc:
    for i in range(len(sentc)):
        if str[0]==sentc[i]:
            print("firts string is a substring of 2 at the position",i)
            break;  
else:
    print("not a substring")