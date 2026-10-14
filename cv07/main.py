#NSD(48, 12) = 3 * 2 * 2

#48 = 2 * 2 * 3 * 2 * 2 * * 1
#12 = 3 * 2 * 2 * * 1

#NSD(50, 9) = 1

#50 = 5 * 9 + 5
#9 = 1 * 5 + 4
#5 = 1 * 4 + 1
#4 = 1 * 4 + 0

#NSD(485, 56)

#485 = 56 * 8 + 37
#56 = 37 * 1 + 19
#37 = 19 * 1 + 18
#19 = 18 * 1 + 1
#18 = 1 * 18 + 0

#NSD(84568, 15432)
#84568 = 15432 * 5 + 7408
#15432 = 7408 * 2 + 616
#7408 = 616 * 12 + 16
#616 = 16 * 38 + 8
#16 = 8 * 2 + 0

def NSD():
    A = int(input("Zadej cislo 1: "))
    B = int(input("Zadej cislo 2: "))

    while B != 0:
        podil = A // B
        zbytek = A % B
        
        print(f"{A} = {B} * {podil} + {zbytek}")

        A = B
        B = zbytek

    print(f"Nejmenší společný násobek je: {A}")

def NSD_NSN():
    while b != 0:
        a, b = b, a % b

def NSN():
    a = int(input("Zadej cislo a: "))
    b = int(input("Zadej cislo b: "))
    print(+(a * b) / NSD_NSN(a,b))
#nefunguje

if __name__ == "__main__":
    NSD()