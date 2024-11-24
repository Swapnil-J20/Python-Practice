# Print a right-angled triangle of stars for a given number of rows:

def pattern(points):
    """
    Prints a right-angled triangle pattern of stars.

    Parameters:
        points (int): The number of rows in the triangle.
    """
    if points <= 0:
        print("Please enter a valid positive integer.")
        return

    i = 1
    while i <= points:
        print("*" * i)  # Print i stars in the current row
        i = i + 1  # Increment to the next row


def main():
    try:
        # Take input from the user
        stars = int(input("Enter the number of rows for the right-angled triangle: "))
        pattern(stars)
    except ValueError:
        print("Error: Please enter a valid integer.")

# Entry Point of the program
if __name__ == "__main__":
    main()
