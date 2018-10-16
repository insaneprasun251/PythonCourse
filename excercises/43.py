import string

with open('./two_by_two.txt', 'w') as two:
    mod = ''
    for i in string.ascii_lowercase:
        mod += i
        if len(mod) == 2:
            two.write(mod + '\n')
            mod = ''

# or
with open("letters.txt", 'w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + "\n")
