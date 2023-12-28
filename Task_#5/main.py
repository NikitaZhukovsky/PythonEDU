import math

# Task 1
x = math.radians(int(input('Введите x (в градусах): ')))

accuracy = 0.01
next_term_sin = 1
next_term_cos = 1
sin = 0
cos = 0
n = 0  # cтепень для sin(x)
i = 0  # степень для cos(x)

while abs(next_term_sin) > accuracy or abs(next_term_cos) > accuracy:
    if abs(next_term_sin) > accuracy:
        next_term_sin = ((-1) ** n) * ((x ** (2 * n + 1)) / math.factorial(2 * n + 1))
        sin += next_term_sin
        n += 1

    if abs(next_term_cos) > accuracy:
        next_term_cos = ((-1) ** i) * ((x ** (2 * i)) / math.factorial(2 * i))
        cos += next_term_cos
        i += 1

print(f"The output of the sin(x) value is {sin}")
print(f"The output of the cos(x) value is {cos}")

# Task 2
final_amount = int(input("Введите сумму, которую Маша хочет накопить: "))
day_amount = int(input("Введите сумму, которую Маша откладывает каждый день: "))

days = 0
saved_amount = 0

while saved_amount < final_amount:
    days += 1
    if days % 7 != 0:  # Проверка, что день не воскресенье
        saved_amount += day_amount

print(f"Маша накопит нужную сумму через {days} дней")

# Task 3
stop_number = int(input('Введите количество чисел в последовательности: '))

list_of_numbers = [1, 1]
next_number = 0

while len(list_of_numbers) < stop_number:
    next_number = list_of_numbers[-1] + list_of_numbers[-2]
    list_of_numbers.append(next_number)

print(f"Последовательнсть Фибоначчи: {list_of_numbers}")

# Task 4
list_numbers = [0, 3, 8, 6, 7, 4]
sum_of_numbers = 0
min_number = list_numbers[0]
max_number = list_numbers[0]

for number in list_numbers:
    sum_of_numbers += number

    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number

print(f"Cумма чисел последовательности: {sum_of_numbers}")
print(f"Минимальное значение: {min_number}")
print(f"Максимальное значение: {max_number}")

# Task 5
list_numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1]
duplicates = []

for number in list_numbers:
    # проверка на "number not in duplicates" для того, чтобы несколько раз не выводились повторяющиеся числа
    if list_numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

if not duplicates:
    print("Все элементы в списке уникальны")
else:
    print("Найдены дублирующиеся элементы:")

for number in duplicates:
    count = list_numbers.count(number)
    print(f"{number}: повторений - {count}")

# Task 6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
left = 0
right = len(numbers) - 1
position = -1

while left <= right and position == -1:
    mid = (left + right) // 2

    if numbers[mid] == target:
        position = mid
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if position != -1:
    print(f"Позиция искомого элемента {target} в исходном списке: {position}")
else:
    print(f"Элемент {target} не найден в исходном списке")

# Task 7*
numbers = [7, 5, 6, 1, 2, 3, 4]
target = 7
left = 0
right = len(numbers) - 1
position = -1

while left <= right and position == -1:
    mid = (left + right) // 2

    if numbers[mid] == target:
        position = mid

    if numbers[left] <= numbers[mid]:
        if numbers[left] <= target <= numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if numbers[mid] <= target <= numbers[right]:
            left = mid + 1
        else:
            right = mid - 1

if position != -1:
    print(f"Позиция искомого элемента {target} в сдвинутом списке: {position}")
else:
    print(f"Элемент {target} не найден в сдвинутом списке")