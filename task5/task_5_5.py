# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


result = 0
with open("file05.txt", "w+", encoding="utf-8") as file:
    for _ in range(0, int(input("Сколько чисел записать в файл? "))):
        print(randint(0, 2020), file=file, end=" ")
    file.seek(0)
    arr = file.readline().split()
    for i in range(0, len(arr)):
        result += int(arr[i])
    print(f"Сумма элементов в файле: {result}")
