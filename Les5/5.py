# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

n = int(input("Введите количество записываемых чисел: "))
numbers = [str(randint(0, 100)) for i in range(n)]
with open(r'python_dz\les5\les5_5.txt', 'w', encoding='utf-8') as txt:
    txt.write(' '.join(numbers))

with open(r'python_dz\les5\les5_5.txt', 'r', encoding='utf-8') as txt:
    content = list(map(int, txt.read().strip().split()))
    print(f'Сумма чисел равна {sum(content)}')