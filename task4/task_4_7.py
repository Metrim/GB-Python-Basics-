from math import factorial


def fact(n):
    for i in range(0, n + 1):
        yield factorial(i)


print(list([el for el in fact(int(input("Введите конечное число списка факториалов ")))]))
