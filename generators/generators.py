def create_cubes(n):
    for x in range(n):
        yield x ** 3


print(list(create_cubes(10)))


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(gen_fibon(10)))
for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))
print(next(g))

s = 'hello'

for letter in s:
    print(letter)

print(iter(s))
