from functools import reduce


def multi(param1, param2):
    return param1 * param2


init_list = [el for el in range(100, 1001) if el % 2 == 0]

print(init_list)

print(reduce(multi, init_list))
