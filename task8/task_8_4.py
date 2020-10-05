# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        pass


class OfficeEquipment(ABC):
    @abstractmethod
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @abstractmethod
    def working(self):
        pass

    @abstractmethod
    def errorInform(self):
        pass

    def __str__(self):
        return self.name


class Printer(OfficeEquipment):
    def __init__(self, name, type, toner_level):
        super().__init__(name, type)
        self.__toner_lvl = int(toner_level)

    def working(self):
        print(f"Printer {self.name} is printing {self.type} content. Toner level is {self.__toner_lvl}")
        self.__toner_lvl -= 1

    def errorInform(self):
        pass


class Scaner(OfficeEquipment):
    def __init__(self, name, type):
        super().__init__(name, type)

    def working(self):
        print(f"Scaner {self.name} is scanning with {self.type}.")

    def errorInform(self):
        pass


class Xerox(OfficeEquipment):
    def __init__(self, name, type, toner_level):
        super().__init__(name, type)
        self.__toner_lvl = int(toner_level)

    def working(self):
        print(f"Xerox {self.name} is copying with {self.type}. Toner level is {self.__toner_lvl}")
        self.__toner_lvl -= 1

    def errorInform(self):
        pass

