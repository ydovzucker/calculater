rom shape import Shape
from math import sqrt

class GeneralTriangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive numbers.")
        if (
            side1 + side2 <= side3 or
            side1 + side3 <= side2 or
            side2 + side3 <= side1
        ):
            raise ValueError("Triangle inequality violated: The sum of any two sides must be greater than the third.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        # Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(
            s *
            (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __repr__(self):
        return f"{self.__class__.__name__}({self.side1}, {self.side2}, {self.side3})"