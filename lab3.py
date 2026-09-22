# Частина А 

def is_valid_variable(s: str) -> bool: # функція перевіряє чи відповідає рядок заданим вимогам

    if len(s) == 0:
        return False

    first_char = s[0] # перевіряємо перший символ
    is_valid_first_char = ('a' <= first_char <= 'z') or ('A' <= first_char <= 'Z') or (first_char == '_')

    if not is_valid_first_char:
        return False

    for i in range (1, len(s)): # перевіряємо другий і наступні символи
        char = s[i]
        is_valid_char = ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or (char == '_')

        if not is_valid_char:
            return False

    return True    

data_for_test_a = [ # тестові дані для перевірки функції is_valid_variable
    ("valid_variable", True),
    ("_valid_variable", True),
    ("validVariable123", True),
    ("1invalid_variable", False),
    ("invalid-variable", False),
    ("invalid variable", False),
    ("", False),
    ("i", True)

]

print("test results for part A") # вивід результатів тестування функції is_valid_variable
for test_case, expected in data_for_test_a:
    actual = is_valid_variable(test_case)
    status = "PASSED" if actual == expected else "FAILED"
    print(f"Test case: '{test_case}', Expected: {expected}, Actual: {actual}, Status: {status}")





# Частина Б

def reverse_matrix_rows(matrix: list) -> list: # функція обертає порядок елементів у кожному рядку матриці
    for row in matrix:
        left = 0
        right = len(row) - 1

        while left < right: # реалізовано алгоритм Two Pointers
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1

    return matrix

data_for_test_b = [ # тестові дані для перевірки функції reverse_matrix_rows
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ],
    [
        [197]
    ],
    [
        [1, 2, 3, 44],
        [],
        [7, 8, 10]
    ]
]

print("\ntest results for part B") # вивід результатів тестування функції reverse_matrix_rows
for idx, mat in enumerate(data_for_test_b, start=1):
    original_matrix = [row[:] for row in mat] # створює копію матриці для збереження початкового стану у виводі
    reversed_matrix = reverse_matrix_rows(mat)

    print(f"Test {idx}:")
    print(f"Original matrix: {original_matrix}")
    print(f"Reversed matrix: {reversed_matrix}")