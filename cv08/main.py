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

    kernel_1 = [
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1]
    ]

    kernel_2 = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]

    bluer_kernel = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]

    sharpening_kernel = [
        [0, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ]

    emboss_kernel = [
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2]
    ]

    laplacian_kernel = [
        [0, 0, -1, 0, 0],
        [0, -1, -2, -1, 0],
        [-1, -2, -12, -2, -1],
        [0, -1, -2, -1, 0],
        [0, 0, -1, 0, 0]
    ]

    gaussian_kernel = [
        [1, 4, 6, 4, 1],
        [4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
        [1, 4, 6, 4, 1]
    ]
#matrix_c = plus(matrix_a, matrix_b)

# 2, 1, 2
# 1, 2, 1
# 1, 1, 2

#format(T(matrix_c))
print(determinant(matrix_x))

image = load("C:\\Users\\lukas.chlebna\\Desktop\\python\\SPSMB-Python\\cv08\\image.png")

img = numpy_to_list(image)
#new_img = convolution(img, kernel_1)
#new_img_2 = convolution(img, kernel_2)
#result = convolution(img, emboss_kernel)
#np_img = list_to_numpy(plus(new_img, new_img_2))
result = convolution(img, laplacian_kernel)
np_img = list_to_numpy(result)
show(np_img)