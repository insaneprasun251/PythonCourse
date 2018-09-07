try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print("TypeError occurred: only numbers can be multiplied")

try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("ZeroDivisionError: you can't divide by 0")

while True:
    integer = input("Please input integer: ")
    try:
        result = int(integer) ** 2
    except TypeError and ValueError:
        print("This is not integer")
        continue
    else:
        print(result)
        break
