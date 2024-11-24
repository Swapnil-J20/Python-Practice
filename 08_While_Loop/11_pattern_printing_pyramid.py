# Print a pyramid of stars for a given number of rows:

def pattern(lines):
    """
    Prints Pyramid pattern of stars.

    Parameters:
        points (int): The number of rows in the pyramid.
    """
    if lines <= 0:
        print("Please enter a valid positive integer.")
        return

    i = 1

    while i <= lines:

        # Calculate spaces for alignment
        spaces = " " * (lines - i)
        
        # Calculate stars for the current row
        stars = "*" * (2 * i - 1)
        
        # Print the row
        print(f"{spaces}{stars}")
        i += 1

def main():
    try:
        # Take input from the user
        rows = int(input("Enter the number of rows for the Pyramid: "))
        pattern(rows)
        
    except ValueError:
        print("Error: Please enter a valid integer.")

# Entry Point of the program
if __name__ == "__main__":
    main()
