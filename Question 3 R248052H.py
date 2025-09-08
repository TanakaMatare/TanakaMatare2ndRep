# Base class
class Shape:
    def __init__(self, name="Shape"):
        self.name = name
        print(f"{self.name} initialized")

    def calculate_area(self):
        # Base version does nothing (placeholder)
        print("Shape.calculate_area() called, but not implemented")
        return 0


# Derived class
class Rectangle(Shape):
    def __init__(self, width, height):
        # Call Shape's constructor using super()
        super().__init__(name="Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        # Call the base class method (even if it does nothing)
        super().calculate_area()
        # Then do Rectangle-specific area calculation
        return self.width * self.height


if __name__ == "__main__":
    # Take input from user
    w = float(input("Enter the width of the rectangle: "))
    h = float(input("Enter the height of the rectangle: "))

    rect = Rectangle(w, h)
    print(f"Area of rectangle: {rect.calculate_area()}")
