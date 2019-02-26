from math import sqrt


def square_rooting(d):
    d = d.split(',')
    c = 50
    h = 30
    d_list = []
    for element in d:
        d_list.append(round(sqrt(2 * c * int(element) / h)))

    return d_list


if __name__ == '__main__':
    print(square_rooting('100,150,180'))
