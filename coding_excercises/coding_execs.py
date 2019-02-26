def give_max(num1, num2):
    return max(num1, num2)


def fizz_buzz(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return "FizzBuzz"
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def check_speed(speed):
    if speed < 70:
        print("OK")
    else:
        speed_over_limit = speed - 70
        points = speed_over_limit / 5
        print("Points: {}".format(int(points)))
        if points > 12:
            print("License suspended")


def show_numbers(limit):
    for el in range(limit):
        if el % 2 == 0:
            print(str(el) + " EVEN")
        else:
            print(str(el) + " ODD")


def show_multiplies(limit):
    result = 0
    for el in range(limit + 1):
        if el % 3 == 0 or el % 5 == 0:
            result += el
    print(result)


if __name__ == '__main__':
    print(give_max(35, 17))
    print(fizz_buzz(8))
    check_speed(135)
    show_numbers(15)
    show_multiplies(20)
