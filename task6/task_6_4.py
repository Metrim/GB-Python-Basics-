# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import randint
import time


class Car:
    speed = 0
    color = "def"
    name = "def"
    is_police = False

    def __init__(self, speed, color, name):
        self.speed, self.color, self.name = speed, color, name

    def go(self):
        print(f"Машина {self.name} тронулась")

    def stop(self):
        print(f"Машина {self.name} встала")

    def turn(self, direction):
        print(f"Машина {self.name} поехала {direction}")

    def show_speed(self):
        print(f"Текущая скорость у {self.name}: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("У вас превышение - уменьшите скорость")
        else:
            print(f"Текущая скорость у {self.name}: {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("У вас превышение - уменьшите скорость!")
        else:
            print(f"Текущая скорость: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name)
        self.is_police = True


my_town = TownCar(70, "White", "Mazda3")
my_sport = SportCar(180, "Red", "Audi R8")
my_work = WorkCar(35, "Green", "Ford")
my_cop = PoliceCar(100, "Black", "Police")

cars = [my_cop, my_town, my_sport, my_work]
dirs = ["Налево", "Вправо", "Назад", "Прямо"]

while True:
    for el in cars:
        el.go()
        el.stop()
        el.turn(dirs[randint(0, 3)])
        el.show_speed()
    time.sleep(1)
    my_town.speed = randint(0, 180)
    my_sport.speed = randint(0, 350)
    my_work.speed = randint(0, 80)
    my_cop.speed = randint(0, 280)

