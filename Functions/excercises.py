def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            return a
        return b
    else:
        if a > b:
            return a
        return b


def animal_crackers(text):
    string1, string2 = text.split(" ")
    if string1[0].lower() == string2[0].lower():
        return True
    return False


def make_twenty(a, b):
    if int(a) == 20 or int(b) == 20 or (a + b) == 20:
        return True
    return False


def old_macdonald(name):
    name2 = str(name[0].upper()) + str(name[1:3]) + str(name[3].upper()) + str(name[4:])
    return name2


def master_yoda(text):
    a, b, c = text.split(" ")
    text2 = " ".join([c, b, a])
    return text2


def almost_there(n):
    if n in range(90, 111) or n in range(190, 211):
        return True
    return False


def has_33(my_list):
    if my_list[0] == my_list[1] == 3 or my_list[1] == my_list[2] == 3:
        return True
    return False


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c]:
        return sum([a, b, c]) - 10
    else:
        return "BUST"


def summer_69(arr):
    # TODO: Correct This

    result = 0
    add = True
    for i in arr:
        while add:
            if i != 6:
                result += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break

    return result


def spy_game(my_list):
    code = [0, 0, 7, 'x']

    for num in my_list:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


def count_primes(num):
    # Store our prime numbers
    primes = [2]
    # Counting going up to the input number
    x = 3
    # Checks for 0 or 1 input
    if num < 2:
        return 0
    # x is going through every number up to input number
    while x <= num:
        # Check if x is prime
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)


print(count_primes(100))
