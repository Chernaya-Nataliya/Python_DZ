# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

f = open('Les5_1.txt', 'w', encoding='utf-8')
print("Введите данные в файл. Пустая строка для выхода: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()