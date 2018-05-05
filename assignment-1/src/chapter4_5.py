def weekday(i):
    if i==1:
        to_disp="monday"
    elif i==2:
        to_disp="Tueday"
    elif i==3:
        to_disp="Wednesday"
    elif i==4:
        to_disp="Thursday"
    elif i==5:
        to_disp="friday"
    elif i==6:
        to_disp="saturday"
    elif i==0:
        to_disp="Sunday"
    return to_disp

day=eval(input("Enter today's day: "))
elap=eval(input("Enter the number of days elapsed since today: "))
i=weekday((day+elap)%7)
today=weekday(day)
print("Today is", today," and the future day is ",i)