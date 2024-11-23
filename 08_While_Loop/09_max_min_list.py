# Write a program to find the maximum and minimum numbers in a list using a loop.

def maxima_minima(values):
    """
    Finds the maximum and minimum numbers in a list using a loop.

    Parameters:
        values (list): List of numeric values.

    Returns:
        tuple: Minimum and maximum numbers in the list.
    """
    if not values:
        raise ValueError("The list is empty. Cannot find maximum and minimum.")

    # Initialize `large` and `small` with the first element
    large = values[0]
    small = values[0]

    i = 1  # Start loop from the second element
    while i < len(values):
        if values[i] > large:
            large = values[i]
        if values[i] < small:
            small = values[i]
        i += 1

    return small, large


def main():
    try:
        # Initialize empty list
        data = []

        # Input for total number of elements in list
        total = int(input("Enter the total number of elements in the list: "))

        # Check for non-positive total
        if total <= 0:
            print("Please enter a positive integer for the total.")
            return

        i = 0  # Initialize counter

        # Loop to collect elements
        while i < total:
            values = input(f"Enter element {i + 1}: ")

            try:
                if "." in values:
                    values = float(values)
                else:
                    values = int(values)

                data.append(values)  # Add valid number to list
                i += 1  # Increment counter
            except ValueError:
                print("Please enter a valid number.")

        # Output the final list
        print(f"Your list is: {data}")

        # Find and display the maximum and minimum values
        min_val, max_val = maxima_minima(data)
        print(f"The maximum number in the list is {max_val}")
        print(f"The minimum number in the list is {min_val}")

    except ValueError as e:
        print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
