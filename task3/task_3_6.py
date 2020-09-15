def correct_string(my_str):
    my_list = []
    my_str = my_str.split()
    for word in my_str:
        for letter in word:
            if ord(letter) > 122 or ord(letter) < 97:
                break
            elif letter == word[- 1]:
                my_list.append(word)
    return ' '.join(my_list)


def int_func(my_str):
    return my_str.title()


print(f"Ваша строка:  {int_func(correct_string(input('Введите строку ')))}")
