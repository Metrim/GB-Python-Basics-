# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open("file02.txt", "r", encoding="utf-8") as file:
    texts = file.readlines()
    print(texts)
    reformat_text = []
    for i in range(0, len(texts)):
        if texts[i] == "\n":
            continue
        reformat_text.append(texts[i].rstrip("\n"))
    print(reformat_text)
    print(f"Количество строк с текстом: {len(reformat_text)}")
    for i in range(0, len(reformat_text)):
        print(f"Количество символов в {i + 1}-й строке: {len(reformat_text[i])}")
