# Zipping: Merge two lists element-wise into a list of tuples. Example: Input: [1, 2, 3], ['a', 'b', 'c'] → Output: [(1, 'a'), (2, 'b'), (3, 'c')]

def get_list_elements(size, list_name):
	"""
	Gathers elements for a list from user input.

	Parameters:
		size (int): Number of elements in the list.
		list_name (str): The name of the list (used for prompts).

	Returns:
		list: List of user-provided elements.
	"""
	print(f"\nEnter {size} elements for {list_name}:")
	return [input(f"Enter element {i + 1}: ") for i in range(size)]


def zipping(data_first, data_second, debug=False):
	"""
	Merges two lists and returns a new list of tuples.

	Parameters:
		data_first (list): First list of elements.
		data_second (list): Second list of elements.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		zipped (list): Zipped list of tuples.
	"""
	# Take the minimum length to handle unequal list sizes
	min_length = min(len(data_first), len(data_second))
	zipped = []

	for i in range(min_length):
		tuple_pair = (data_first[i], data_second[i])
		zipped.append(tuple_pair)

		if debug:
			print(f"Step {i + 1}: Adding {tuple_pair}, Zipped so far: {zipped}")

	return zipped


def main():
	"""
	Main function to gather inputs, zip list elements, and display the result.
	"""
	try:
		# Input: Sizes of the two lists
		size_one = int(input("Enter the size of the first list: "))
		size_second = int(input("Enter the size of the second list: "))

		while size_one <= 0 or size_second <= 0:
			print("Error: Sizes must be positive integers.")
			if size_one <= 0:
				size_one = int(input("Enter the size of the first list again: "))
			if size_second <= 0:
				size_second = int(input("Enter the size of the second list again: "))

		# Gather list elements using the helper function
		items_one = get_list_elements(size_one, "first list")
		items_second = get_list_elements(size_second, "second list")

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Zip the lists
		output = zipping(items_one, items_second, debug)

		# Output: Display results
		print(f"\nFirst List: {items_one}")
		print(f"Second List: {items_second}")
		print(f"Zipped List: {output}")

	except ValueError:
		print("Error: Please enter valid integers for list sizes.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
