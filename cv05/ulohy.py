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

#3.5
#def evensum():
    #N = int(input("Zadej cislo: "))
    #for i in range(N):
        #if i % 2 != 0
#nedodelane

#3.2
def backwards():
    N = int(input("Zadej cislo: "))
    for i in range(N):
        print(f"{N-i}")
    
def nasobilka():
    N = int(input("Zadej cislo: "))
    for i in range(1, 11):
        print(f"{N*i}")

def minimum():
    N = int(input("Zadej cislo: "))
    min = N
    while N != -1:
        if min > N:
            min = N
        N = int(input("Zadej cislo: "))
    print(f"minimum je: {min} ")

def sum():
    N = int(input("Zadej cislo: "))
    print(f"{(N*(N+1)) / 2}")

def even_sum():
    soucet = 0
    N = int(input("Zadej cislo: "))
    for i in range(N + 1):
        if i % 2 == 0:
            soucet += i
    print(f"sum: {soucet}")

def factorial():
    result = 1
    index = 1
    N = int(input("Zadej cislo: "))

if __name__ == "__main__":
    even_sum()