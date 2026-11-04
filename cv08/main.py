from matrix import plus, zeros, minus, eyes, format, T, multiply, replace_row, replace_collum, determinant

if __name__ == "__main__":
    matrix_a = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 1]
    ]

    matrix_b = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]

    matrix_x = [
        [2, 1],
        [1, 2]
    ]

#matrix_c = plus(matrix_a, matrix_b)

# 2, 1, 2
# 1, 2, 1
# 1, 1, 2

#format(T(matrix_c))
print(determinant(matrix_x))