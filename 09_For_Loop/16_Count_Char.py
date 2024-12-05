# Write a program to count the frequency of each character in a string using a loop. Example: Input: "banana" → Output: { 'b': 1, 'a': 3, 'n': 2 }

def count_char(text, debug=False):
	"""
	Counts the frequency of each character in a given string.

	Parameters:
		text (str): The input string.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: A dictionary containing the character frequencies.
	"""
	counter = {}  # Dictionary to store character counts

	for i, char in enumerate(text):
		if char not in counter:
			counter[char] = 1  # Initialize count for a new character
			if debug:
				print(f"Step {i + 1}: '{char}' added to counter with count 1.")
		else:
			counter[char] = counter[char] + 1  # Increment count for existing character
			if debug:
				print(f"Step {i + 1}: Incremented count of '{char}' to {counter[char]}.")

	return counter


def main():
	"""
	Main function to handle user input and count the frequency of characters.
	"""
	try:
		# Input the string
		phrase = input("Enter the phrase to count characters: ")

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Count the characters
		result = count_char(phrase, debug)

		# Print the result
		print(f"Original Phrase: '{phrase}'")
		print(f"Characterwise Count: {result}")

	except ValueError:
		print("Input Error: Please enter a valid string.")


# Entry Point of the program
if __name__ == "__main__":
	main()
