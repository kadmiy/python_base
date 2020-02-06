import turtle

side = 10
turtle.shape('turtle')
for i in range(10):
    for j in range(4):
        turtle.forward(side)
        turtle.left(90)
    side += 20
    turtle.penup()
    for k in range(2):
        turtle.right(90)
        turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
turtle.exitonclick()

