from math import sqrt, sin, cos, radians, pi

"""
Task №1
Calculating the values of equations
y... from 1a) - first_equation
y... from 1b) - second_equation
y... from 1c) - third_equation
y... from 1d) - fourth_equation
"""
a = float(input('Enter a: '))
b = float(input('Enter b: '))
x = radians(float(input('Enter x: ')))

first_equation = ((a ** 2) / 3) + (((a ** 2) + 4) / b) + (sqrt((a ** 2) + 4) / 4) + (sqrt(((a ** 2) + 4) ** 3) / 4)
second_equation = cos(x) + sin(x)
third_equation = (((cos(x ** 2)) ** 2) + (sin(2 * x - 1)) ** 2) ** (1 / 3)
fourth_equation = (5 * x) + (3 * (x ** 2)) * sqrt(1 + (sin(x)) ** 2)

print('Our first equation from task 1a) is equal to:', first_equation)
print('Our second equation from task 1b) is equal to:', second_equation)
print('Our third equation from task 1c) is equal to:', third_equation)
print('Our fourth equation from task 1d) is equal to:', fourth_equation)

# Task 2 "Играл с кредитами – проиграл"
i = float(input('Введите годовую процентную ставку: '))
s = float(input('Введите сумму займа: '))
n = int(input('Введите количество месяцев: '))

p = i / 12 / 100  # Месячная процентная ставка
m = (p * s * (1 + p) ** n) / ((1 + p) ** n - 1)  # Ежемесячная выплата

total_payment = m * n  # Общая сумма выплат
overpayment = total_payment - s  # Переплата

print('--- Результаты расчета кредита ---')
print('Ежемесячная выплата:', m)
print('Общая сумма выплат:', total_payment)
print('Переплата:', overpayment)

"""
Task №3 «Интерстеллар»
L - ..._year_length
R - ..._radius
V - ..._velocity
"""
print('--- Первая планета---')
first_radius = float(input('Введите радиус первой планеты (в млн. км): '))
first_velocity = float(input('Введите орбитальную скорость первой планеты (в км/ч): '))
print('--- Вторая планета---')
second_radius = float(input('Введите радиус второй планеты (в млн. км): '))
second_velocity = float(input('Введите орбитальную скорость второй планеты (в км/ч): '))

print('--- Результаты ---')
first_year_length = (2 * (first_radius * (10 ** 6)) * pi) / first_velocity
print('Длина года на первой планете в часах:', first_year_length)

second_year_length = (2 * (first_radius * (10 ** 6)) * pi) / second_velocity
print('Длина года на второй планете в часах:', second_year_length)

print('Правда ли, что на первой планете год длиннее, чем на второй:', first_year_length > second_year_length)
