def my_func(my_string):
    new_string = ''
    for i, x in enumerate(my_string):
        if i % 2 == 0:
            new_string += x.upper()
        else:
            new_string += x.lower()

    return new_string


for i, value in enumerate("Hello"): print(i, value)
