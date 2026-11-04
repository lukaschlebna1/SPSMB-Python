from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load(path):
    img = Image.open(path).convert("L")
    matrix = np.array(img)
    return matrix

def show(matrix):
    plt.imshow(matrix, cmap="gray")
    plt.colorbar()
    plt.show()

#hlavni program
matrix = load("C:\\Users\\lukas.chlebna\\Desktop\\python\\SPSMB-Python\\cv08\\image.png")
print(matrix)
show(matrix)