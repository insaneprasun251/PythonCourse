from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Husky', name='Sam')

print(sam.age)

Cat = namedtuple('Cat', 'fur claws name')

c = Cat(fur='Fuzzy', claws=False, name='Kitty')

print(c.fur)