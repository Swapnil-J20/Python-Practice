# Write a program to find the sum of digits of a number using a loop.

def digit_sum(value):
    """
    Calculates the sum of the digits of a number using a loop.

    Parameters:
        value (int): The number whose digits will be summed.

    Returns:
        int: Sum of the digits.
    """
    ans = 0

    while value > 0:
        ans += value % 10  # Extract the last digit and add it to the sum
        value //= 10       # Remove the last digit

    return ans


def main():
    try:
        # Take input from the user
        num = int(input("Enter the number: "))

        # Calculate and display the sum of digits
        result = digit_sum(num)
        print(f"The sum of the digits is: {result}")

    except ValueError:
        print("Error: Enter a valid integer.")


# Entry point of the program
if __name__ == "__main__":
    main()

