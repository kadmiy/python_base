# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (501, 501)
sd.background_color = [255, 255, 0]
start_x, start_y = 0, 1
end_x, end_y = 499, 1
current_color = [0, 0, 0]
current_color_2 = [255, 0, 255]

for y in range(1, 551, 100):
    start_point = sd.get_point(start_x, y)
    end_point = sd.get_point(end_x, y)
    sd.line(start_point=start_point, end_point=end_point, color=current_color, width=1)
    for x in range(0, 599, 100):
        start_point_2 = sd.get_point(x, y)
        end_point_2 = sd.get_point(x, y + 50)
        sd.line(start_point=start_point_2, end_point=end_point_2, color=current_color, width=1)
        start_point_21 = sd.get_point(x + 1, y + 1)
        end_point_21 = sd.get_point(x + 1, y + 49)
        sd.line(start_point=start_point_21, end_point=end_point_21, color=current_color_2, width=1)
        start_point_22 = sd.get_point(x - 1, y + 1)
        end_point_22 = sd.get_point(x - 1, y + 49)
        sd.line(start_point=start_point_22, end_point=end_point_22, color=current_color_2, width=1)
        start_point_23 = sd.get_point(x + 2, y + 1)
        end_point_23 = sd.get_point(x + 98, y + 1)
        sd.line(start_point=start_point_23, end_point=end_point_23, color=current_color_2, width=1)
        start_point_24 = sd.get_point(x + 2, y + 49)
        end_point_24 = sd.get_point(x + 98, y + 49)
        sd.line(start_point=start_point_24, end_point=end_point_24, color=current_color_2, width=1)

for y in range(51, 551, 100):
    start_point = sd.get_point(start_x, y)
    end_point = sd.get_point(end_x, y)
    sd.line(start_point=start_point, end_point=end_point, color=current_color, width=1)
    for x in range(-50, 499, 100):
        start_point_2 = sd.get_point(x, y)
        end_point_2 = sd.get_point(x, y + 50)
        sd.line(start_point=start_point_2, end_point=end_point_2, color=current_color, width=1)
        start_point_21 = sd.get_point(x + 1, y + 1)
        end_point_21 = sd.get_point(x + 1, y + 49)
        sd.line(start_point=start_point_21, end_point=end_point_21, color=current_color_2, width=1)
        start_point_22 = sd.get_point(x - 1, y + 1)
        end_point_22 = sd.get_point(x - 1, y + 49)
        sd.line(start_point=start_point_22, end_point=end_point_22, color=current_color_2, width=1)
        start_point_23 = sd.get_point(x + 2, y + 1)
        end_point_23 = sd.get_point(x + 98, y + 1)
        sd.line(start_point=start_point_23, end_point=end_point_23, color=current_color_2, width=1)
        start_point_24 = sd.get_point(x + 2, y + 49)
        end_point_24 = sd.get_point(x + 98, y + 49)
        sd.line(start_point=start_point_24, end_point=end_point_24, color=current_color_2, width=1)

sd.pause()
