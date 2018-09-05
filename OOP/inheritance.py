class Animal():

    def __init__(self):
        print("Animal created")

    @staticmethod
    def who_am_i():
        print("I am an animal")

    @staticmethod
    def eat():
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    @staticmethod
    def bark():
        print("WOOF!")


my_dog = Dog()
print(my_dog)
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
