import turtle
x1,y1=eval(input("enter point of bigger circle"))
r1=eval(input("enter the radii1"))
x2,y2=eval(input("enter point of bigger circle"))
r2=eval(input("enter the radii1"))
c1=turtle.Turtle()
c1.penup()
c1.goto(x1,y1)
c1.goto(x1,(y1+r1))
c1.pendown()
c1.circle(r1)
c1.hideturtle()

c1.penup()
c1.goto(x2,y2)
c1.goto(x2,(y2+r2))
c1.pendown()
c1.circle(r2)
c1.hideturtle()

turtle.done()