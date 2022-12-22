# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) > 1:
    name_script, work_hours, rate, reward = argv
    work_hours = int(work_hours)
    rate = int(rate)
    reward = int(reward)
    print((work_hours * rate) + reward)
else:
    work_hours = int(input("Введите количество отработанных часов: "))
    rate = int(input("Введите суммы оплаты труда за 1 час: "))
    reward = int(input("Укажите размер премии: "))
    print((work_hours * rate) + reward)