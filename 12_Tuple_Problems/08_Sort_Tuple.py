# Sorting: Write a program to sort a tuple of numbers in ascending order

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
		while True:
			try:
				element = int(input(f"Enter element {i + 1}: "))
				elements.append(element)
				if debug:
					print(f"[DEBUG] Added element: {element}")
				break
			except ValueError:
				print("Error: Please enter a valid integer.")

	data = tuple(elements)
	if debug:
		print(f"[DEBUG] Final Tuple: {data}")
	return data


def sort_tuple(data, debug=False):
	"""
	Sorts a tuple in ascending order using Bubble Sort.

	Parameters:
		data (tuple): Tuple to be sorted.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Sorted tuple in ascending order.
	"""
	length = len(data)
	list_data = list(data)

	for i in range(length):
		if debug:
			print(f"Pass {i + 1}: Starting with list: {list_data}")

		# Compare adjacent elements and swap if necessary
		for j in range(length - i - 1):
			if list_data[j] > list_data[j + 1]:
				# Swap elements
				list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
				if debug:
					print(f"Swapped {list_data[j + 1]} and {list_data[j]}: {list_data}")

		if debug:
			print(f"Pass {i + 1}: Resulting list: {list_data}")

	final_data = tuple(list_data)
	return final_data


def main():
	"""
	Main function to sort a tuple of numbers in ascending order.
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

		# Sort the tuple
		result = sort_tuple(items, debug)

		# Display results
		print(f"\nOriginal Tuple: {items}")
		print(f"Sorted Tuple: {result}")

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
