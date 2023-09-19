# num_1 = int(input('Введи диаметр окружности: '))
# if num_1 > 0:
#     choice = int(input('1-площадь\n2-периметр'))
#     if choice == 1:
#         print(3.14 * num_1  / 4 )
#     elif choice == 2:
#         print(2  *  3.14 * (num_1/2))
#     else:
#         print('нет такого варианта')
# else:
#     print('ошибка')

# price = int(input("Введи стоимость игровой приставки: "))
# amount = int(input("Введи количество приставок: "))
# discount = int(input("Введи процент скидки: "))
# if price > 0 and amount > 0 and 100 > discount >= 0:
#     choice = int(input('1-full price\n2-одна приставка'))
#     if choice == 1:
#         print(price * amount)
#     elif choice == 2:
#         print(price - (price * discount / 100))
#     else:
#         print('ошибка')
# else:
#     print('ошибка')

# razmer = float(input("Введи размер файла: "))
# scororst = float(input("Введи скорость интернета: "))
# if razmer > 0 and scororst > 0:
#     choice = int((input('1-минута\n2-секунда\n3-часы')))
#     if choice == 2:
#         print(razmer/scororst/60)
#     elif choice == 1:
#         print(razmer/scororst)
#     elif choice == 3:
#         print(razmer/scororst/3600)
#     else:
#         print('ты ввел неверно')
# else:
#     print('ввод не верен')

#Задание 5
# hours = int(input('Enter hours: '))
# if 6 > hours >= 0:
#     print('Good Night')
# elif 13 > hours >= 6:
#     print('Good Morning')
# elif 17 > hours >= 13:
#     print('Good Day')
# elif 24 > hours >= 17:
#     print('Good Evining')
# else:
#     print('Incorrect Input')