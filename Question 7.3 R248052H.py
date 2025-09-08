#Question 7 (function check_positive in a try block )

# Define custom exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    pass


# Function to check if number is positive
def check_positive(number):
    """
    Raises NegativeNumberError if the number is negative.

    Parameters:
        number (int or float): The number to check.

    Returns:
        str: Confirmation message if number is positive or zero.
    """
    if number < 0:
        raise NegativeNumberError("❌ Error: Negative numbers are not allowed!")
    return "✅ Number is positive or zero."


def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)

            # Check if the number is positive
            result = check_positive(number)
            print(result)
            break  # Exit loop after valid input
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")
        except NegativeNumberError as e:
            print(e)


if __name__ == "__main__":
    main()
