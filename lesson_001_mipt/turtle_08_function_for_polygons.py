import turtle
from math import cos,radians


def polygons(f_radius, f_heads, f_angle, f_side, f_start_angle):
    turtle.penup()
    turtle.forward(f_radius)
    turtle.pendown()
    turtle.left(f_start_angle)
    for _ in range(f_heads):
        turtle.left(f_angle)
        turtle.forward(f_side)
    turtle.right(f_start_angle)


radius = step_radius = 15
turtle.shape('turtle')
# turtle.shape('classic')
# turtle.speed(speed=1)
for heads in range(3, 13, 1):
    angle = 360 / heads
    start_angle = 90 - (angle / 2)
    side = 2 * cos(radians(start_angle)) * radius
    polygons(step_radius, heads, angle, side, start_angle)
    radius += step_radius
