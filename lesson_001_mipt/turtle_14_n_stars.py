import turtle


def stars(f_forward, f_length, f_heads):
    turtle.penup()
    turtle.forward(f_forward)
    turtle.pendown()
    angle = 180 - (360 / (f_heads * 2))
    for _ in range(f_heads):
        turtle.forward(f_length)
        turtle.left(angle)


turtle.shape('turtle')
turtle.left(180)
stars(50, 200, 5)
stars(-300, 200, 11)
turtle.exitonclick()
