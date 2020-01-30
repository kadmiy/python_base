import turtle

side = 10
turtle.shape('turtle')
for i in range(10):
    for j in range(4):
        turtle.forward(side)
        turtle.left(90)
        side += 10
