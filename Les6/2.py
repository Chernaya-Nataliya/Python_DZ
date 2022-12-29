# Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

from memory_profiler import profile
from copy import deepcopy

@profile
def function_1():
    x = list(range(10000))
    y = deepcopy(x)
    return y

@profile
def my_func(a, b, c):
    return a + b + c - min(a, b, c)

@profile
def my_func1(a, b, c):
    sorted_list = sorted([a, b, c])
    y = deepcopy(sorted_list)
    return sorted_list[1] + sorted_list[2]

@profile
def list_of_seasons(number):
    if 1 <= number <= 12:
       list_of_seasons = ['зима', 'зима', 'весна', 'весна',
                      'весна', 'лето', 'лето', 'лето',
                      'осень', 'осень', 'осень', 'зима']
       return list_of_seasons[number - 1]
    else:
        print("Ошибка в месяце")

@profile
def dict_of_seasons(number):
    if 1 <= number <= 12:
        dict_of_seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
        return dict_of_seasons[number]
    else:
        print("Ошибка в месяце")

"""Тестирование в выбранных алгоритмах показало одинаковый результат"""