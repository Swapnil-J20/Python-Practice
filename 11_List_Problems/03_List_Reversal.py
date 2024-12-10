# Write a program to reverse a list without using the reverse() method

def reversal(data, debug=False):
    """
    Returns a reversed list from the provided list.

    Parameters:
        data (list): A list with items to be reversed
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        output (list): Reversed List
    """
    output = []
    length = len(data)

    while length != 0:
        j = data[length - 1]
        output.append(j)
        if debug:
            print(f"Step {len(data) - length + 1}: Adding {j} to reversed list, Current Reversed List: {output}")
        length = length - 1

    return output


def main():
    """
    Main function to gather input, reverse the list, and display the reversed result
    """
    try:
        # Input: List size
        size = int(input("Enter the size of the list: "))
        while size <= 0:
            print("Error: Enter a positive integer for list size.")
            size = int(input("Try again: "))

        # Input: List elements
        items = []
        print(f"Enter {size} items for the list:")
        while len(items) < size:
            i = input(f"Enter item {len(items) + 1}: ")
            items.append(i)

        # Debug mode
        debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Reverse the list
        result = reversal(items, debug)

        # Output
        print(f"\nOriginal List: {items}")
        print(f"Reversed List: {result}")

    except ValueError:
        print("Error: Please enter a valid number for the list size.")


# Entry Point of the Program
if __name__ == "__main__":
    main()
