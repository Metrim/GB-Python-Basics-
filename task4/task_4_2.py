import random

init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(init_list)


def gen(l_list):
    for i in range(1, len(l_list)):
        if l_list[i] > l_list[i - 1]:
            yield l_list[i]


def list_gen(length):
    for i in range(0, length):
        yield random.randint(0, 1000)


my_list = [el for el in gen(init_list)]

print(my_list)

init_list = [el for el in list_gen(25)]

print(init_list)

print(list(el for el in gen(init_list)))
