import math
#kvuli pi

#2.5 
def year(number):
    return number % 400 == 0 or ((number % 4 == 0) and (number % 100 != 0))

#1.5 
def mean():
    x1 = int(input("1:"))
    x2 = int(input("2:"))
    x3 = int(input("3:"))
    print(f"Vysledek je: {(x1 + x2 + x3) / 3}")

#3.1 
def nums():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{i + 1}")

#3.2
def backwards():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{N-i}")

#3.6 
def nasobilka():
    N = int(input("Zadej cislo: "))
    for i in range(1, 11):
        print(f"{N*i}")

#7.1
def minimum():
    N = int(input("Zadej cislo: "))
    min = N
    while N != -1:
        if min > N:
            min = N
        N = int(input("Zadej cislo: "))
    print(f"minimum je: {min} ")

#3.3
def sum():
    N = int(input("Zadej cislo: "))
    print(f"{(N*(N+1)) / 2}")

#3.4
def even_sum():
    soucet = 0
    N = int(input("Zadej cislo: "))
    for i in range(1, N + 1):
        if i % 2 == 0:
            soucet += i
    print(f"sum: {soucet}")

#4.1
def factorial():
    result = 1
    N = int(input("Zadej cislo: "))
    for i in range(1, N + 1):
        result = result * i
    print(f"Vysledek faktorialu je: {result}")

#4.1
def factorial2(N):
    result = 1
    for i in range(1, N + 1):
        result = result * i
    return result

#5.1
def combination_num():
    N = int(input("Zadej cislo: "))
    K = int(input("Zadej cislo: "))
    print(factorial2(N) / ( factorial2(K) * factorial2(N - K)))

#4.2
def factorial3(N):
    if N <= 1:
        return 1
    
    return N * factorial3(N - 1)

#2.1
def even_or_odd():
    N = int(input("Zadej cislo: "))
    if N % 2 == 0:
        print("cislo je sude")
    else:
        print("cislo je liche")

#15.1
def obdelnik():
    A = int(input("Zadej cislo: "))
    B = int(input("Zadej cislo: "))
    O = 2*(A + B)
    S = A * B
    print(f"Obvod: {O}")
    print(f"Obsah: {S}")

#15.2
def kruh():
    r = int(input("Zadej cislo: "))
    o = 2 * math.pi * r
    S = math.pi * (r*r)
    print(f"Obvod: {o}")
    print(f"Obsah: {S}")

#2.4
def nejvetsi_z_3():
    A = int(input("Zadej cislo: "))
    B = int(input("Zadej cislo: "))
    C = int(input("Zadej cislo: "))
    highest = max(A,B,C)
    print(f"Nejvetsi cislo ze 3 je: {highest}")

#15.3
def pythagorova():
    a = int(input("Zadej cislo: "))
    b = int(input("Zadej cislo: "))

    c = ((a ** 2) * (b ** 2)) ** 0.5
    print(f"pythagorova veta: {c}")

#1.1 + 1.2 + 1.3 + 1.4
def ulohy():
    a = int(input("Zadej cislo: "))
    b = int(input("Zadej cislo: "))
    c = (a + b)
    d = (a - b)
    e = (a * b)
    f = (a / b)
    print(f"vysledek: {c}, {d}, {e}, {f}")

if __name__ == "__main__":
    ulohy()