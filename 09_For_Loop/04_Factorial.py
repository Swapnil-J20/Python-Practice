# Write a program to calculate the factorial of a number using a loop

def factorial(val, debug=False):
    """
    Calculates the factorial of a given number.

    Parameters:
        val (int): Number for which the factorial is to be calculated.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        int or str: Returns the factorial or an error message for invalid input.
    """
    if val < 0:
        return "#Error: Negative numbers don't have a factorial."

    i = 1
    result = 1

    # Loop to calculate factorial
    for i in range(1, val + 1):
        result = result * i
        if debug:
            print(f"Step {i}: result = {result}")

    return result


def main():
    """
    Main function to handle user input and calculate the factorial.
    """
    try:
        # Input from the user
        num = int(input("Enter a number to calculate its factorial: "))

        # Ask if the user wants to enable debug mode
        debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Calculate factorial
        output = factorial(num, debug)

        # Print the result
        print(f"Factorial of {num} is {output}")

    except ValueError:
        print("Input Error: Please enter a valid integer.")


# Entry Point of the program
if __name__ == "__main__":
    main()
