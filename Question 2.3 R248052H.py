#Question 2 (Function calculate_average)

def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
        *args (int or float): One or more numbers.

    Returns:
        float: The average of the provided numbers.
               Returns 0 if no numbers are provided.
    """

    if len(args) == 0:
        return 0
    return sum(args) / len(args)


def main():
    print("Enter numbers separated by spaces to calculate their average:")
    user_input = input("Numbers: ")

    try:
        # Convert input into a list of floats
        numbers = [float(num) for num in user_input.split()]

        # Call function with unpacked list
        avg = calculate_average(*numbers)
        print(f"The average is: {avg}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()

