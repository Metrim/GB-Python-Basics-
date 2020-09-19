# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

from googletrans import Translator


translator = Translator()
with open("text_4.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
    print(f"Считанный из файла текст: {text}")
    for i in range(0, len(text)):
        text[i] = text[i].rstrip("\n").split()
    print(f"Преобразованный текст: {text}")
    for i in range(0, len(text)):
        text[i][0] = translator.translate(text[i][0], dest='ru').text
    print(f"Переведенный текст: {text}")

with open("text_4_1.txt", "w", encoding="utf-8") as file:
    for i in range(0, len(text)):
        print(' '.join(text[i]), file=file)

# Или можно короче:

with open("text_4.txt", "r", encoding="utf-8") as file:
    text = file.read()
with open("text_4_2.txt", "w", encoding="utf-8") as file:
    file.write(translator.translate(text, dest="ru").text)
