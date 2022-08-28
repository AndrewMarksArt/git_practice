# python oop practice, create an "Orange" class to instantiate Orange objects

class Orange:
    def __init__(self, weight: float, color: str) -> None:
        self.weight = weight
        self.color = color
        print(f"Created a {color} Orange weighing {weight} ounces.")


orange1 = Orange(6, "dark orange")
print(orange1.weight)
print(orange1.color)

orange1.weight = 10
orange1.color = "light orange"

print(orange1.color, orange1.weight)
