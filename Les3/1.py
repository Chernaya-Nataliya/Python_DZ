# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(divisible,divider):          
    try:
        return divisible/divider
    except ZeroDivisionError:
        print('Ошибка! Делить на ноль нельзя!')  

divisible = float(input('Введите делимое: '))
divider = float(input('Введите делитель: '))
print(division(divisible, divider))              