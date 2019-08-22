# easy
# task1

varNumber = 50
print(varNumber)

vartxt = 'Hello teacher'
print(vartxt)

varfl = 333.3
print(varfl)

varBol = True
if varBol == True:
    print('Правильно')

planet = input('Назовите планету, на которой вы живете: ')
print(planet)

# task2

number = int(input('Введите произвольное число: '))
print('Я прибавил к вашему числу 2 и получилось:', number + 2)

age = int(input('Сколько вам лет?: '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

# normal
# task1

number = int(input('Введите число больше 0, но меньше 10: '))

while number < 1 or number > 9:
    print('Неверно, повторите')
    number = int(input('Введите число больше 0, но меньше 10: '))
else:
    print('Число',number,'возведенное в степень 2, будет равняться', number ** 2 )

# task2

var1 = int(input('Введите первое число: '))
var2 = int(input('Введите второе число: '))

var1 = var1 + var2
var2 = var1 - var2
var1 = var1 - var2

print('Теперь первое число равно', var1, ',а второе число равно', var2)

# hard

name = str(input('Ваше имя: '))
surname = str(input('Ваша фамилия: '))
age = int(input('Ваш возраст:'))
weight = int(input('Ваш вес: '))

if age >= 18 and age <= 25:
    if weight >= 70 and weight <= 80:
        print('Здоров')
    elif weight > 80:
        print('Необходимо заняться ЗОЖ ')
    elif weight < 70:
        print('Необходимо обратиться к врачу ')
elif age >= 25 and age <= 40:
    if weight >= 70 and weight <= 90:
        print('Здоров')
    elif weight > 90:
        print('Необходимо заняться ЗОЖ ')
    elif weight < 70:
        print('Необходимо обратиться к врачу ')
elif age >= 41 and age <= 60:
    if weight >= 70 and weight <= 100:
        print('Здоров')
    elif weight > 100:
        print('Необходимо заняться ЗОЖ ')
    elif weight < 70:
        print('Необходимо обратиться к врачу ')