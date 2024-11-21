# Write a program to count the number of even and odd numbers in a list

def count_odd_even(values):
    """
    Counts even and odd numbers in a list using a while loop.

    Parameters:
        values (list): A list of integers.

    Returns:
        tuple: A tuple containing the count of even and odd numbers.
    """
    even_count = 0
    odd_count = 0
    i = 0
    length = len(values)

    while i < length:
        if values[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        i += 1

    return even_count, odd_count


def main():
    # Predefined list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Count even and odd numbers
    even, odd = count_odd_even(numbers)

    # Output the counts
    print(f"Count of even numbers: {even}")
    print(f"Count of odd numbers: {odd}")


if __name__ == "__main__":
    main()
