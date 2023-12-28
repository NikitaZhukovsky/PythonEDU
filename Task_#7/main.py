import time
from math import factorial
from functools import reduce


some_list = [1, -1, 4, 6, -3, 8, 9]


def calculate_area(room):
    return room["length"] * room["width"]


def measure_exectime(func):
    def inner(*args, **kwargs):
        start = time.time()

        func(*args, **kwargs)

        end = time.time()

        print(f'Функции требуется {end - start} секунд для выполнения задачи')

    return inner


@measure_exectime
def factor(num):
    print(factorial(num))


print(f"Исходный список для заданий №1, 2: {some_list}")

# ------------------------------------------------------------------------------
# Task 1
print(f"Результат №1: {list(map(lambda elem: str(elem), some_list))}")

# ------------------------------------------------------------------------------
# Task 2
print(f"Результат №2: {list(filter(lambda x: x > 0, some_list))}")

# ------------------------------------------------------------------------------
# Task 3
strings = ["abc", "abcba", "hello", "aabbaa", "world"]

print(f"Исходный список строк: {strings}")
print(f"Результат №3: {list(filter(lambda x: x == x[::-1], strings))}")

# ------------------------------------------------------------------------------
# Task 4
factor(1000)

# ------------------------------------------------------------------------------
# Task 6
rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

areas = map(calculate_area, rooms)

total_area = reduce(lambda x, y: x + y, areas)

print("Общая площадь квартиры:", total_area)
