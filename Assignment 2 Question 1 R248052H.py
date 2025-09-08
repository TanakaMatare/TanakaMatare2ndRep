#   Question 1 : Create a simple base class(vehicle),2 subclasses (bike and car)
# Base Class
class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def description(self):
        """General description of a vehicle"""
        print(f"{self.name} is a vehicle with {self.wheels} wheels.")


# Subclass 1: Car
class Car(Vehicle):
    def __init__(self, name):
        # Call the constructor of the base class with 4 wheels
        super().__init__(name, 4)

    # Overriding the description() method
    def description(self):
        print(f"{self.name} is a car. It typically has {self.wheels} wheels and is great for road travel.")


# Subclass 2: Bike
class Bike(Vehicle):
    def __init__(self, name):
        # Call the constructor of the base class with 2 wheels
        super().__init__(name, 2)

    # Overriding the description() method
    def description(self):
        print(f"{self.name} is a bike. It usually has {self.wheels} wheels and is ideal for quick rides.")


#  Testing the classes
if __name__ == "__main__":
    # Creating objects
    v1 = Vehicle("Generic Vehicle", 3)   # A general vehicle with 3 wheels
    c1 = Car("Toyota Corolla")           # A car object
    b1 = Bike("Yamaha")                  # A bike object

    # Calling the description method
    v1.description()  #  Vehicle's version
    c1.description()  #  Car's overridden version
    b1.description()  #  Bike's overridden version



