# Count and Index: Use the count() and index() methods on a tuple. Example: Count the occurrences of a specific value in a tuple.

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


def count_index(data, value, debug=False):
	"""
	Finds the count and first index of a value in a tuple.

	Parameters:
		data (tuple): Tuple to search.
		value: Value to find in the tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary containing the count and index (if found).
	"""
	count = data.count(value)
	if count == 0:
		if debug:
			print(f"[DEBUG] Value '{value}' not found in the tuple.")
		return {"count": 0, "index": None}

	index = data.index(value)
	if debug:
		print(f"[DEBUG] Value '{value}' found {count} time(s) at index {index}.")

	return {"count": count, "index": index}


def main():
	"""
	Main function to demonstrate the use of count() and index() on a tuple.
	"""
	try:
		# Input: Size of the tuple
		size = int(input("Enter the size of the tuple: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the tuple: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect tuple elements
		items = get_input(size, debug)

		# Input: Value to count and find index
		value = input("\nEnter a value to find its count and index: ")

		# Process: Count and index
		result = count_index(items, value, debug)

		# Output the results
		print(f"\nOriginal Tuple: {items}")
		if result["count"] == 0:
			print(f"The value '{value}' is not found in the tuple.")
		else:
			print(f"The value '{value}' appears {result['count']} time(s) and first occurs at index {result['index']}.")

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
