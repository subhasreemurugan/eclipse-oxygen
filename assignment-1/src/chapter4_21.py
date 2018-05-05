import math
year=eval(input("enter year"))
m=eval(input("enter month"))
q=eval(input("enter day"))
j=year/100
k=year%100
h=math.ceil(q+(26*(m+1)/10)+k+(k/4)+(j/4)+(5*j))%7
print("h",h)
if h ==0:
    print("saturday")
elif h ==1:
    print("sunday")
elif h ==2:
    print("monday")
elif h ==3:
    print("tuesday")
elif h ==4:
    print("wednesday")
elif h ==5:
    print("thursday")
elif h ==6:
    print("friday")
else:
    print("err")

