print("Введите элементы списка, для окончания ввдоа введите слово exit")
my_list = []

while True:
    temp = input("Введите элемент, для выхода exit: ")
    if temp == "exit":
        break
    my_list.append(temp)

print(f"Вы ввели список: {my_list}")

for i in range(0, len(my_list) - 1):
    if i % 2 == 0:
        temp = my_list[i + 1]
        my_list[i + 1] = my_list[i]
        my_list[i] = temp
print(f"Список после изменения пар элементов: {my_list}")
