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
    while index <= number:
        result = result * index
        index += 1
    return result

def factorial_recursion(number):
    if number <= 0:
        return 1
    return factorial_recursion(number - 1) * number

def fibbonachi(number):
    """
    Napiste funkci, ktera vypocita hodnotu x clen fibbonachiho posloupnosti
    """
    prev = 1
    actual = 1
    if number == 1 or 2:
        return 1
    
    for _ in range(number):
        tmp = prev + actual
        prev = actual
        actual = tmp
    return actual

def fibbonachi_recursion(number):
    if number == 0 or number == 1:
        return 1
    
    return fibbonachi_recursion(number - 1) + fibbonachi_recursion(number - 2)

def pascal_triangle(i):
    """
    Napiste funkci, ktera vypise X radek pascalova trouhelniku
    """
    for item in range(i + 1):
        print(int(combination_number(i, item)))

def combination_number(n, k):
    """
    Napiste funkci ktera vypocita kombinacni cislo
    """
    return (factorial_recursion(n) / (factorial_recursion(n-k) * factorial_recursion(k)))

if __name__ == "__main__":
    pascal_triangle(10)