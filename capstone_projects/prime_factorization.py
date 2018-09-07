# TODO: Prime Factorization
def prime_factorization(num):
    square_root = num ** 0.5
    factors = []
    for i in range(1, int(square_root) + 1):

        if num % i == 0:
            factors.append(i)
            continue
        elif len(factors) == 2:
            print(str(num) + " is a prime number")
            break
        else:
            print(str(num) + " is not a prime number")
            break


prime_factorization(9)
