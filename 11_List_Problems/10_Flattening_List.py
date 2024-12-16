# Flattening a List: Write a program to flatten a nested list. Example: Input: [1, [2, 3], [4, [5, 6]]] → Output: [1, 2, 3, 4, 5, 6]

def flattening_list(data, debug=False):
	"""
	Flattens a nested list into a single-level list.

	Parameters:
		data (list): The nested list to flatten.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: Flattened list.
	"""
	result = []

	for index, item in enumerate(data):
		if isinstance(item, list):  # Check if the item is a nested list
			if debug:
				print(f"Flattening nested list at index {index}: {item}")
			# Recursively flatten the nested list
			result.extend(flattening_list(item, debug))
		else:
			if debug:
				print(f"Adding element at index {index}: {item}")
			result.append(item)

	return result


def main():
	"""
	Main function to gather inputs, flatten a nested list, and display the result.
	"""
	try:
		# Input the nested list
		items = eval(input("Enter a nested list (e.g., [1, [2, 3], [4, [5, 6]]]): "))

		if not isinstance(items, list):
			print("Error: Input must be a list.")
			return

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Flatten the nested list
		output = flattening_list(items, debug)

		# Display results
		print(f"\nNested List: {items}")
		print(f"Flattened List: {output}")

	except (SyntaxError, ValueError):
		print("Error: Invalid input. Please enter a valid nested list.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
