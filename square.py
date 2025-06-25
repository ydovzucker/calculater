from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.width})"