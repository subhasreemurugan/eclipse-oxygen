mins=eval(input("enter the total minutes"))
totaldays=mins/60/24
years=int(totaldays/365)
days=int(totaldays%365)
print(mins," is approximately", years ,"years"," ",days,"days")
