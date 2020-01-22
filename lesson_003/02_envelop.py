# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9 # NO!
# проверить для
# paper_x, paper_y = 9, 8 # NO!
# paper_x, paper_y = 6, 8 # YES!
# paper_x, paper_y = 8, 6 # YES!
# paper_x, paper_y = 3, 4 # YES!
# paper_x, paper_y = 11, 9 # NO!
# paper_x, paper_y = 9, 11 # NO!
# (просто раскоментировать нужную строку и проверить свой код)

if (paper_x < envelop_x and paper_y < envelop_y) or (paper_x < envelop_y and paper_y < envelop_x):
    print('Yes!')
else:
    print('No!')

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2 # No!
# brick_x, brick_y, brick_z = 11, 2, 10 # No!
# brick_x, brick_y, brick_z = 10, 11, 2 # No!
# brick_x, brick_y, brick_z = 10, 2, 11 # No!
# brick_x, brick_y, brick_z = 2, 10, 11 # No!
# brick_x, brick_y, brick_z = 2, 11, 10 # No!
# brick_x, brick_y, brick_z = 3, 5, 6 # Yes!
# brick_x, brick_y, brick_z = 3, 6, 5 # Yes!
# brick_x, brick_y, brick_z = 6, 3, 5 # Yes!
# brick_x, brick_y, brick_z = 6, 5, 3 # Yes!
# brick_x, brick_y, brick_z = 5, 6, 3 # Yes!
# brick_x, brick_y, brick_z = 5, 3, 6 # Yes!
# brick_x, brick_y, brick_z = 11, 3, 6 # Yes!
# brick_x, brick_y, brick_z = 11, 6, 3 # Yes!
# brick_x, brick_y, brick_z = 6, 11, 3 # Yes!
# brick_x, brick_y, brick_z = 6, 3, 11 # Yes!
# brick_x, brick_y, brick_z = 3, 6, 11 # Yes!
# brick_x, brick_y, brick_z = 3, 11, 6 # Yes!
# (просто раскоментировать нужную строку и проверить свой код)

if (brick_x < hole_x and brick_y < hole_y) or (brick_y < hole_x and brick_z < hole_y) or (brick_z < hole_x and brick_x < hole_y):
    print('Yes!')
else:
    print('No!')
