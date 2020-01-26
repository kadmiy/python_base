# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
x, y, radius, tmp = 100, 100, 50, 3
circle_color = [0, 255, 0]
while tmp > 0:
    circle_center = sd.get_point(x, y)
    sd.circle(center_position=circle_center, radius=radius, color=circle_color, width=5)
    radius = radius - 10
    tmp -= 1

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


