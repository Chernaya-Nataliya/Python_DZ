#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_num = input('Введдите число: ')
user_transformation = int(user_num) + int(user_num * 2) + int(user_num * 3)
print(f'Сумма чисел по формуле n + nn + nnn для числа {user_num} равна {user_transformation} ')