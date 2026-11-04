from matrix import plus, zeros, minus, eyes, format, T, multiply, replace_row, replace_collum, determinant, convolution
from view import load, numpy_to_list, list_to_numpy, show

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

    kernel = [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]

#matrix_c = plus(matrix_a, matrix_b)

# 2, 1, 2
# 1, 2, 1
# 1, 1, 2

#format(T(matrix_c))
print(determinant(matrix_x))

image = load("C:\\Users\\lukas.chlebna\\Desktop\\python\\SPSMB-Python\\cv08\\image.png")

img = numpy_to_list(image)
new_img = convolution(img, kernel)
np_img = list_to_numpy(new_img)
show(np_img)