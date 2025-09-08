#Question 1 (function classify_number)
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def main():
    while True:
        user_input = input("Enter an integer: ")
        try:
            number = int(user_input)  # Try converting to integer
            result = classify_number(number)
            print(f"The number {number} is {result}.")
            break  # Exit loop after valid input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
