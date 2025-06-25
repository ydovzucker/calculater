from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return 0.5 * self.width * self.height

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width}, {self.height})"