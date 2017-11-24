"""decouple an abstraction from its implementation, so that both can bemodified independently without
the need to alter the other.
Name:Leonardo Israel Aguayo González"""
class DrawingAPIOne(object):
    """Implementation-specific abtraction: concrete class one"""

    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {}! )".format(x, y, radius))


class DrawingAPITwo(object):
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {}! )".format(x, y, radius))


class Circle(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


# Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw a circle
circle1.draw()

circle2=Circle(2,3,4,DrawingAPITwo())

circle2.draw()