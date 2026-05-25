# Exercise 1: Geometry
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = float(radius)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def geo(self):
        print("In geometry, a circle is the set of points in a plane at an equal distance from a fixed point called the center.")

result = Circle()
print(result.perimeter())
print(result.area())
result.geo()
