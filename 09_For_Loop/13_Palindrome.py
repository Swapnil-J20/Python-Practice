# Write a program to check if a given number or string is a palindrome using a loop. Example: Input: "madam" → Output: True

def palindrome(phrase, debug=False):
	"""
	Checks if a given string or number is a palindrome using a for loop.

	Parameters:
		phrase (str): Input string or number to check.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		str: "a Palindrome" if the input is a palindrome, otherwise "not a Palindrome".
	"""
	length = len(phrase)

	# Loop to compare characters from the start and end
	for i in range(length // 2):
		if phrase[i] != phrase[length - i - 1]:
			if debug:
				print(f"Mismatch: Char at position {i} = {phrase[i]}, Char at position {length - i - 1} = {phrase[length - i - 1]}")
			return "not a Palindrome"

		if debug:
			print(f"Match: Char at position {i} = {phrase[i]}, Char at position {length - i - 1} = {phrase[length - i - 1]}")

	return "a Palindrome"


def main():
	"""
	Main function to handle user input and check for palindrome.
	"""
	text = input("Enter text or number to check if it's a Palindrome: ").strip().lower()

	# Ask if the user wants to enable debug mode
	debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

	# Check if the input is a palindrome
	result = palindrome(text, debug)

	# Print the result
	print(f"{text} is: {result}")


# Entry Point of the program
if __name__ == "__main__":
	main()
