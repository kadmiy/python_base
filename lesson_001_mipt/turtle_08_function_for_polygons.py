import turtle


def polygons(n, polygon_side):
    for j in range(n):
        angle = 360 / n
        turtle.left(angle)
        turtle.forward(polygon_side)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()


side = 10
turtle.shape('classic')
turtle.speed(speed=1)
for i in range(3, 13, 1):
    polygons(i, side)
    side += 15
