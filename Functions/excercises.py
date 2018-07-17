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
    name2 = ''
    for el in name:
        if el == 0 or el == 3:
            name2 += (name[el].upper())
        name2 += name[el]
    return name2


print(old_macdonald("macdonald"))
