# Set to List: Convert a set into a list, sort it, and print the sorted list

def get_input(limit, debug):
    """
    Creates and returns a Set of unique values.
    """
    data = set()

    for i in range(limit):
        value = input(f"Enter the {i + 1} value: ")
        data.add(value)
        if debug:
            print(f"[DEBUG] Current Set: {data}")
    return data

def sorting(data, debug):
    """
    Converts a set into a sorted list and returns it.
    """
    list_data = list(data)
    if debug:
        print(f"[DEBUG] List before sorting: {list_data}")
    list_data.sort()
    if debug:
        print(f"[DEBUG] List after sorting: {list_data}")
    return list_data

def main():
    """
    Main program to gather inputs, convert Set to List, and display the sorted list.
    """
    try:
        size = int(input("Enter the size of the Set: "))
        while size <= 0:
            print("Error: Enter a Positive Integer for Size")
            size = int(input("Try again. Enter the size of the Set: "))

        debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

        items = get_input(size, debug)
        if len(items) < size:
            print(f"Warning: Only {len(items)} unique elements were added.")

        output = sorting(items, debug)

        print(f"\nInitial Set: {items}")
        print(f"Final Sorted List: {output}")

    except ValueError:
        print("Error: Enter a Positive Integer for Size")

# Entry Point of the Program
if __name__ == "__main__":
    main()
