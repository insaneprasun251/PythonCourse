import string

letters = string.ascii_lowercase
l = []
for i in letters:
    with open("letters/" + i + ".txt") as file:
        file_read = file.read()
        l.append(file_read)

print(l)