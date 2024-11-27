# Write a program to print all prime numbers between 1 and 100 using a loop

def all_prime(value, debug=False):
    """
    Finds all prime numbers from 1 to the given value using a loop.

    Parameters:
        value (int): The upper limit for finding prime numbers.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        list: A list of prime numbers between 1 and value.
    """

    prime = []

    for i in range(2, value + 1):  # Start from 2, as 1 is not a prime number
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  # Check divisors up to √i
            if debug:
                print(f"Checking if {i} is divisible by {j}")
            if i % j == 0:
                if debug:
                    print(f"{i} is divisible by {j}, so it is not a prime.")
                is_prime = False
                break
        if is_prime:
            prime.append(i)
            if debug:
                print(f"{i} is a prime number.")

    return prime

def main():
    try:
        # Input from the user
        num = int(input("Enter an upper limit to find all prime numbers: "))

        if num < 2:
            print("There are no prime numbers less than 2.")
            return

        # Ask if the user wants to enable debug mode
        debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"

        # Get all prime numbers
        output = all_prime(num, debug=debug)

        # Display the result
        print(f"All prime numbers between 1 and {num}: {output}")

    except ValueError:
        print("Input Error: Please enter a valid integer.")


# Entry Point of the program
if __name__ == "__main__":
    main()