#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Введите количество секунд: '))

hours = user_time // 3600
minuts = (user_time - hours * 3600) // 60
seconds = (user_time - hours * 3600 - minuts * 60)
print(f'{user_time} секунд в формате чч:мм:сс имеет вид {hours}ч: {minuts}мин: {seconds}сек')