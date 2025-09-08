#Question 3 (Use try block)

def main():
    while True:
        user_input = input("Enter a number: ")
        try:
            number = float(user_input)  # try converting input to a number
            print(f"✅ You entered a valid number: {number}")
            break  # exit loop once valid number is entered
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
