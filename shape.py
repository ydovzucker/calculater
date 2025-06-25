from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return "This is a Shape"

    def __add__(self, other):
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        return NotImplemented

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.get_area() < other.get_area()