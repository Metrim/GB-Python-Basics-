calendar = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month = input("Введите, пожалуйста, номер месяца от 1 до 12: ")
month = int(month)
for k in calendar.keys():
    for m in calendar[k]:
        if month == m:
            print(f"Вы ввели время года: {k}")
            break
