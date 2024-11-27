#Write a program to check if a number is an Armstrong number. Example: Input: 153 → Output: True (because 1³ + 5³ + 3³ = 153)

def armstrong_number(value, debug=False):
    """
    Checks if a number is an Armstrong number.

    Parameters:
        value (int): The number to check.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        str: Returns a confirmation string if it's an Armstrong number or not.
    """
    total = 0
    original = value
    digits = 0

    # Calculate the number of digits
    temp = value
    while temp > 0:
        temp = temp // 10
        digits = digits + 1

    # Calculate the sum of powers
    temp = value
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10
        if debug:
            print(f"Processing digit: {digit}, Raising to power {digits}, Current total: {total}")

    if total == original:
        return "an Armstrong Number"
    else:
        return "not an Armstrong Number"


def main():
    try:
        # Input from the user
        num = int(input("Enter a number to check if it's an Armstrong number: "))

        if num < 0:
            print("There are no Armstrong Numbers below 1.")
            return

        # Ask if the user wants to enable debug mode
        debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"

        # Check if the number is an Armstrong number
        output = armstrong_number(num, debug=debug)

        print(f"{num} is {output}")

    except ValueError:
        print("Input Error: Please enter a valid positive integer.")


# Entry Point of the program
if __name__ == "__main__":
    main()
