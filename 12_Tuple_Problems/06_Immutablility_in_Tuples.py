# Immutable Changes: Demonstrate how to modify a tuple by creating a new one (since tuples are immutable)

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
	for i in range(limit):
		element = input(f"Enter element {i + 1}: ")
		elements.append(element)
		if debug:
			print(f"[DEBUG] Added element: {element}")

	data = tuple(elements)
	if debug:
		print(f"[DEBUG] Final Tuple: {data}")
	return data


def modify_tuple(tuple_data, debug=False):
	"""
	Demonstrates immutability by creating a new tuple after modification.

	Parameters:
		tuple_data (tuple): The tuple to be modified.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: The modified tuple.
	"""
	print("\nChoose the operation to perform on the tuple:")
	print("1. Add an element")
	print("2. Modify an existing element")

	while True:
		task = input("Enter 1 to add or 2 to modify: ").strip()
		if task in {"1", "2"}:
			break
		print("Invalid choice. Please enter 1 or 2.")

	if task == "1":  # Add an element
		element = input("Enter the element to add: ")

		if debug:
			print(f"[DEBUG] Adding element '{element}' to the tuple.")

		# Convert to list and add the element
		list_data = list(tuple_data)
		list_data.append(element)
		final_data = tuple(list_data)

		if debug:
			print(f"[DEBUG] New List: {list_data}")
			print(f"[DEBUG] Converted back to Tuple: {final_data}")

	elif task == "2":  # Modify an element
		while True:
			try:
				position = int(input("Enter the index of the element to modify: "))
				if 0 <= position < len(tuple_data):
					break
				print(f"Error: Index out of range. Valid indices are 0 to {len(tuple_data) - 1}.")
			except ValueError:
				print("Error: Please enter a valid integer.")

		new_value = input(f"Enter the new value for index {position}: ")

		if debug:
			print(f"[DEBUG] Modifying index {position} with value '{new_value}'.")

		# Convert to list and modify the element
		list_data = list(tuple_data)
		list_data[position] = new_value
		final_data = tuple(list_data)

		if debug:
			print(f"[DEBUG] New List: {list_data}")
			print(f"[DEBUG] Converted back to Tuple: {final_data}")

	return final_data


def main():
	"""
	Main function to demonstrate tuple immutability and modification.
	"""
	try:
		size = int(input("Enter the size of the tuple: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the tuple: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect tuple elements
		items = get_input(size, debug)

		# Modify the tuple
		new_tuple = modify_tuple(items, debug)

		# Display the results
		print("\nOriginal Tuple:", items)
		print("Modified Tuple:", new_tuple)

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
