class Rectangle():
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.width + 2 * self.length

    def change_size(self, width, length):
        self.width = width
        self.length = length


rect = Rectangle(10, 20)
print(rect.area(), rect.perimeter())

rect.change_size(20, 30)
print(rect.area(), rect.perimeter())
