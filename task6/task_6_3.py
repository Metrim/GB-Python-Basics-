# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name = "default"
    surname = "default"
    position = "default"
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"], self._income["bonus"] = wage, bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname


    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

my_emp = Position(input("Имя: "), input("Фамилия: "), input("Должность: "), int(input("Зарплата: ")), int(input("Бонус: ")))

print(f"Полное имя: {my_emp.get_full_name()}, Полная зарплата: {my_emp.get_total_income()}")
