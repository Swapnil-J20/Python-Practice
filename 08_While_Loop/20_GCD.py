# Write a program to find the greatest common divisor (GCD) of two numbers using a loop

def gcd(val1, val2, debug=False):
    """
    Calculates the GCD of two numbers using the Euclidean algorithm.

    Parameters:
        val1 (int): First integer.
        val2 (int): Second integer.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        int: Greatest Common Divisor of the two numbers.
    """
    if val1 == 0:
        return val2
    if val2 == 0:
        return val1

    while val2 != 0:
        if debug:
            print(f"val1 = {val1}, val2 = {val2}, val1 % val2 = {val1 % val2}")
        val1, val2 = val2, val1 % val2

    return val1


def main():
    try:
        print("This program will compute the Greatest Common Divisor (GCD) of two numbers.")

        # Inputs from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 < 0 or num2 < 0:
            print("Only non-negative integers are allowed.")
            return

        # Ask if the user wants to enable debug mode
        debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"

        # Calculate GCD
        result = gcd(num1, num2, debug)

        print(f"GCD of {num1} and {num2} is: {result}")

    except ValueError:
        print("Input Error: Please enter valid integers.")


# Entry Point of the program
if __name__ == "__main__":
    main()
