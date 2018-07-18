def my_func(*args):
    """

    :param a: first value
    :param b: second value
    :return: returns 5% of the sum of all arguments
    """
    return sum(args) * 0.05


print(my_func(1, 5, 4, 5, 6, 3, 5, 7, 4, 1000, 5000))


def my_func2(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit of choice is: {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")


print(my_func2(fruit="orange", veggie="celery"))


def my_func3(*args, **kwargs):
    print("I would like to buy: {} {}". format(args[0], kwargs['food']))


print(my_func3(10, 20, 30, food="hamburgers", veggie="pepper", animal="dog"))