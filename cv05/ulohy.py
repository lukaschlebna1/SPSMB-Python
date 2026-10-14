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
def suma():
    N = int(input("Zadej cislo: "))
    print(f"{(N*(N+1)) / 2}")

#3.4
def even_sumo():
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

#11.1
def retezec():
    text = (input("Zadej text: "))
    print(len(text))

#11.3
def palindrom():
    txt = input("Zadej text: ")
    pal = txt[::-1]
    if pal == txt:
        print(f"Zadane slovo je palindrom")
    else:
        print(f"Neni palidrom")

#11.4
def samo():
    txt = input("Zadej text: ")
    lst = ["a", "e", "i", "o", "u"]
    for c in lst:
        counter = 0
        for h in txt:
            if c.capitalize() == h.capitalize():
                counter += 1
        print(f"V textu se nachazi {c} -> {counter}")

#11.5
def znaky():
    txt = input("Zadej text: ")
    dct = {}
    for i in txt:
        if i in dct.keys():
            counter = dct[i] + i
            dct[i] = counter
        else:
            dct[i] = i
    print(dct)

#12.1
def list_sum():
    N = input("Zadejte cisla: ")
    numbers = [int(x) for x in N.split()]
    print(sum(numbers))

#12.3
def seznam():
    N = input("Zadejte cisla: ")
    number = []
    for i in N.split():
        number.append(int(i))
    #number.reverse()
    print(number[::-1])

#12.4
def dupe():
    N = input("Zadejte cisla: ")
    cislo = []
    for i in N.split():
        a = int(i)
        if a not in cislo:
            cislo.append(a)
            #if a no in cislo:
            # cislo.append(a)
    st = set(cislo)
    lst = list(st)
    print(lst)

#12.2
def min_max():
    N = input("Zadej cisla: ")
    numbers = []
    min = float("inf")
    max = float("-inf")
    for i in N.split():
        a = int(i)
        if a > max:
            max = i
        if a < min:
            min = i 
    print(f"max {max} min {min}")

if __name__ == "__main__":
    dupe()