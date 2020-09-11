my_list = [7, 5, 3, 3, 2]

while True:
    my_num = input("Введите новый элемент рейтинга, или введите exit: ")
    flag = True
    if my_num == "exit":
        break
    for i in range(0, len(my_list)):
        if int(my_num) > my_list[i]:
            my_list.insert(i, int(my_num))
            flag = False
            break
    if flag:
        my_list.append(int(my_num))
print(f"Списко рейтинга чисел выглядит таким образом: {my_list}")