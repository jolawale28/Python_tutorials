class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    # Override
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    # Override
    def move(self):
        print("Fly!")

vehicle = Vehicle("Toyota", "2013")
car = Car("Honda", 2019)
boat = Boat("Titanic", "1918")
plane = Plane("Boeing", "747")

vehicle.move()
car.move()
boat.move()
plane.move()