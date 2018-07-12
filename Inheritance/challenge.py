class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ( (x2-x1)**2 + (y2-y1)**2) **0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2-y1))/(x2-x1)


li = Line((3,2), (8,10))
print(li.distance())
print(li.slope())


class Cylinder(object):
    pi = 22/7

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * self.pi * self.radius**2

    def surface_area(self):
        top = self.pi * self.radius**2
        return 2 * top + 2 * self.pi * self.radius * self.height


c = Cylinder(2,3)
print(c.surface_area())
print(c.volume())
