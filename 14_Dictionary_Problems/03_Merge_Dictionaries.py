# Merge Dictionaries: Merge two dictionaries into one

def get_dict_elements(limit, debug=False):
	"""
	Collects key-value pairs for a dictionary from user input.

	Parameters:
		limit (int): Number of elements in the dictionary.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary containing the user-provided key-value pairs.
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


def dict_merge(data_one, data_two, debug=False):
	"""
	Merges two dictionaries into one.

	Parameters:
		data_one (dict): First dictionary to be merged.
		data_two (dict): Second dictionary to merge into the first.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: A new dictionary containing merged key-value pairs.
	"""
	merged_dict = data_one.copy()  # Preserve original data_one
	for key in data_two:
		merged_dict[key] = data_two[key]
		if debug:
			print(f"[DEBUG] Adding/Updating Key '{key}' with Value '{data_two[key]}': {merged_dict}")

	return merged_dict


def main():
	"""
	Main function to gather input, merge two dictionaries, and display the result.
	"""
	try:
		# Input: Sizes of the dictionaries
		size_one = int(input("Enter size of the First Dictionary: "))
		size_two = int(input("Enter size of the Second Dictionary: "))

		while size_one <= 0 or size_two <= 0:
			if size_one <= 0:
				print("Error: Enter a Positive Integer for Size.")
				size_one = int(input("Enter size of the First Dictionary: "))
			if size_two <= 0:
				print("Error: Enter a Positive Integer for Size.")
				size_two = int(input("Enter size of the Second Dictionary: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect dictionaries
		items_one = get_dict_elements(size_one, debug)
		items_two = get_dict_elements(size_two, debug)

		print(f"\nFirst Dictionary: {items_one}")
		print(f"Second Dictionary: {items_two}")

		# Merge dictionaries
		combined_dict = dict_merge(items_one, items_two, debug)

		# Display the result
		print(f"\nFirst Dictionary: {items_one}")
		print(f"\nSecond Dictionary: {items_two}")
		print(f"\nMerged Dictionary: {combined_dict}")

	except ValueError:
		print("Error: Enter a valid positive integer for the size of the dictionaries.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
