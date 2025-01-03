# Delete Keys: Write a program to remove a key from a dictionary

def get_dict_elements(limit, debug=False):
	"""
	Collects elements for a Dictionary from user input.

	Parameters:
		limit (int): Size of the Dictionary.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary with Keys and Values.
	"""
	elements = {}

	print("\nProvide key-value pairs for the dictionary:")
	for i in range(limit):
		element_key = input(f"Enter Key {i + 1}: ")
		element_value = input(f"Enter Value {i + 1}: ")
		elements[element_key] = element_value

		if debug:
			print(f"[DEBUG] Current Dictionary: {elements}")

	return elements


def remove_key(data, debug=False):
	"""
	Removes a user-provided key from a copy of the dictionary, preserving the original.

	Parameters:
		data (dict): The original dictionary.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: A copy of the dictionary with the specified key removed.
	"""

	# Create a copy to avoid modifying the original dictionary
	new_data = data.copy()

	print(f"\nCurrent Dictionary: {new_data}")

	element = input("Enter key to be removed: ")

	while element not in new_data:
		print("Error: Specified key not in dictionary. Try again.")
		element = input("Enter key to be removed: ")

	new_data.pop(element)

	if debug:
		print(f"[DEBUG] Key '{element}' removed. Updated Dictionary: {new_data}")

	return new_data


def main():
	"""
	Main function to gather input, create a dictionary, and update its elements.
	"""
	try:
		# Input: Size of the dictionary
		size = int(input("Enter the size of the dictionary: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the dictionary: "))

		# Enable Debug Mode
		debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect dictionary elements
		items = get_dict_elements(size, debug)

		# Remove a key from a copy of the dictionary
		output = remove_key(items, debug)

		# Display results
		print(f"\nOriginal Dictionary: {items}")
		print(f"Dictionary post Key removal: {output}")

	except ValueError:
		print("Error: Please enter a valid positive integer for the size of the dictionary.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
