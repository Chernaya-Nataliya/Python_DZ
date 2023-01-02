# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки. Название: {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой. Название: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом. Название: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером. Название: {self.title}'


s = Stationery('Стандарт')
p_1 = Pen('Parker')
p_2 = Pencil('Цветные карандаши')
h = Handle('Touch Raven')


print(s.draw(), p_1.draw(), p_2.draw(), h.draw(), sep='\n')