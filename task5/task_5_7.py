# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

companies = {}
av_profit = {"average_profit": 0}
analitics = [companies, av_profit]
profitable_companies = 0

with open("text_7.txt", "r", encoding="utf-8") as file:
    for el in file:
        com_name, comp_form, profit, costs = el.split()
        companies[com_name] = int(profit) - int(costs)
        print(f"Прибыль компании {com_name} составляет: {int(profit) - int(costs)}")
        if int(profit) - int(costs) > 0:
            av_profit["average_profit"] += companies[com_name]
            profitable_companies += 1

    av_profit["average_profit"] = av_profit["average_profit"] / profitable_companies
    print(analitics)

with open("text_7_1.json", "w") as file:
    json.dump(analitics, file, ensure_ascii=False)
