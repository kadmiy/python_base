# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# x, y, radius, tmp = 100, 100, 50, 3
# circle_color = [0, 255, 0]
# while tmp > 0:
#     circle_center = sd.get_point(x, y)
#     sd.circle(center_position=circle_center, radius=radius, color=circle_color, width=5)
#     radius = radius - 10
#     tmp -= 1

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def circle(circle_center, radius, circle_color):
#     sd.circle(center_position=circle_center, radius=radius, color=circle_color, width=5)
#
# x, y, radius, tmp = 100, 100, 50, 3
# circle_color = [0, 255, 0]
# while tmp > 0:
#     circle_center = sd.get_point(x, y)
#     circle(circle_center, radius, circle_color)
#     radius = radius - 10
#     tmp -= 1

# Нарисовать 10 пузырьков в ряд
# def circle(circle_center, radius, circle_color):
#     sd.circle(center_position=circle_center, radius=radius, color=circle_color, width=5)
#
#
# x, y, radius, tmp, tmp_2 = 100, 100, 50, 3, 10
# circle_color = [0, 255, 0]
# start_x, start_y = x, y
# while tmp_2 > 0:
#     circle_center = sd.get_point(start_x, start_y)
#     start_radius = radius
#     while tmp > 0:
#         circle(circle_center, start_radius, circle_color)
#         start_radius = start_radius - 10
#         tmp -= 1
#     start_x += 75
#     tmp = 3
#     tmp_2 -= 1

# Нарисовать три ряда по 10 пузырьков
def circle(circle_center, radius, circle_color):
    sd.circle(center_position=circle_center, radius=radius, color=circle_color, width=5)


x, y, radius, tmp, tmp_2, tmp_3 = 100, 100, 50, 3, 10, 3
circle_color = [0, 255, 0]
start_x, start_y = x, y
while tmp_3 >0:
    while tmp_2 > 0:
        circle_center = sd.get_point(start_x, start_y)
        start_radius = radius
        while tmp > 0:
            circle(circle_center, start_radius, circle_color)
            start_radius = start_radius - 10
            tmp -= 1
        start_x += 75
        tmp = 3
        tmp_2 -= 1
    start_x = x
    start_y += 75
    tmp_2 = 10
    tmp_3 -= 1

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
