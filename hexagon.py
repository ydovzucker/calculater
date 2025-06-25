from shape import Shape
from math import sqrt

class RegularHexagon(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side_length = side_length

    def get_area(self):
        return (3 * sqrt(3) / 2) * self.side_length ** 2

    def get_perimeter(self):
        return 6 * self.side_length

    def __repr__(self):
        return f"{self.__class__.__name__}({self.side_length})"