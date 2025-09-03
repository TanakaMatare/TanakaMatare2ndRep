# Demonstrating variables, constants, and the print function

# Constant (by convention written in UPPERCASE)
PI = 3.14159

# Ask the user to enter values
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

# Calculations
circle_area = PI * (radius ** 2)
cylinder_volume = PI * (radius ** 2) * height

# Display results using f-strings (modern and clean)
print(f"\nRadius: {radius}")
print(f"Height: {height}")
print(f"Circle Area: {circle_area}")
print(f"Cylinder Volume: {cylinder_volume}")
