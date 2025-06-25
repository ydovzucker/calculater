from shape import Shape
from math import sqrt

class RightTriangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height
        self.hypotenuse = sqrt(base ** 2 + height ** 2)

    def get_area(self):
        return 0.5 * self.base * self.height

    def get_perimeter(self):
        return self.base + self.height + self.hypotenuse

    def __repr__(self):
        return f"{self.__class__.__name__}({self.base}, {self.height})"