# Reverse Mapping: Reverse the keys and values in a dictionary.
# Example: Input: {'a': 1, 'b': 2} → Output: {1: 'a', 2: 'b'}

def get_dict_elements(limit, debug=False):
	"""
	Collects elements for a Dictionary from user input.

	Parameters:
		limit (int): Size of the Dictionary
		debug (bool): Whether to display debug prints (default is False)

	Returns:
		dict: Dictionary with Keys and Values
	"""
	elements = dict()

	print("\nProvide key-value pairs for the dictionary:")
	for i in range(limit):
		key = input(f"Enter Key {i + 1}: ")
		value = input(f"Enter Value {i + 1}: ")
		elements[key] = value
		if debug:
			print(f"[DEBUG] Current Dictionary: {elements}")

	return elements

def reverse_mapping(data, debug = False):
	"""
	Reverses the keys and values in a dictionary

	Parameters:
		data (dict): Dictionary with keys and values
		debug (bool): Whether to display debug prints (default is False)

	Returns:
		dict: Reversed dictionary
	"""

	result = dict()

	for i in data:
		result_value = i
		result_key = data[i]

		result[result_key] = result_value

		if debug:
			print(f"[DEBUG] Key: {result_key}, Value: {result_value}, Result: {result}")

	return result


def main():
	"""
	Main function to gather input, create a dictionary, and reverse its elements
	"""

	try:
		size = int(input("Enter the Size of the Dictionary: "))

		while size <= 0:
			print("Error: Enter Positive Number for Size")
			size = int(input("Try again. Enter the Size of the Dictionary: "))

		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect dictionary elements
		items = get_dict_elements(size, debug)

		# Reverse the dictionary
		output = reverse_mapping(items, debug)

		# Display results
		print(f"\nOriginal Dictionary: {items}")
		print(f"Reversed Dictionary: {output}")

	except ValueError:
		print("Error: Enter a valid positive integer for the size of the dictionary.")

if __name__ == "__main__":
	main()