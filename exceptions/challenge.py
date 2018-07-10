from pip._vendor.distlib.compat import raw_input

for i in ['a', 'b', 'c']:
    try:
        print(i **2)
    except TypeError:
        print("Seems like {} is not a number".format(i))

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("One of the values is 0, you can't divide by zero")
finally:
    print("Finally, all good")


def ask():

    while True:
        try:
            value = int(raw_input('Please enter the integer to get a square of it'))
        except ValueError:
            print("Seems like you did not input the integer")
            continue
        else:
            print("Thank you, your number square is: " + str(value * value))
            break


ask()
