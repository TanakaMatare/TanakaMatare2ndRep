#Question 4 (Program to to execute a list of names by user input)
def main():
    # Ask user to enter names separated by commas
    user_input = input("Enter names separated by commas: ")

    # Split input into a list of names and remove extra spaces
    names = [name.strip() for name in user_input.split(",") if name.strip()]

    # Write names to names.txt
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

    print("\nNames written to 'names.txt' successfully!\n")

    # Read the file and print each name
    print("Reading names from 'names.txt':")
    with open("names.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes newline characters


if __name__ == "__main__":
    main()

