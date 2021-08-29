def my_func(a, b, c):
    return a + b + c - min(a, b, c)


print(f"Сумма введенных двух наибольших чисел: {my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: ')))}")
