import turtle


def circle(radius, extent, color):
    turtle.color('black', color)
    turtle.begin_fill()
    extent /= 10
    extent = int(extent)
    for _ in range(extent):
        turtle.forward(radius)
        turtle.left(10)
    turtle.end_fill()


def arc(radius, extent, color):
    turtle.color(color)
    turtle.width(10)
    extent /= 10
    extent = int(extent)
    for _ in range(extent):
        turtle.forward(radius)
        turtle.left(10)


turtle.shape('turtle')
circle(10, 360, 'yellow')
turtle.penup()
turtle.goto(-20, 70)
turtle.pendown()
circle(2, 360, 'blue')
turtle.penup()
turtle.goto(30, 70)
turtle.pendown()
circle(2, 360, 'blue')
turtle.penup()
turtle.goto(7, 65)
turtle.pendown()
turtle.color('black')
turtle.width(10)
turtle.right(90)
turtle.forward(25)
turtle.penup()
turtle.goto(-22, 40)
turtle.pendown()
arc(5, 190, 'red')
turtle.penup()
turtle.color('black')
turtle.goto(-100, -100)
turtle.exitonclick()
