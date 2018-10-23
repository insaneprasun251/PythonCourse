name = str(input("What's your name? "))
age = int(input("How old are you? "))

if age > 17 and age < 31:
    print("Enjoy your holiday, {0}!".format(name))
elif age < 18:
    print("You are too young to enjoy free holiday!")
else:
    print("You are too old for free holiday!")

