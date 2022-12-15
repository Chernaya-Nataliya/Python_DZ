# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month = 0 

while month not in range(1, 13):
    month = int(input("Введите порядковый номер месяца: "))
    if month not in range(1, 13):
        print("Ошибка. Введите от 1 до 12, так как в году 12 месяцев.")

list_of_seasons = ["зима", "весна", "лето", "осень"]
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]

if month in winter:
    print(list_of_seasons[0])
elif month in spring:
    print(list_of_seasons[1])
elif month in summer:
    print(list_of_seasons[2])
else:
    print(list_of_seasons[3])



dict_of_seasons = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for season, months in dict_of_seasons.items():
    if month in months:
        print(season)