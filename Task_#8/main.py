# Funcs for task №1
def calculate_bmi(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        if height <= 0 or weight <= 0:
            raise ValueError("Рост и вес должны быть положительными значениями.")
        elif height > 3:
            raise ValueError("Перепроверьте рост, он указывается в метрах")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    if bmi is None:
        return None

    if bmi < 18.5:
        return "Недостаточный вес"
    elif bmi < 25:
        return "Нормальный вес"
    elif bmi < 30:
        return "Избыточный вес"
    else:
        return "Ожирение"


# Func for task №2
def calculate(first_number, second_number, operator):
    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        print("Ошибка: Введите числа корректно.")
        return None

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль недопустимо.")
            return None
    else:
        print("Ошибка: Неизвестный оператор.")
        return None

    return result


# -------------------------------------------------------------------------------------
# Task 1
choice = 1
while choice == 1:
    our_height = input("Введите ваш рост (в метрах): ")
    our_weight = input("Введите ваш вес (в килограммах): ")

    our_bmi = calculate_bmi(our_height, our_weight)
    interpretation = interpret_bmi(our_bmi)

    if interpretation is not None:
        print(f"Ваш ИМТ: {our_bmi:.2f}")
        print(f"Пояснение: {interpretation}")
    choice = int(input("Хотите продолжить? (1. Да / 2. Нет): "))

# -------------------------------------------------------------------------------------
# Task 2
choice = 1
while choice == 1:
    input_first_number = input("Введите первое число: ")
    input_second_number = input("Введите второе число: ")
    input_operator = input("Введите оператор (+, -, *, /): ")

    expression_result = calculate(input_first_number, input_second_number, input_operator)
    if expression_result is not None:
        print(f"Результат: {expression_result}")

    choice = int(input("Хотите продолжить? (1. Да / 2. Нет): "))
