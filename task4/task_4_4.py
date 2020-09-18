def compare(l_list):
    for i in range(0, len(l_list)):
        if l_list.count(l_list[i]) == 1:
            yield l_list[i]


init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(f"Original: {init_list}, replaced: {list(el for el in compare(init_list))}")
