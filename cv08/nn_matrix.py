import math
from matrix import T, multiply, apply, plus

def signoid(x):
    return 1 / (1 + math.exp(-x))

def neuron_network(
    X
):
    X = T(X)
    W = [
        [0.4, 0.1, 0.3, 0.4, 0.1, 0.5, -0.2], # DOG
        [-0.2, -0.2, 0.1, 0.1, 0.1, 0.1, 0.6], # FISH
        [0.4, 0.3, 0.5, 0.5, 0.5, 0.3, 0.0], # CAT
    ]

    b = T([[0.1, 0.6, 0.1]]) # bias

    result = multiply(W, X)

    result = plus(result, b)

    return apply(result, signoid)

def do_softmax(items):
    total_signoid = sum(items)
    result = []
    for i in items:
        result.append(i/total_signoid)
    return result
    
if __name__ == "__main__":
    X = [
        [0.75, 1, 1, 1, 1, 1, 0] #priznaky/vstup
    ]

    Y = neuron_network(
        X
    )
    Y = T(Y)
    print(do_softmax(Y))