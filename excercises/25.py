import string

for letter in string.ascii_uppercase:
    print(letter)

for number in range(1, 11):
    print(number)


def accleration(v1, v2, t1, t2):
    return (v2 - v1) / (t2 - t1)


print(accleration(0, 10, 0, 20))
