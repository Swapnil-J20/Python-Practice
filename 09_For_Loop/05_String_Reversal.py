# Write a program to reverse a given string using a loop


def string_reversal(phrase, debug=False):
	"""
	Reverses the given string using a loop.

	Parameters:
		phrase (str): The string to be reversed.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		str: The reversed string.
	"""
	length = len(phrase) - 1  # Start index for reversal
	result = ""  # To store the reversed string

	for char in phrase:
		result = result + phrase[length]  # Add the character from the end
		if debug:
			print(f"Step: Adding '{phrase[length]}' to result = '{result}'")
		length = length - 1  # Move to the previous character

	return result


def main():
	"""
	Main function to handle user input and reverse the string.
	"""
	try:
		# Input from the user
		text = input("Enter a string to reverse it: ")

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Reverse the string
		output = string_reversal(text, debug)

		# Print the result
		print(f"'{text}' reversed is: '{output}'")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")


# Entry Point of the program
if __name__ == "__main__":
	main()
