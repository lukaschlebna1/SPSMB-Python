def prime_number(number):
    """
    Napiste funkci, ktera zjisti jestli je na vstupu prirozeny cislo
    """
    i = number - 1
    while i > 1:
        if number % i == 0:
            return False
        i = i - 1
    return True

def factorial(number):
    """
    Napiste funkci, ktera vypocita hodnotu faktorialu
    """
    result = 1
    index = 1
    while index < number:
        result = result * index
        index += 1
    return result

def factorial_recursion(number):
    if number <= 0:
        return 1
    return factorial_recursion(number - 1) * number

def fibbonachi():
    """
    Napiste funkci, ktera vypocita hodnotu x clen fibbonachiho posloupnosti
    """
    pass

def fibbonachi_recursion(number):
    if number == 0 or number == 1:
        return 1
    
    return fibbonachi_recursion(number -1) + fibbonachi_recursion(number -2)

def pascal_triangle():
    """
    Napiste funkci, ktera vypise X radek pascalova trouhelniku
    """
    pass

    if __name__ == "__main__":
        lst = []
        number = None
        while number is None or number != -1:
            number = int(input("Zadej hodnotu: "))
            if number == -1:
                break
            lst.append(number)

        print(f"Max value {max(lst)}")
        print(f"Min value {min(lst)}")
        print(f"Mean value {sum(lst) / len(lst)}")
