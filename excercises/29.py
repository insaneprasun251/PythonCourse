def volume(h, r=10, pi=3.14159265359):
    return ((4 * pi * r ** 3) / 3) - ((pi * h ** 2 * (3 * r - h)) / 3)


print(volume(2))
