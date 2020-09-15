def my_fun(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Вы ввели аргументы для деления на ноль!")


print(my_fun(int(input("Введите первое число ")), int(input("Введите второе число "))))
