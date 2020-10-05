# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, n, j):
        self.__n = n
        self.__j = j

    def __add__(self, other):
        return ComplexNumber(self.__n + other.__n, self.__j + other.__j)

    def __mul__(self, other):
        return ComplexNumber(self.__n * other.__n - self.__j * other.__j, self.__n * other.__j + other.__n * self.__j)

    def __str__(self):
        return f"{self.__n}{self.__j:+d}i"


num_0 = ComplexNumber(5, 4)
num_1 = ComplexNumber(1, -7)
print(num_0 + num_1)
print(num_0 * num_1)
