"""
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def integral(n):
    dict_of_integrals = {}
    for i in range(1, n + 1):
        dict_of_integrals[i] = i * i

    return dict_of_integrals


if __name__ == '__main__':
    print(integral(8))
