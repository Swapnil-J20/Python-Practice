"""
	Write a program to check if a given number or string is a palindrome using a loop.
	Example: Input: "madam" → Output: True
"""

def palindrome(phrase):
	"""
    Checks if a given string or number is a palindrome using a loop.

    Parameters:
        phrase (str): The input string or number to check.

    Returns:
        str: "Palindrome" if the input is a palindrome, otherwise "Not a Palindrome".
    """
    # Initialize variables

    length = len(phrase)
    i = 0

    # Compare characters from both ends
    while i < length // 2:
        if phrase[i] != phrase[length - i - 1]:
            return "Not a Palindrome"
        i = i + 1

    return "Palindrome"


def main():

	text = input("Enter text or number to check if it is a Palindrome: ")

	result = palindrome(text)

	print(f"{text} is {result}")

# Entry Point of the program
if __name__ == "__main__":
    main()