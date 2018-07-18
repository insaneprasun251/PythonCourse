my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list.pop(3)
print(my_list)
my_list.insert(6, 8)
print(my_list)


def name_function(name="Jose"):
    """
    Returns Hello with a provided name
    :param name: name
    :return: Hello + name
    """
    return "Hello " + str(name)


print(help(name_function))
result = name_function("Zach")
print(result)


def dog_check(s):
    return "dog" in s.lower()


result = dog_check("My dog ran away")
print(result)


def pig_latin(s):
    if s[0] in 'aeiou':
        pig_word = s + 'ay'
    else:
        pig_word = s[1:] + s[0] + 'ay'
    return pig_word


print(pig_latin("apple"))
