# Task №1
number_one = 5
number_two = 8
number_three = 3

print('Сумма чисел:', number_one + number_two + number_three)
print('Разность чисел:', number_one - number_two - number_three)
print('Произведение чисел:', number_one * number_two * number_three)

# Oт первой переменной отнять вторую и прибавить третью
print('Результат:', number_one - number_two + number_three)

# Поделить произведение двух переменных на третью
print('Результат:', (number_one * number_two) / number_three)

# Oт суммы первых двух переменных найти остаток от деления на третью переменную
print('Результат:', (number_one + number_two) % number_three)

# Task №2
cat_a = 3
cat_b = 4

# Формула площади прямоугольного треугольника (a*b)/2
print('Площадь треугольника:', (cat_a * cat_b) / 2)

# Формула гипотенузы sqrt(a^2 + b^2)
print('Гипотенуза:', (cat_a ** 2 + cat_b ** 2) ** (1 / 2))

# Task №3
first_str = 'Hello world'
second_str = 'a b c'
third_str = 'test'
fourth_str = 'test1 test2 test3 test4 test5'

print('Количество слов в 1 строке:', first_str.count(' ') + 1)
print('Количество слов в 2 строке:', second_str.count(' ') + 1)
print('Количество слов в 3 строке:', third_str.count(' ') + 1)
print('Количество слов в 4 строке:', fourth_str.count(' ') + 1)

# Task №4
some_str = 'hhhaahhahh'

# Заменяем все символы 'h' на 'H', кроме последнего
modified_str = some_str.replace('h', 'H', some_str.count('h') - 1)

# Затем заменяем первый символ 'H' на 'h'
print('Преобразованная строка:', modified_str.replace('H', 'h', 1))

# Task №5
some_str = 'Hello'

# Сначала выведите третий символ этой строки.
print(some_str[2])

# Во второй строке выведите предпоследний символ строки.
print(some_str[-2])

# В третьей строке выведите первые пять символов строки.
print(some_str[:5])

# В четвертой выведите всю до последних двух символов.
print(some_str[:-2])

# В пятой строке выведите все символы с четными индексами.
print(some_str[::2])

# В шестой строке выведите все символы с нечетными индексами.
print(some_str[1::2])

# В седьмой строке выведите все символы в обратном порядке.
print(some_str[::-1])

# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print(some_str[::-2])

# В девятой строке выведите длину данной строки.
print(len(some_str))

# Task №6
number = 123

print('Последняя цифра числа:', number % 10)

# Task №7
number = 567

print('Количество десятков в числе', number, ':', (number % 100) // 10)

# Task №8
number = 123

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

print('Сумма цифр трехзначного числа:', first_digit + second_digit + third_digit)
