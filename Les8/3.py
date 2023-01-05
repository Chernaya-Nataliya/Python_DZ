"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Division_Null(Exception):
    def __init__(self, txt):
        self.txt = txt

def div_null():
    try:
        divisible = float(input('Введите делимое: '))
        divider = float(input('Введите делитель: '))
        if divider == 0:
            raise Division_Null(f'На ноль делить нельзя.')
        else:
            return divisible / divider
    except ValueError:
        return "Вы промахнулись и не ввели число"
    except Division_Null as err:
        return err

print(div_null())