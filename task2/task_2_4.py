my_string = input("Ввдеите строку из слов ").split()

for i in range(0, len(my_string)):
    print(f"Строка №{i + 1}: {my_string[i][:10]}")
