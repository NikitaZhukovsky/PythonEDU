# Func for task 1
import random


def binary_search_recursive(someone_list, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if someone_list[mid] == target:
        return mid

    if someone_list[mid] > target:
        return binary_search_recursive(someone_list, target, left, mid - 1)
    else:
        return binary_search_recursive(someone_list, target, mid + 1, right)


# Func for task 2
def decimal_to_binary_iterative(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number


# Func for task 3
def is_prime_number(number):
    counter = 0
    if number == 1 or number == 0:
        return 'не является ни простым, ни составным'
    for divisible in range(1, number + 1):
        if number % divisible == 0:
            counter += 1
    return 'простое' if counter == 2 else 'составное'


# Func for task 4
def largest_common_divisor(first_number, second_number):
    # алгоритм Евклида
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return second_number


# Funcs for task 5
def caesar_cipher_encrypt(word, key):
    encrypted_word = ""
    for letter in word:
        if letter.isdigit():
            encrypted_letter = letter
        elif 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            if letter.isupper():
                encrypted_letter = chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted_letter = chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        elif 'А' <= letter <= 'я' or 'Ё' <= letter <= 'ё':
            if letter.isupper():
                encrypted_letter = chr((ord(letter) - ord('А') + key) % 33 + ord('А'))
            else:
                encrypted_letter = chr((ord(letter) - ord('а') + key) % 33 + ord('а'))
        else:
            encrypted_letter = letter
        encrypted_word += encrypted_letter
    return encrypted_word


def caesar_cipher_decrypt(word, key):
    encrypted_word = ""
    for letter in word:
        if letter.isdigit():
            encrypted_letter = letter
        elif 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
            if letter.isupper():
                encrypted_letter = chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
            else:
                encrypted_letter = chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
        elif 'А' <= letter <= 'я' or 'Ё' <= letter <= 'ё':
            if letter.isupper():
                encrypted_letter = chr((ord(letter) - ord('А') - key) % 33 + ord('А'))
            else:
                encrypted_letter = chr((ord(letter) - ord('а') - key) % 33 + ord('а'))
        else:
            encrypted_letter = letter
        encrypted_word += encrypted_letter
    return encrypted_word


# Funcs for task 7
def random_matrix(lines, columns):
    matrix = []
    for i in range(lines):
        row = []
        for j in range(columns):
            row.append(random.randint(0, 10))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Func for task 8
def find_min_max_matrix(matrix):
    min_val = float('inf')
    max_val = float('-inf')
    min_index = None
    max_index = None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_index = (i, j)
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_index = (i, j)

    return min_index, max_index


# Func for task 9
def calculate_column_percentages(matrix):
    total_sum = 0
    column_sums = []

    # Вычисление суммы элементов матрицы и сумм каждого столбца
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        total_sum += row_sum
        for j in range(len(matrix[i])):
            if i == 0:
                column_sums.append(matrix[i][j])
            else:
                column_sums[j] += matrix[i][j]

    # Вычисление доли каждого столбца в общей сумме
    column_percentages = [(col_sum / total_sum) * 100 for col_sum in column_sums]

    return column_percentages


# Func for task 12
def check_columns(matrix, h):
    columns_with_h = []
    columns_without_h = []
    for j in range(len(matrix[0])):
        has_h = False
        for i in range(len(matrix)):
            if matrix[i][j] == h:
                has_h = True
                break
        if has_h:
            columns_with_h.append(j)
        else:
            columns_without_h.append(j)
    return columns_with_h, columns_without_h


# Func for task 13
def calculate_diagonal_sums(matrix):
    main_sum = 0
    secondary_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:  # элементы на главной диагонали имеют одинаковые индексы
                main_sum += matrix[i][j]
            if i + j == len(matrix) - 1:  # элементы на побочной диагонали имеют сумму индексов равную len(matrix) - 1
                secondary_sum += matrix[i][j]

    return main_sum, secondary_sum


# Func for task 14
def add_even_column(matrix):
    modified_matrix = []
    for row in matrix:
        count_ones = row.count(1)
        if count_ones % 2 == 0:
            row.append(0)
        else:
            row.append(1)
        modified_matrix.append(row)
    return modified_matrix


# MAIN
# ----------------------------------------------------------------------------------------------
# Task 1
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Отсортированный список: {sorted_list}")
target_number = int(input("Введите значение, которое хотите найтив отсортированном списке: "))

result = binary_search_recursive(sorted_list, target_number, 0, len(sorted_list) - 1)

if result != -1:
    print(f"Искомый элемент найден на позиции {result} ")
else:
    print("Искомый элемент не найден")

# ----------------------------------------------------------------------------------------------
# Task 2
decimal_number = int(input("Введите число в десятичной системе: "))
result = decimal_to_binary_iterative(decimal_number)
print(f"Число в двоичной системе: {result}")

# ----------------------------------------------------------------------------------------------
# Task 3
input_number = int(input("Введите число, чтобы проверить является оно простым или составным: "))
print(f"Число {input_number}: {is_prime_number(input_number)}")

# ----------------------------------------------------------------------------------------------
# Task 4
input_first_number = int(input('Введите первое число для НОД: '))
input_second_number = int(input('Введите второе число для НОД: '))

print(f"НОД чисел: {largest_common_divisor(input_first_number, input_second_number)}")

# ----------------------------------------------------------------------------------------------
# Task 5
message = input("Введите сообщение для шифрования: ")
print("Не ставьте пробел в конце строки!!!")
action = input("Выберите действие (шифровать или дешифровать): ")

if action.lower() == "шифровать":
    shift = int(input("Введите сдвиг: "))
    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Зашифрованное сообщение: {encrypted_message}")
elif action.lower() == "дешифровать":
    shift = int(input("Введите сдвиг: "))
    decrypted_message = caesar_cipher_decrypt(message, shift)
    print(f"Расшифрованное сообщение: {decrypted_message}")
else:
    print("Неверное указание действия. Пожалуйста, выберите 'шифровать' или 'дешифровать'.")

# ----------------------------------------------------------------------------------------------
# Task 7
number_of_lines = int(input('Введите количество строк матрицы: '))
number_of_columns = int(input('Введите количество столбцов матрицы: '))

main_matrix = random_matrix(number_of_lines, number_of_columns)
print('Матрица для задания №7')
print_matrix(main_matrix)

# ----------------------------------------------------------------------------------------------
# Task 8
print('Матрица для задания №8')
print_matrix(main_matrix)
print(f"Индексы минимального и максимального элементов матрицы: {find_min_max_matrix(main_matrix)}")

# ----------------------------------------------------------------------------------------------
# Task 9
percentages = calculate_column_percentages(main_matrix)
print('Матрица для задания №9')
print_matrix(main_matrix)
print("Доли каждого столбца в общей сумме:")
for index_column, percentage in enumerate(percentages):
    print(f"Столбец {index_column + 1}: {percentage:.2f}%")

# ----------------------------------------------------------------------------------------------
# Task 12
check_number = int(input("Введите число, которое нужно найти в столбцах: "))
check_columns_with_h, check_columns_without_h = check_columns(main_matrix, check_number)
print('Матрица для задания №13')
print_matrix(main_matrix)
print(f"Искомый элемент находится в столбце: {check_columns_with_h}, этого числа нет в: {check_columns_without_h}")
# ----------------------------------------------------------------------------------------------
# Task 13
main_diagonal_sum, secondary_diagonal_sum = calculate_diagonal_sums(main_matrix)
print('Матрица для задания №13')
print_matrix(main_matrix)

print(f"Сумма элементов на главной диагонали: {main_diagonal_sum}")
print(f"Сумма элементов на побочной диагонали: {secondary_diagonal_sum}")

# ----------------------------------------------------------------------------------------------
# Task 14
one_zero_matrix = \
    [[1, 1, 0],
     [1, 0, 1],
     [0, 0, 1]]

print('Исходная матрица для задания №14')
print_matrix(one_zero_matrix)
print('Полученная матрица')
print_matrix(add_even_column(one_zero_matrix))
