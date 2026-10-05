from random import random

total_couter = 0
counter_in = 0

for _ in range(1000):
    x = random() - 0.5 # 0-1
    y = random() - 0.5 # 0-1

    size = (x ** 2 + y ** 2) ** (0.5)

    if size <= 0.5:
        counter_in = counter_in + 1

    total_couter = total_couter + 1

print(counter_in / total_couter * 4)