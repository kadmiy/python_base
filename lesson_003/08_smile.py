# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(start_x, start_y, line_color):
    start_point = sd.get_point(start_x, start_y)
    sd.circle(center_position=start_point,radius=200,color=line_color,width=3)
    start_point = sd.get_point(start_x - 75, start_y + 75)
    sd.circle(center_position=start_point,radius=20,color=line_color,width=3)
    start_point = sd.get_point(start_x + 75, start_y + 75)
    sd.circle(center_position=start_point,radius=20,color=line_color,width=3)
    start_point = sd.get_point(start_x, start_y + 75)
    end_point = sd.get_point(start_x, start_y - 75)
    sd.line(start_point=start_point, end_point=end_point,color=line_color,width=3)
    point_list = [sd.get_point(start_x - 100, start_y - 100), sd.get_point(start_x - 50, start_y - 125)
        , sd.get_point(start_x + 50, start_y - 125), sd.get_point(start_x + 100, start_y - 100)]
    sd.polygon(point_list=point_list, color=current_color, width=3)


sd.resolution = (501, 501)
sd.background_color = [255, 255, 0]
current_color = [0, 0, 255]
smile(250,250,current_color)

sd.pause()
