import turtle

turtle.shape('turtle')
radius = 50
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)
for i in range(7):
    turtle.circle(-radius, 180)
    if i < 6:
        turtle.circle(-radius / 5, 180)
