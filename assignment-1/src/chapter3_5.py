import turtle
x1,y1=eval(input("enter the first point x1,y1"))
x2,y2=eval(input("enter the first point x2,y2"))
point=turtle.Turtle()
point.penup()
point.goto(x1,y1)
point.pendown()
point.write(x1)
point.write(y1)

point.goto(x2,y2)
point.hideturtle()
point.write(x2)
point.write(y2)

turtle.done()
