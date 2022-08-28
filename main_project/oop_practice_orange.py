# python oop practice, create an "Orange" class to instantiate Orange objects

class Orange:
    def __init__(self, weight: float, color: str, mold=0) -> None:
        self.weight = weight
        self.color = color
        self.mold = mold
        print(f"Created a {color} Orange weighing {weight} ounces.")

    def rot(self, days, temp):
        self.mold = days * temp


class Apple:
    def __init__(self, weight, color, type, rot=0) -> None:
        self.weight = weight
        self.color = color
        self.type = type
        self.rot = rot


# create Oranges
orange1 = Orange(6, "dark orange")
print(orange1.weight)
print(orange1.color)

orange1.weight = 10
orange1.color = "light orange"

print(orange1.color, orange1.weight)

orange1.rot(2, 98.0)
print(orange1.mold)

# Create Apples
apple1 = Apple(4, "bright red", "Fuji", 0)
apple2 = Apple(7, "dark red", "Red Delicious", 0)
apple3 = Apple(10, "green", "Granny Smith", 0)
apple4 = Apple(3, "yellow", "Golden Delicious", 0)
