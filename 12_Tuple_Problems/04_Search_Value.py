# Search: Check if a specific value exists in a tuple

def get_input(limit, debug=False):
	"""
	Collects elements for a tuple from user input.

	Parameters:
		limit (int): Number of elements in the tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Tuple containing the user-provided elements.
	"""
	elements = []
	print(f"\nEnter {limit} elements for the tuple:")

	for i in range(limit):
		element = input(f"Enter element {i + 1}: ")
		elements.append(element)
		if debug:
			print(f"[DEBUG] Added element: {element}")

	data = tuple(elements)
	if debug:
		print(f"[DEBUG] Final Tuple: {data}")
	return data


def tuple_search(data, element, debug=False):
	"""
	Checks if an element exists in the tuple.

	Parameters:
		data (tuple): Tuple to search within.
		element (str): The element to search for.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		bool: True if the element exists, False otherwise.
	"""
	if debug:
		print(f"[DEBUG] Searching for: {element} in {data}")

	for index, value in enumerate(data):
		if value == element:
			if debug:
				print(f"[DEBUG] Element found at index {index}.")
			return True

	if debug:
		print(f"[DEBUG] Element not found.")
	return False


def main():
	"""
	Main function to check if a value exists in a tuple.
	"""
	try:
		# Input the size of the tuple
		size = int(input("Enter the size of the tuple: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the tuple: "))

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect tuple elements
		items = get_input(size, debug)

		# Input the value to search
		value = input("Enter a value to check its availability in the tuple: ")

		# Search value in the tuple
		result = tuple_search(items, value, debug)

		# Output the result
		if result:
			print(f"\nThe value '{value}' exists in the tuple {items}")
		else:
			print(f"\nThe value '{value}' does not exist in the tuple {items}")

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
