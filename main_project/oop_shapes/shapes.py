class Shape:
    def __init__(self, w, l) -> None:
        self.width = w
        self.len = l

    def print_size(self):
        print(
            """
            {} wide by {} long
            """.format(self.width, self.len)
        )


class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print(
            """
            I am {} wide by {} long
            """.format(self.width, self.len)
        )


shape1 = Shape(20,20)
shape1.print_size()

square1 = Square(20, 20)
square1.print_size()
