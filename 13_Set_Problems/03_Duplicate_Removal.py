# Duplicate Removal: Remove duplicates from a list by converting it into a set

def get_list_elements(size, debug=False):
	"""
	Collects elements for a list from user input.

	Parameters:
		size (int): Number of elements in the list.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A list containing unique user-provided elements.
	"""
	elements = list()
	print(f"\nEnter {size} elements for the List:")

	for _ in range(size):
		element = input(f"Enter element { _ + 1}: ")
		elements.append(element)
		if debug:
			print(f"[DEBUG] Current List: {elements}")

	return elements


def main():
	"""
	Main function to demonstrate Duplicate removal property of Sets
	"""
	try:
		# Input: Sizes of the List
		size = int(input("Enter the size of the List: "))
		
		while size <= 0:
			print("Error: Sizes must be positive integers.")
			size = int(input("Enter the size of the List: "))
			
		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect List elements
		items = get_list_elements(size, debug)

		set_data = set(items)

		# Display results
		print(f"\nOriginal List: {items}")
		print(f"Duplicates get removed in Set: {set_data}")

	except ValueError:
		print("Error: Please enter valid integers for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
