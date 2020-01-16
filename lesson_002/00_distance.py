#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# Long string variant
# moscow_london = ((sites.get('Moscow')[0] - sites.get('London')[0]) ** 2 + (sites.get('Moscow')[1] - sites.get('London')[1]) ** 2) ** 0.5
# moscow_paris = ((sites.get('Moscow')[0] - sites.get('Paris')[0]) ** 2 + (sites.get('Moscow')[1] - sites.get('Paris')[1]) ** 2) ** 0.5
# london_paris = ((sites.get('London')[0] - sites.get('Paris')[0]) ** 2 + (sites.get('London')[1] - sites.get('Paris')[1]) ** 2) ** 0.5

moscow = sites ['Moscow']
london = sites ['London']
paris = sites ['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** .5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['London'] = london_paris
distances['Paris']['Moscow'] = moscow_paris

pprint(distances)

print(distances['Moscow']['Paris'])


