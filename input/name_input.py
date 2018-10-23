name = str(input("What's your name? "))

if name.lower().endswith('a'):
    if name == 'kuba':
        print("Jesteś mężczyzną")
    else:
        print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")

age = input("How old are you? ")
print("Hello {} you are {} years old".format(name.capitalize(), age))
