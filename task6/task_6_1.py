# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]
    __current_col = 0

    def running(self):
        if TrafficLight.__current_col == 0:
            TrafficLight.__current_col = 1
            return self.__color[0]
        elif TrafficLight.__current_col == 1:
            TrafficLight.__current_col = 2
            return self.__color[1]
        else:
            TrafficLight.__current_col = 0
            return self.__color[2]


lighter = TrafficLight()

while True:
    print(lighter.running())
    time.sleep(7)
    print(lighter.running())
    time.sleep(2)
    print(lighter.running())
    time.sleep(1)
