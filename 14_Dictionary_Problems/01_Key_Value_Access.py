# Key-Value Access: Create a dictionary and access its keys, values, and items.

def get_dict_elements(limit, debug=False):
	"""
	Collects elements for a dictionary from user input.

	Parameters:
		limit (int): Number of key-value pairs in the dictionary.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: A dictionary containing user-provided key-value pairs.
	"""
	elements = dict()

	print(f"\nProvide {limit} key-value pairs:")

	for i in range(limit):
		element_key = input(f"Enter the Key for Element {i + 1}: ")
		element_value = input(f"Enter the Value for Element {i + 1}: ")
		elements[element_key] = element_value

		if debug:
			print(f"[DEBUG] Current Dictionary: {elements}")

	return elements


def access_elements(data, debug=False):
	"""
	Accesses and prints keys, values, and items of a dictionary.

	Parameters:
		data (dict): Dictionary to access.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	print("\nAccessing Dictionary Elements:")

	# Keys
	print("\nKeys:")
	for key in data.keys():
		print(key)
		if debug:
			print(f"[DEBUG] Key: {key}")

	# Values
	print("\nValues:")
	for value in data.values():
		print(value)
		if debug:
			print(f"[DEBUG] Value: {value}")

	# Items
	print("\nItems (Key-Value Pairs):")
	for item in data.items():
		print(item)
		if debug:
			print(f"[DEBUG] Item: {item}")


def main():
	"""
	Main function to gather input, create a dictionary, and access its elements.
	"""
	try:
		size = int(input("Enter the size of the Dictionary: "))

		while size <= 0:
			print("Error: Enter a Positive Integer for Size.")
			size = int(input("Try again. Enter the size of the Dictionary: "))

		debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect dictionary elements
		items = get_dict_elements(size, debug)

		# Access dictionary keys, values, and items
		access_elements(items, debug)

	except ValueError:
		print("Error: Enter a valid positive integer for the size of the dictionary.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
