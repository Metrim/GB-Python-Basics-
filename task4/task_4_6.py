from itertools import count, cycle


def gen(start, end):
    for el in count(start):
        if el > end:
            break
        yield el


def rep(my_str, amount):
    c = 0
    for el in cycle(my_str):
        if c > amount:
            break
        print(el)
        c += 1


init_str = [el for el in gen(int(input("Введите начальное число списка ")), int(input("Введите конечное число списка ")))]

print(f"Your list: {init_str}")

rep(init_str, int(input("Введите сколько раз необходимо повторить элементы сгенерированного списка ")))
