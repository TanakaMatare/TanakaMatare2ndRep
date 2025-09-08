# Question 2 (Shapes and Polymorphism)
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area using polymorphism
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


if __name__ == "__main__":
    shapes = []
    n = int(input("How many shapes do you want to enter? "))

    for i in range(n):
        print(f"\nShape {i+1}:")
        shape_type = input("Enter shape type (circle/rectangle): ").strip().lower()

        if shape_type == "circle":
            r = float(input("Enter radius: "))
            shapes.append(Circle(r))
        elif shape_type == "rectangle":
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            shapes.append(Rectangle(w, h))
        else:
            print("Invalid shape, skipping...")

    print("\nTotal area of all shapes:", total_area(shapes))

