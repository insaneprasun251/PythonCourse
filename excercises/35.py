def string_splitter(default_string):
    a = []
    for i in default_string.split():
        a.append(i)
    return len(a)


print(string_splitter("My name is Matthew"))
