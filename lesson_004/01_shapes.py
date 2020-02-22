# -*- coding: utf-8 -*-
import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle(point, angle, length):
#     t1 = sd.get_vector(point, angle, length, 5)
#     sd.line(start_point=point, end_point=t1.end_point, color=sd.COLOR_YELLOW, width=1)
#     t2 = sd.get_vector(t1.end_point, angle + 120, length, 5)
#     sd.line(start_point=t1.end_point, end_point=t2.end_point, color=sd.COLOR_YELLOW, width=1)
#     # t3 = sd.get_vector(t2.end_point, angle + 240, length, 5)
#     sd.line(start_point=t2.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)
#
#
# def square(point, angle, length):
#     s1 = sd.get_vector(point, angle, length, 5)
#     sd.line(start_point=point, end_point=s1.end_point, color=sd.COLOR_YELLOW, width=1)
#     s2 = sd.get_vector(s1.end_point, angle + 90, length, 5)
#     sd.line(start_point=s1.end_point, end_point=s2.end_point, color=sd.COLOR_YELLOW, width=1)
#     s3 = sd.get_vector(s2.end_point, angle + 180, length, 5)
#     sd.line(start_point=s2.end_point, end_point=s3.end_point, color=sd.COLOR_YELLOW, width=1)
#     # s4 = sd.get_vector(s3.end_point, angle + 270, length, 5)
#     sd.line(start_point=s3.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)
#
#
# def pentagon(point, angle, length):
#     p1 = sd.get_vector(point, angle, length, 5)
#     sd.line(start_point=point, end_point=p1.end_point, color=sd.COLOR_YELLOW, width=1)
#     p2 = sd.get_vector(p1.end_point, angle + 72, length, 5)
#     sd.line(start_point=p1.end_point, end_point=p2.end_point, color=sd.COLOR_YELLOW, width=1)
#     p3 = sd.get_vector(p2.end_point, angle + 144, length, 5)
#     sd.line(start_point=p2.end_point, end_point=p3.end_point, color=sd.COLOR_YELLOW, width=1)
#     p4 = sd.get_vector(p3.end_point, angle + 216, length, 5)
#     sd.line(start_point=p3.end_point, end_point=p4.end_point, color=sd.COLOR_YELLOW, width=1)
#     # p5 = sd.get_vector(p4.end_point, angle + 288, length, 5)
#     sd.line(start_point=p4.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)
#
#
# def hexagon(point, angle, length):
#     h1 = sd.get_vector(point, angle, length, 5)
#     sd.line(start_point=point, end_point=h1.end_point, color=sd.COLOR_YELLOW, width=1)
#     h2 = sd.get_vector(h1.end_point, angle + 60, length, 5)
#     sd.line(start_point=h1.end_point, end_point=h2.end_point, color=sd.COLOR_YELLOW, width=1)
#     h3 = sd.get_vector(h2.end_point, angle + 120, length, 5)
#     sd.line(start_point=h2.end_point, end_point=h3.end_point, color=sd.COLOR_YELLOW, width=1)
#     h4 = sd.get_vector(h3.end_point, angle + 180, length, 5)
#     sd.line(start_point=h3.end_point, end_point=h4.end_point, color=sd.COLOR_YELLOW, width=1)
#     h5 = sd.get_vector(h4.end_point, angle + 240, length, 5)
#     sd.line(start_point=h4.end_point, end_point=h5.end_point, color=sd.COLOR_YELLOW, width=1)
#     # h6 = sd.get_vector(h5.end_point, angle + 300, length, 5)
#     sd.line(start_point=h5.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)
#
#
# point_work = sd.get_point(100, 100)
# triangle(point_work, 15, 150)
#
# point_work = sd.get_point(350, 100)
# square(point_work, 15, 150)
#
# point_work = sd.get_point(100, 350)
# pentagon(point_work, 15, 100)
#
# point_work = sd.get_point(350, 350)
# hexagon(point_work, 15, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# ___ Если использовать принцип "Copy-Paste" получится просто невероятное количество строк кода,
# ___ равно как и ошибок в них.


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
        point = end_point
        # t2 = sd.get_vector(t1.end_point, angle + 120, length, 5)
        # sd.line(start_point=t1.end_point, end_point=t2.end_point, color=sd.COLOR_YELLOW, width=1)
        # sd.line(start_point=t2.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)


# (point_start_x, point_start_y, length_start, type_of_polygon)
start_point = [(100, 100, 150, 3), (350, 100, 150, 4), (100, 350, 100, 5), (350, 350, 100, 6)]

for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    polygon(point_start, heads_start, length_start)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

# ___ Не то слово, через вызов функции в цикле читаем из списка параметры многоугольника


sd.pause()
