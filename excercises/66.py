d = dict(weather = "clima", earth="terra", rain="chuva")

x = input("Please enter word to be translated: ")

if x in d:
    print(d[x])
else:
    print("I don't know that word")