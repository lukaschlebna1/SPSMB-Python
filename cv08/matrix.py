def zeros(m, n):
    """
    Function creates empty matrix
    """
    matrix_c = []
    for i in range(m):
        matrix_c.append([])
        for j in range(n):
            matrix_c[i].append(0)
    return matrix_c

def plus(matrix_a, matrix_b):
    matrix_c = zeros(len(matrix_a), len(matrix_a[0]))
    for i in range(len(matrix_c)):
        for j in range(len(matrix_c[i])):
            matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return matrix_c

def minus(matrix_a, matrix_b):
    matrix_c = zeros(len(matrix_a), len(matrix_a[0]))
    for i in range(len(matrix_c)):
        for j in range(len(matrix_c[i])):
            matrix_c[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return matrix_c

def eyes(m, n):
    """
    Vygeneruje jednotkovou matici
    """
    matrix = zeros(m, n)
    for i in range(m):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
    return matrix

def size_of(matrix):
    "Vraci velikost matice"
    return (len(matrix), len(matrix[0]))

def format(matrix):
    size_m, size_n = size_of(matrix)
    print(f"Size ({size_m}, {size_n})")
    for i in range(size_m):
        for j in range(size_n):
            print(f"{matrix[i][j]}\t", end="")
        print()

def multiplty_const(matrix, const):
    m, n = size_of(matrix)
    result = zeros(n, m)
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j] * const
    return result

def multiply(matrix_a, matrix_b):
    mA, nA = size_of(matrix_a)
    mB, nB = size_of(matrix_b)
    if nA != mB:
        raise ValueError(f"Matrix A and B can not be multiply.")
    result = zeros(mA, nB)
    for i in range(mA):
        for j in range(nB):
            sum = 0
            for l in range(nA):
                sum += matrix_a[i][j] * matrix_b[l][j]
            return result
        
def apply(matrix, func):
    m, n = size_of(matrix)
    result = zeros(n, m)
    for i in range(m):
        for j in range(n):
            result[j][i] = func(matrix[i][j])
    return result

def T(matrix):
    m, n = size_of(matrix)
    result = zeros(n, m)
    for i in range(m):
        for j in range(n):
            result[j][i] = matrix[i][j]
    return result