class Dog():
    def __init__(self, name, breed, owner) -> None:
        self.name = name
        self.breed = breed
        self.owner = owner


class Horse():
    def __init__(self, name, color, rider) -> None:
        self.name = name
        self.color = color
        self.rider = rider


class Person():
    def __init__(self, name) -> None:
        self.name = name


mick = Person("Mick")
stella = Dog("stella", "bulldog", mick)

rider_rick = Person("rick")
lucky = Horse("lucky", "black", rider_rick)

print(stella.owner.name)
print(lucky.rider.name)
