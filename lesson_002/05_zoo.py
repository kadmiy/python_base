#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

print('Default Zoo')
print(zoo)

print('Adding a bear to the Zoo')
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

print('Adding birds to the Zoo')
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль

print('Removing the elephant from the Zoo')
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

print('Count of Lion''s in zoo... = ', zoo.count('lion'))
print('The lion is sitting in cage', zoo.index('lion') + 1)

print('Count of Lark''s in zoo... = ', zoo.count('lark'))
print('The lark is sitting in cage', zoo.index('lark') + 1)
