# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r"testex2.txt",  'w', encoding='utf-8') as text:
    user_text = input('Введите текст. Пустая строка заканчивает ввод: ')
    while user_text:
        text.write(user_text + '\n') 
        user_text = input('Введите текст \n')
        if not user_text:
            break    

with open(r"testex2.txt") as text:
    f_text = text.readlines() 
    print(f'Всего в файле {len(f_text)} строки')
    for i, j in enumerate(f_text):
                print(f"В строке {i + 1}: {len(j.split())} слов(а)")