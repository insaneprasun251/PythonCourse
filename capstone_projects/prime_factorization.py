# TODO: Prime Factorization
from collections_module import Counter


def prime_factorization(num):
    square_root = num ** 0.5
    factors = []
    if num ** 0.5 == int:
        factors.append(square_root)

    for i in range(1, int(square_root) + 1):

        if num % i == 0:
            factors.append(i)
            continue

    if len(factors) != 2:
        print(str(num) + " is not a prime number")
    print(factors)
    print("Factors: {}".format(sorted(factors)))
    print(Counter(factors))
    print("Multiplication of those numbers results in the provided number: " + str(sorted(factors)))


prime_factorization(12)
