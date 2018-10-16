d = dict(weather="clima", earth="terra", rain="chuva")


def vocabulary(word):
    try:
        return d[word]
    except KeyError:
        return "I don't know that word"


x = input("Please enter word to be translated: ")
print(vocabulary(x.lower()))