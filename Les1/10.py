# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_num = int(input('Введите номер четверти системы коорддинат: '))
if coordinate_num == 1:
    print('Диапазон для координат точек в первой четверти составляет X > 0 и Y > 0')
elif coordinate_num == 2:
    print('Диапазон для координат точек в второй четверти составляет X < 0 и Y > 0')
elif coordinate_num == 3:
    print('Диапазон для координат точек в третьей четверти составляет X < 0 и Y < 0')
elif coordinate_num == 4:
    print('Диапазон для координат точек в четвертой четверти составляет X > 0 и Y < 0')
else:
    print(f'В данной системе есть только четыре четверти, вы ввели {coordinate_num}')