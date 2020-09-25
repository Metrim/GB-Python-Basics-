# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "Handle"

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Запуск отрисовки {type(self)} И {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {type(self)} И {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {type(self)} И {self.title}")


stat_0 = Stationery("Базовый")
stat_1 = Pen("Дочерний №1")
stat_2 = Pencil("Дочерний №2")
stat_3 = Handle("Дочерний №3")

my_list = [stat_0, stat_1, stat_2, stat_3]

for el in my_list:
    el.draw()
