# Write a program to print the Fibonacci series up to n terms using a loop

def fibonacci(n):
    """
    Prints the Fibonacci series up to n terms.

    Parameters:
        n (int): The number of terms in the Fibonacci series to generate.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return

    a = 0  # Starting values for Fibonacci sequence
    b = 1  # Starting values for Fibonacci sequence
    i = 0

    while i < n:
        print(a, end=" ")
        a, b = b, a + b  # Update the two terms
        i += 1
    print()  # Add a newline at the end


def main():
    try:
        num = int(input("Enter the number of terms in the Fibonacci series: "))
        fibonacci(num)
    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
