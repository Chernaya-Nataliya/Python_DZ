# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

k = []  

k.append(54)
k.append(65.7)
k.append('mama')
k.append([54, 65.7, 'mama'])
k.append((54, 65.7, 'mama'))
k.append({3, 5, 3, 7, 7, 7, 9, 1})
k.append(frozenset([3, 5, 3, 7, 7, 7, 9, 1]))
k.append(complex(5, -1))
k.append(None)
k.append(True)
k.append(b'Byte text')
k.append(bytearray(b'Byte text'))

for i in k:
    print(i, type(i))