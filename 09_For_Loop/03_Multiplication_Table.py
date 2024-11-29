# Write a program to print the multiplication table of a given number n

def multiplication(val, debug=False):
    """
    Prints the multiplication table for a given number.

    Parameters:
        val (int): Number for which the multiplication table is to be created.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        None
    """
    max_factor = 10  # Maximum multiplier

    # Loop to generate and print the multiplication table
    for i in range(1, max_factor + 1):
        result = val * i
        if debug:
            print(f"Debug: Step {i}: val = {val}, i = {i}, result = {result}")
        print(f"{val} * {i} = {result}")


def main():
    """
    Main function to handle user input and initiate the multiplication table.
    """
    try:
        # Input from the user
        num = int(input("Enter a number to get the multiplication table: "))

        # Ask if the user wants to enable debug mode
        debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Generate multiplication table
        multiplication(num, debug)

    except ValueError:
        print("Input Error: Please enter a valid number.")


# Entry Point of the program
if __name__ == "__main__":
    main()