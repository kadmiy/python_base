import turtle

turtle.shape('turtle')
radius = 50
turtle.left(90)
for _ in range(10):
    turtle.circle(radius)
    turtle.circle(-radius)
    radius += 5
