# Set Conversion: Convert a string into a set of characters and count the unique characters.

import string

def unique_chars(text, exclude_special=False, debug=False):
	"""
	This function takes a string and returns the unique count of characters.

	Parameters:
		text (str): String of characters.
		exclude_special (bool): Whether to exclude special characters (default is False).
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		count (int): Unique count of characters.
	"""

	data = set()

	for char in text:
		if exclude_special and char in string.punctuation + string.whitespace:
			continue

		data.add(char)
		if debug:
			print(f"[DEBUG] Current Unique Set: {data} (Size: {len(data)})")

	count = len(data)
	return count

def main():
	"""
	Main function to gather input and count unique characters.
	"""
	try:
		# Input string
		phrase = input("Enter a word or sentence to get the count of Unique Characters: ").strip().lower()

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Exclude special characters
		exclude_special = input("Exclude spaces and punctuation? (yes/no): ").lower().strip() == "yes"

		# Count unique characters
		num = unique_chars(phrase, exclude_special, debug)

		# Output result
		print(f"\nUnique Characters in '{phrase}' are: {num}")

	except Exception as e:
		print(f"Error: {e}")

# Entry Point of the Program
if __name__ == "__main__":
	main()
