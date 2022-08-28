import math


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


class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle():
    def __init__(self, height, base) -> None:
        self.height = height
        self.base = base

    def area(self):
        return (self.base * self.height) / 2


class Hexagon():
    def __init__(self, side_len) -> None:
        self.side_len = side_len

    def area(self):
        return 6 * self.side_len


# create rectangle object and print the area and perimeter
rect = Rectangle(10, 20)
print(rect.area(), rect.perimeter())
# change the rectangle size and then print area and perimeter of new rectangle
rect.change_size(20, 30)
print(rect.area(), rect.perimeter())

# Create a circle and find the area
circle = Circle(5)
print(circle.area())

# create triangle and print area
triangle = Triangle(4, 3)
print(triangle.area())

# create a hexagon and print the perimeter
hexagon = Hexagon(3)
print(hexagon.area())
