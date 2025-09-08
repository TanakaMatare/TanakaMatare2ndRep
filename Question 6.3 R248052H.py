#Question 6 (Function divide_numbers)

def divide_numbers(numerator, denominator):
    """
    Divides numerator by denominator, handling division by zero and invalid types.

    Parameters:
        numerator (int or float): The numerator.
        denominator (int or float): The denominator.

    Returns:
        float: The result of division if successful.
        None: If an error occurs, prints an error message.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")
    except TypeError:
        print("❌ Error: Invalid input type. Please provide numbers only.")


def main():
    while True:
        try:
            num = float(input("Enter the numerator: "))
            denom = float(input("Enter the denominator: "))

            result = divide_numbers(num, denom)
            if result is not None:
                print(f"✅ Result: {num} / {denom} = {result}")
            break  # Exit loop after successful operation
        except ValueError:
            print("❌ Invalid input! Please enter numeric values only.")


if __name__ == "__main__":
    main()
