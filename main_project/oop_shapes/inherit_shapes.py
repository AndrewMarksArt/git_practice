class Shape:
    def __init__(self, w, l) -> None:
        self.width = w
        self.len = l

    def what_am_i(self):
        print("I am a shape")


class Square(Shape):
    def __init__(self, side_len) -> None:
        self.side_len = side_len

    def change_size(self, new_len):
        self.side_len = self.side_len + new_len

    def calc_perimeter(self):
        return self.side_len * 4

    def what_am_i(self):
        print(f"I am a square with a side length of {self.side_len}")


class Rectangle(Shape):
    def __init__(self, w, l) -> None:
        super().__init__(w, l)

    def calc_perimeter(self):
        return 2 * self.width + 2 * self.len

    def what_am_i(self):
        print(
            f"I am a rectangle with a width of {self.width}"
            + " and a length of {self.len}"
        )


shape1 = Shape(20, 20)
shape1.what_am_i()

square1 = Square(4)
square1.what_am_i()
print(square1.calc_perimeter())
square1.change_size(10)
print(square1.calc_perimeter())

rect1 = Rectangle(10, 5)
rect1.what_am_i()
print(rect1.calc_perimeter())
