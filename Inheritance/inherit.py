class Animal(object):
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        # Any method that is the same as in the Parent class is overwritten by this.
        print('Dog')

    def bark(self):
        print("woof!")


a = Animal()
print(a)

d = Dog()
d.eat()
d.bark()