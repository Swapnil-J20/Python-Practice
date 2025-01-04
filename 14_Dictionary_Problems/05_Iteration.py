# Iteration: Iterate over a dictionary and print all key-value pairs

def get_dict_elements(limit, debug=False):
    """
    Collects elements for a Dictionary from user input.

    Parameters:
        limit (int): Size of the Dictionary.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        dict: Dictionary with Keys and Values.
    """
    elements = {}
    print("\nProvide key-value pairs for the dictionary:")

    for i in range(limit):
        element_key = input(f"Enter Key {i + 1}: ")
        element_value = input(f"Enter Value {i + 1}: ")
        elements[element_key] = element_value

        if debug:
            print(f"[DEBUG] Current Dictionary: {elements}")

    return elements


def dict_iteration(data, debug=False):
    """
    Iterates over a dictionary and prints all key-value pairs.

    Parameters:
        data (dict): The dictionary to iterate over.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        None
    """
    for key, value in data.items():
        if debug:
            print(f"[DEBUG] Processing Key: {key}, Value: {value}")
        print(f"Key: {key}, Value: {value}")


def main():
    """
    Main function to gather input, create a dictionary, and update its elements.
    """
    try:
        # Input: Size of the dictionary
        size = int(input("Enter the size of the dictionary: "))

        while size <= 0:
            print("Error: Enter a positive integer for the size.")
            size = int(input("Try again. Enter the size of the dictionary: "))

        # Enable Debug Mode
        debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

        # Collect dictionary elements
        items = get_dict_elements(size, debug)

        # Iterate and print key-value pairs
        dict_iteration(items, debug)

    except ValueError:
        print("Error: Please enter a valid positive integer for the size of the dictionary.")


# Entry Point of the Program
if __name__ == "__main__":
    main()



