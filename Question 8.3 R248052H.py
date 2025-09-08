#Question 8 (10 random intergers between 1 and 100)

import random


def generate_random_numbers(count=10, start=1, end=100):
    """
    Generates a list of random integers.

    Parameters:
        count (int): Number of random integers to generate.
        start (int): Minimum value.
        end (int): Maximum value.

    Returns:
        list: List of random integers.
    """
    return [random.randint(start, end) for _ in range(count)]


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Parameters:
        numbers (list): List of numeric values.

    Returns:
        float: Average of the numbers.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    random_numbers = generate_random_numbers()
    print("Random numbers generated:", random_numbers)

    avg = calculate_average(random_numbers)
    print(f"The average of the generated numbers is: {avg}")


if __name__ == "__main__":
    main()
