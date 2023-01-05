"""Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell). В его конструкторе инициализировать параметр (quantity), соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

** - По желанию: В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: **\n\n***.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print()

print("Складываем")
print(cell1 + cell2)

print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))

Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

Организация ячеек по рядам
**\n *\n *\n *\n *\n *\n
******\n ****\n **
"""

class Organic_cell(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка не может иметь меньше одной ячейки')
        self.size = size

    def __add__(self, other):
        return Organic_cell(self.size + other.size)

    def __sub__(self, other):
        result = self.size - other.size
        if result > 0:
            return Organic_cell(result)
        else:
            raise Exception(f'Ошибка! Вычитание {self} из {other} невозможно!')

    def __mul__(self, other):
        return Organic_cell(self.size * other.size)

    def __truediv__(self, other):
        return Organic_cell(self.size // other.size)

    def make_order(self, row_size: int) -> str:
        rows = ['*' * row_size for _ in range(self.size // row_size)]
        tail = '*' * (self.size % row_size)
        rows.append(tail)
        return '\n'.join(rows)

    def __str__(self):
        return '*' * self.size


if __name__ == '__main__':
    size_cell = int(input('Введите размер первой клетки: '))
    size_cell2 = int(input('Введите размер второй клетки: '))
    infusorium_1 = Organic_cell(size_cell)
    infusorium_2 = Organic_cell(size_cell2)
    infusorium_add = infusorium_1 + infusorium_2
    try:
        infusorium_sub1 = infusorium_1 - infusorium_2
    except Exception as e:
        infusorium_sub1 = None
        print(e)
    infusorium_sub2 = infusorium_2 - infusorium_1
    infusorium_mul = infusorium_1 * infusorium_2
    infusorium_div = infusorium_2 / infusorium_1

    print('infusorium_1:', infusorium_1)
    print('infusorium_2:', infusorium_2)
    print('Сложение:', infusorium_add)
    print('Вычитание из первой клетки вторую:', infusorium_sub1)
    print('Вычитание из второй клетки первую:', infusorium_sub2)
    print('Умножение клеток:', infusorium_mul)
    print('Деление клеток:', infusorium_div)


    infusorium_3 = Organic_cell(int(input('Какой размер клетки: ')))
    row_cell = int(input('Сколько клеток должно быть в ряду: '))
    order = infusorium_3.make_order(row_cell)
    print(f'\norder\n{order}')