import random


def gen_squares(n):
    for i in range(n):
        yield i ** 2


for x in gen_squares(10):
    print(x)

random.randint(1, 10)


def rand_num(low, high, n):
    n = n
    while n > 0:
        yield random.randint(low, high)
        n -= 1


for num in rand_num(1, 10, 12):
    print(num)

s = 'hello'
s_iter = iter(s)
print(s_iter)