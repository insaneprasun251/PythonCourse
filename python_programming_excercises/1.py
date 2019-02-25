def divisble(min_number, max_number):
    list_of_ints = []
    for i in range(min_number, max_number + 1):
        if i % 7 == 0 and i % 5 != 0:
            list_of_ints.append(i)
    return list_of_ints


if __name__ == '__main__':
    print(divisble(2000, 3200))
