# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod


class Warehouse:
    def __init__(self):
        self.assets = {
                        "Warehouse": {'Printer': [], 'Scaner': [], 'Xerox': []},
                        "IT": {'Printer': [], 'Scaner': [], 'Xerox': []},
                        "Accounting": {'Printer': [], 'Scaner': [], 'Xerox': []},
                        "RnD": {'Printer': [], 'Scaner': [], 'Xerox': []}
                       }

    def getting_stuff(self, desti, source_type, el):
        self.assets[desti][source_type].append(el)

    def move_asset(self, source, desti, source_type, amount):
        if len(self.assets[source][source_type]) - int(amount) >= 0:
            for _ in range(0, int(amount)):
                self.assets[desti][source_type].append(self.assets[source][source_type].pop())
        else:
            print(f"Not enough devices {source_type} to move!")

    def __str__(self):
        temp_str = []
        for k1 in self.assets.keys():
            temp_str.append(f"{k1}:")
            for k2 in self.assets[k1].keys():
                temp_str.append(f"{k2}:")
                for el in self.assets[k1][k2]:
                    temp_str.append(f"{el.name},")
            temp_str.append("|")
        return " ".join(temp_str)


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


class Printer(OfficeEquipment):
    def __init__(self, name, type, toner_level):
        super().__init__(name, type)
        self.__toner_lvl = int(toner_level)

    def working(self):
        print(f"Printer {self.name} is printing {self.type} content. Toner level is {self.__toner_lvl}")
        self.__toner_lvl -= 1
        if self.__toner_lvl < 10:
            Printer.errorInform()

    def errorInform(self):
        print("Low toner")

    def __str__(self):
        return self.name


class Scaner(OfficeEquipment):
    def __init__(self, name, type):
        super().__init__(name, type)

    def working(self):
        print(f"Scaner {self.name} is scanning with {self.type}.")

    def __str__(self):
        return self.name

    def errorInform(self):
        pass


class Xerox(OfficeEquipment):
    def __init__(self, name, type, toner_level):
        super().__init__(name, type)
        self.__toner_lvl = int(toner_level)

    def working(self):
        print(f"Xerox {self.name} is copying with {self.type}. Toner level is {self.__toner_lvl}")
        self.__toner_lvl -= 1
        if self.__toner_lvl < 10:
            Printer.errorInform()

    def errorInform(self):
        print("Low toner")

    def __str__(self):
        return self.name


my_print_0 = Printer("HP", "Color", 100)
my_print_1 = Printer("HP2", "Color", 80)
my_print_2 = Printer("Hewlett", "Black&White", 100)
my_print_3 = Printer("Hewlett", "Black&White", 100)
my_print_4 = Printer("Lexmark", "Color", 100)
my_print_5 = Printer("Panasonic", "Color", 80)
my_print_6 = Printer("Samsung", "Black&White", 100)

my_scanner_0 = Scaner("HP", "Color")
my_scanner_1 = Scaner("HP2", "Color")
my_scanner_2 = Scaner("Hewlett", "Black&White")
my_scanner_3 = Scaner("Hewlett", "Black&White")
my_scanner_4 = Scaner("Lexmark", "Color")
my_scanner_5 = Scaner("Panasonic", "Color")
my_scanner_6 = Scaner("Samsung", "Black&White")

my_xerox_0 = Xerox("HP", "Black&White", 8)
my_xerox_1 = Xerox("HP2", "Black&White", 50)
my_xerox_2 = Xerox("Hewlett", "Black&White", 80)
my_xerox_3 = Xerox("Hewlett", "Black&White", 80)
my_xerox_4 = Xerox("Lexmark", "Color", 45)
my_xerox_5 = Xerox("Panasonic", "Color", 100)
my_xerox_6 = Xerox("Samsung", "Black&White", 65)

my_warehouse = Warehouse()
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_0)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_1)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_2)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_3)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_4)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_5)
my_warehouse.getting_stuff("Warehouse", "Printer", my_print_6)

my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_0)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_1)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_2)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_3)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_4)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_5)
my_warehouse.getting_stuff("Warehouse", "Scaner", my_scanner_6)

my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_0)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_1)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_2)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_3)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_4)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_5)
my_warehouse.getting_stuff("Warehouse", "Xerox", my_xerox_6)

print(my_warehouse)

while True:
    my_data = input("Please Enter: \nSHOW- to see warehouse \nMOVE - to move assets\nEXIT - to exit\n")
    if my_data.upper() == "EXIT":
        print(my_warehouse)
        break
    elif my_data.upper() == "SHOW":
        print(my_warehouse)
    elif my_data.upper() == "MOVE":
        while True:
             my_data = input(f"Please Enter: \nFrom where to move: {my_warehouse.assets.keys()} \n"
                            f"Where to move: {my_warehouse.assets.keys()} \n"
                            f"What to move: {my_warehouse.assets['Warehouse'].keys()} \n"
                            f"Enter how many to move\n"
                            f"Or type MENU - to get to menu\n")
             if my_data.upper() == "MENU":
                break
             source, desti, source_type, amount = my_data.split()
             my_warehouse.move_asset(source, desti, source_type, amount)
