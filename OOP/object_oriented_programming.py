my_list = [1, 2, 3]

my_set = set()


class Dog:
    # Class Object attribute
    # Same for any instance of the class
    species = "mammal"

    def __init__(self, name, spots, breed="Lab"):
        """
        Attributes
        We take in argument
        Assign it using self.attribute name
        :param breed: Breed of a Dog
        """
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

    @staticmethod
    def bark(self, number):
        print("Woof! My name is: {} and the number is  {}".format(self.name, number))


my_dog = Dog(name="Pedro", spots=False, breed="Husky")
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.species)
my_dog.bark(my_dog, 76)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)

print(my_circle.get_circumference())
print(my_circle.area)
