goods= []
# piece = (1, {})
my_key = 1
while True:
    name = input("Введите новое название товара, или введите exit: ")
    if name == "exit":
        break
    price = int(input("Введите цену товара "))
    amount = int(input("Введите количество товара "))
    measure = input("Введите единицу измерения товара ")
    goods.append((my_key, {"название": name, "цена": price, "количество": amount, "eд": measure}))
    my_key += my_key

analytics = {
    "название": [],
    "цена": [],
    "количество": [],
    "eд": []
}

for el in goods:
    for k in analytics.keys():
        analytics[k].append(el[1][k])

print(goods)
print(analytics)
