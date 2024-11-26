# Write a program to count the frequency of each character in a string using a loop. Example: Input: "banana" → Output: { 'b': 1, 'a': 3, 'n': 2 }

def count_char(data, debug=False):
    """
    Counts the frequency of each character in a string using a loop.
    Includes an optional debug parameter for step-by-step computation.

    Parameters:
        data (str): The input string.
        debug (bool): Whether to display debug prints (default is False).

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    i = 0
    length = len(data)
    result = {}

    while i < length:
        
        char = data[i]
        
        # Debug print: Current character and dictionary state
        if debug:
            print(f"Step {i + 1}: Processing character '{char}'")
            print(f"Current dictionary: {result}")

        # Update the count for each character
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1

        if debug:
            print(f"Updated dictionary after '{char}': {result}\n")

        i += 1

    return result


def main():
    # Input from the user
    text = input("Enter a string or number for character count: ")

    # Ask if the user wants to enable debug mode
    debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"

    # Count character frequencies
    result = count_char(text, debug=debug)

    # Display the result
    print(f"Character frequencies: {result}")


# Entry Point of the program
if __name__ == "__main__":
    main()
