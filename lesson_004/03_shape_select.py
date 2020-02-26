# -*- coding: utf-8 -*-
from math import sin, radians

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(heads, color):
    color_rainbow = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                     sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    length = 150
    center = sd.get_point(300, 300)
    angle = 0
    angle_start = 0
    angle_polygon = 360 / heads
    angle_center = angle_polygon / 2
    radius = length / (2 * sin(radians(angle_center)))
    point = vector(center, radius, -(90 + angle_center))
    point_polygon = point
    color_paint = color_rainbow[color - 1]
    sd.circle(center_position=center, radius=2, color=color_rainbow[0], width=1)
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=color_paint, width=1)
        point = end_point


color_input = 1

while color_input:
    color_input = input('Возможные цвета:\n'
                        '   0: Выход из программы.\n'
                        '   1: Красный\n'
                        '   2: Оранжевый\n'
                        '   3: Жёлтый\n'
                        '   4: Зелёный\n'
                        '   5: Голубой\n'
                        '   6: Синий\n'
                        '   7: фиолетовый\n')
    if color_input.isnumeric():
        color_input = int(color_input)
        if color_input == 0:
            break
        elif color_input < 0 or color_input > 7:
            print('Неверный ввод')
            continue
    else:
        print('Неверный ввод')
        continue
    heads_start = input('Введите количество вершин многоугольника:\n')
    if heads_start.isnumeric():
        heads_start = int(heads_start)
        if heads_start < 3:
            print('Построение многоугольника невозвожно!')
            continue
    else:
        print('Неверный ввод')
        continue
    polygon(heads_start, color_input)
    break
sd.pause()
