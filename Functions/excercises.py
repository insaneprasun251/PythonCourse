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


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
