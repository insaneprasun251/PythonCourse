import string

with open("letters.txt", 'w') as file:
    letters = string.ascii_lowercase + " "
    slice1 = letters[0::3]
    slice2 = letters[1::3]
    slice3 = letters[2::3]
    for letter1, letter2, letter3 in zip(slice1, slice2, slice3):
        file.write(letter1 + letter2 + letter3 + "\n")
