# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

user_list = []

def get_list(num, num2):
    for item in count(num):
        if item > num2:
            break
        else:
            user_list.append(item)
            print(item)
    return user_list

def get_repeat(user_list,user_num):
    for i, j in enumerate(cycle(user_list)):
        print(j, end=' ')        
        if i > user_num + 1: 
            print()       
            break             

user_num = int(input('Введите начальное число: '))
user_num2 = int(input('Введите конечное число элемента: '))
get_list(user_num,user_num2)
print(f'Полученный список: {user_list}')

user_num3 = int(input('Сколько элементов повторить: '))        
received = get_repeat(user_list,user_num3)