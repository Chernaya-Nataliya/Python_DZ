# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('Les5_2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'Всего строк: {len(lines)}')
    for key, value in enumerate(lines):
        words = value.split(' ')
        print(f"Слов в строке {key + 1}: {len(words)}")