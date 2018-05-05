subtotal,rate=eval(input("enter the subtotal and gratuity rate : "))
grat=(subtotal*rate/100)
total=subtotal+grat
print("the gratuity is",format(grat,"10.2f"),"and the  total ",format(total,"10.2f"))