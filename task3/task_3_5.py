my_numsum = 0
FLAG = True


def my_sum(*args):
    global my_numsum
    for i in range(0, len(args[0])):
        my_numsum += int(args[0][i])
    return my_numsum


while FLAG:
    numbers = input('Введите числа через пробел или exit для выхода ').split()
    if numbers.count("exit"):
        FLAG = False
        for i in range(numbers.index("exit"), len(numbers)):
            numbers.pop()
    print(f"Сумма введенных чисел: {my_sum(numbers)}")
