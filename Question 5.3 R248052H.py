#Question 5 (Convert temperature Celsius to Fahrenheit)

def main():
    # Ask the user to enter Celsius temperatures separated by spaces
    user_input = input("Enter temperatures in Celsius separated by spaces: ")

    try:
        # Convert input string to a list of floats
        celsius_temps = [float(temp) for temp in user_input.split()]

        # Use lambda and map to convert Celsius to Fahrenheit
        fahrenheit_temps = list(map(lambda c: c * 9 / 5 + 32, celsius_temps))

        # Print the result
        print("\nCelsius temperatures: ", celsius_temps)
        print("Converted to Fahrenheit: ", fahrenheit_temps)

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()
