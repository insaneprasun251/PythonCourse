class Line:
    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        return (
                       (self.coordinate2[0] - self.coordinate1[0]) ** 2 +
                       (self.coordinate2[1] - self.coordinate1[1]) ** 2) ** 0.5

    def slope(self):
        return (self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0])


line1 = Line((3, 2), (8, 10))
print(line1.distance())
print(line1.slope())


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius ** 2 + 2 * self.pi * self.radius * self.height


cyli = Cylinder(2, 3)
print(cyli.volume())
print(cyli.surface_area())

