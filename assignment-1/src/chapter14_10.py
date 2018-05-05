dict={"A":"a","B":"b","C":"c","D":"d"}
states=dict.keys()
for x in states:
    cap=input("enter the cpital  of "+x)
    if cap ==dict[x]:
        print("right")
    else:
        print("wrong")