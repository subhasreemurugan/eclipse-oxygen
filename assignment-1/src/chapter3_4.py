import turtle
shapes=turtle.Turtle()
shapes.penup()
shapes.left(180)
shapes.goto(-250,0)
shapes.pendown()
shapes.circle(40,steps=3)

shapes.left(45)
shapes.penup()
shapes.goto(-180,0)
shapes.pendown()
shapes.circle(40,steps=4)

shapes.left(26)
shapes.penup()
shapes.goto(-70,-10)
shapes.pendown()
shapes.circle(35,steps=5)

shapes.left(18)
shapes.penup()
shapes.goto(50,-20)
shapes.pendown()
shapes.circle(35,steps=6)

shapes.left(22)
shapes.penup()
shapes.goto(150,-30)
shapes.pendown()
shapes.circle(35,steps=8)

turtle.done()