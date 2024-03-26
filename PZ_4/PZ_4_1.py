# Вариант 3.
# 1.	Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, ..., 10 кг конфет.
# 2.	Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить,
#       имеется ли в записи числа N цифра «2». Если имеется, то вывести TRUE, если нет — вывести FALSE.


#1

price = input("Введите стоимость одного килограмма конфет: ")

while type(price) != int:
    try:
        price = int(price)
    except ValueError:
        print("Вы ввели не целое число!")
        price = input("Введите стоимость одного килограмма конфет: ")

a = []
for i in range(1, 11):
    a.append(int(price) * i)

print('Стоимость 1, 2, ..., 10 килограммов конфет: ', a)


#2

n = input("Enter n>0: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Вы ввели не целое число!")
        n = input("Enter n>0: ")

while n > 0:
    if n % 10 == 2:
        print("TRUE")
        break
    n = n // 10
else:
    print("FALSE")
