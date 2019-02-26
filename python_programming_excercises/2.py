def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i

    return result


if __name__ == '__main__':
    print(factorial(8))
