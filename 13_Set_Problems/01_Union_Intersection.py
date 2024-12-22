# Union and Intersection: Perform union, intersection, and difference operations on two sets

def get_set_elements(limit, debug=False):
    """
    Collects elements for a set from user input.

    Parameters:
        limit (int): Number of elements in the set.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        set: Set containing the user-provided elements.
    """
    elements = set()
    print(f"Enter {limit} unique elements for the set:")

    while len(elements) < limit:
        element = input(f"Enter element {len(elements) + 1}: ")
        elements.add(element)
        if debug:
            print(f"[DEBUG] Current Set: {elements}")

    return elements


def set_operations(set_one, set_two, debug=False):
    """
    Performs union, intersection, and difference operations on two sets.

    Parameters:
        set_one (set): First set.
        set_two (set): Second set.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        tuple: Results of union, intersection, and difference operations.
    """
    union_result = set_one.union(set_two)
    intersection_result = set_one.intersection(set_two)
    difference_result = set_one.difference(set_two)

    if debug:
        print(f"[DEBUG] Union: {union_result}")
        print(f"[DEBUG] Intersection: {intersection_result}")
        print(f"[DEBUG] Difference (Set One - Set Two): {difference_result}")

    return union_result, intersection_result, difference_result


def main():
    """
    Main function to demonstrate set operations.
    """
    try:
        # Input: Sizes of the sets
        size_one = int(input("Enter the size of the first set: "))
        size_two = int(input("Enter the size of the second set: "))

        while size_one <= 0 or size_two <= 0:
            print("Error: Sizes must be positive integers.")
            if size_one <= 0:
                size_one = int(input("Enter the size of the first set: "))
            if size_two <= 0:
                size_two = int(input("Enter the size of the second set: "))

        # Debug mode
        debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

        # Collect set elements
        set_one = get_set_elements(size_one, debug)
        set_two = get_set_elements(size_two, debug)

        # Perform set operations
        union, intersection, difference = set_operations(set_one, set_two, debug)

        # Display results
        print(f"\nSet One: {set_one}")
        print(f"Set Two: {set_two}")
        print(f"\nUnion: {union}")
        print(f"Intersection: {intersection}")
        print(f"Difference (Set One - Set Two): {difference}")

    except ValueError:
        print("Error: Please enter valid integers for set sizes.")


# Entry Point of the Program
if __name__ == "__main__":
    main()
