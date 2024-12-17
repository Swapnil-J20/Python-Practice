# Tuple to List: Convert a tuple into a list, modify it, and then convert it back into a tuple

def get_input(limit, debug=False):
    """
    Collects elements for a tuple from user input.

    Parameters:
        limit (int): Number of elements in the tuple.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        tuple: Tuple containing the user-provided elements.
    """
    elements = []
    print(f"\nEnter {limit} elements for the tuple:")

    for i in range(limit):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element)
        if debug:
            print(f"[DEBUG] Added element: {element}")

    data = tuple(elements)
    if debug:
        print(f"[DEBUG] Final Tuple: {data}")
    return data

def tuple_conversion(data, debug=False):
    """
    Convert a tuple to a list, modify it, and convert it back to a tuple.

    Parameters:
        data (tuple): Tuple to be converted and modified.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        tuple: The modified tuple and the list.
    """
    # Convert the tuple to a list
    data_list = list(data)
    if debug:
        print(f"[DEBUG] Tuple to List: {data_list}")

    # Modify the list (for example, append a new item)
    data_list.append("New Item")
    if debug:
        print(f"[DEBUG] Modified List: {data_list}")

    # Convert the list back to a tuple
    data_tuple = tuple(data_list)
    if debug:
        print(f"[DEBUG] List to Tuple: {data_tuple}")

    return data_list, data_tuple

def main():
    """
    Main function to demonstrate tuple to list conversion, modification, and re-conversion to tuple.
    """
    try:
        # Input the size of the tuple
        size = int(input("Enter the size of the tuple: "))

        while size <= 0:
            print("Error: Enter a positive integer for the size.")
            size = int(input("Try again. Enter the size of the tuple: "))

        # Debug mode
        debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Collect tuple elements
        items = get_input(size, debug)

        # Convert tuple to list, modify it, and convert it back to tuple
        list_items, tuple_items = tuple_conversion(items, debug)

        print(f"\nTuple to List Conversion: {list_items}")
        print(f"List to Tuple Conversion: {tuple_items}")

    except ValueError:
        print("Error: Please enter a valid number for the size.")

# Entry Point of the Program
if __name__ == "__main__":
    main()
