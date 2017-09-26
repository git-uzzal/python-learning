from math import sqrt


class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        print('Line created!')

    def distance(self):
        return sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

class Cylinder(object):
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        print('Cylinder is created!')

    def volume(self):
        return (self.radius ** 2) * self.height * Cylinder.pi

    def surface_area(self):
        return (2 * self.height * self.radius * Cylinder.pi) + 2 * (self.radius ** 2) * Cylinder.pi

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

c = Cylinder(1,1)
print(c.volume())
print(c.surface_area())