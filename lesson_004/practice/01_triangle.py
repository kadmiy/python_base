# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length_0 = 200
point_0 = sd.get_point(300, 300)


# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(point, length, angle=0):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


# Одиночный вызов функции
# triangle(point_0, length_0)
# triangle(point_0, length_0, angle=30)
# triangle(point_0, length_0, angle=60)
# triangle(point_0, length_0, angle=90)


for angle_0 in range(0, 361, 30):
    triangle(point_0, length_0, angle_0)

sd.pause()
