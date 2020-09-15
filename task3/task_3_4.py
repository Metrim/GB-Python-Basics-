def my_pow(x, y):
    return 1 / x ** abs(y) if y != 0 else 1


def my_pow_second(x, y):
    for i in range(1, abs(y)):
        x *= x
    return 1 / x if y != 0 else 1

print(f"Итоговое значение числа в отрицательной степени: {my_pow(int(input('Введите число ')), int(input('Введите отрицательную степень ')))}")
print(f"Итоговое значение числа в отрицательной степени второй способ: {my_pow_second(int(input('Введите число ')), int(input('Введите отрицательную степень ')))}")

