# Calculate the sum and average of a list of numbers.

def sum_avg(data, debug=False):
    """
    Returns Sum and Average of numbers from the provided list.

    Parameters:
        data (list): A list of numbers to calculate their sum and average
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        cumulative (float): Sum of numbers
        mean (float): Average of numbers
    """
    cumulative = 0

    for index, value in enumerate(data):
        cumulative += value
        if debug:
            print(f"Step {index + 1}: Current Sum = {cumulative}")

    mean = cumulative / len(data) if len(data) > 0 else 0
    return cumulative, mean


def main():
    """
    Main function to gather input, find Sum & Average of numbers, and display the result
    """
    try:
        # Input: List size
        size = int(input("Enter the size of the list: "))
        while size <= 0:
            print("Error: Enter a Positive Integer for the list size.")
            size = int(input("Try again: "))

        # Input: List elements
        items = []
        print(f"Enter {size} numbers:")
        while len(items) < size:
            try:
                num = float(input(f"Enter number {len(items) + 1}: "))
                items.append(num)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        # Debug mode
        debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Process: Calculate sum and average
        total, average = sum_avg(items, debug)

        # Output: Display results
        print(f"\nOriginal Data: {items}")
        print(f"Sum of Data: {round(total, 2)}")
        print(f"Average of Data: {round(average, 2)}")

    except ValueError:
        print("Error: Please enter a valid number for the list size.")


# Entry Point of the Program
if __name__ == "__main__":
    main()
