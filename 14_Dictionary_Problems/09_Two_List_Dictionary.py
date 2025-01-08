# Dictionary from Two Lists: Create a dictionary from two lists:
# Example: Input: ['a', 'b'], [1, 2] → Output: {'a': 1, 'b': 2}

def create_dict_from_lists(keys, values, debug=False):
	"""
	Creates a dictionary by combining two lists: keys and values.

	Parameters:
		keys (list): List containing keys for the dictionary.
		values (list): List containing values corresponding to the keys.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary created by combining the two lists.
	"""
	# Ensure both lists have the same length
	if len(keys) != len(values):
		print("Error: The number of keys and values must be the same.")
		return {}

	dictionary = {}

	for i in range(len(keys)):
		dictionary[keys[i]] = values[i]

		if debug:
			print(f"[DEBUG] Added Key: {keys[i]}, Value: {values[i]} - Current Dictionary: {dictionary}")

	return dictionary


def get_list_elements(limit, label, debug=False):
	"""
	Collects elements for a list from user input.

	Parameters:
		limit (int): Number of elements in the list.
		label (str): Label indicating whether the list is for keys or values.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: List containing the user-provided elements.
	"""
	elements = []

	print(f"\nEnter {limit} elements for the {label} list:")
	for i in range(limit):
		element = input(f"Enter element {i + 1}: ")
		elements.append(element)
		if debug:
			print(f"[DEBUG] Current {label} List: {elements}")

	return elements


def main():
	"""
	Main function to gather input, create a dictionary from two lists, and display the result.
	"""
	try:
		# Input: Size of the lists
		size = int(input("Enter the number of elements for both lists: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the number of elements for both lists: "))

		# Enable Debug Mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect keys and values
		keys = get_list_elements(size, "Keys", debug)
		values = get_list_elements(size, "Values", debug)

		# Create dictionary from lists
		result = create_dict_from_lists(keys, values, debug)

		# Display result
		print(f"\nKeys List: {keys}")
		print(f"Values List: {values}")
		print(f"Generated Dictionary: {result}")

	except ValueError:
		print("Error: Please enter a valid positive integer for the size of the lists.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
