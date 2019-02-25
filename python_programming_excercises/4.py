def tuple_changer():
    numbers = input("Please input sequence: ")
    return list(numbers.split(",")), tuple(numbers.split(","))



if __name__ == '__main__':
    print(tuple_changer())