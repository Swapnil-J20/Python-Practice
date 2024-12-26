# Set Iteration: Iterate through a set and print its elements.

def get_set_elements(size, debug=False):
	"""
	Collects elements for a Set from user input.

	Parameters:
		size (int): Number of elements in the Set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		Set: A Set containing unique user-provided elements.
	"""
	elements = set()
	print(f"\nEnter {size} unique elements for the Set:")

	for _ in range(size):
		element = input(f"Enter element {_ + 1}: ")
		if element in elements:
			print(f"[INFO] Element '{element}' is a duplicate and will not be added.")
		elements.add(element)
		if debug:
			print(f"[DEBUG] Current Set: {elements}")

	return elements


def main():
	"""
	Main function to demonstrate set iteration.
	"""
	try:
		# Input: Size of the Set
		size = int(input("Enter the size of the Set: "))
		
		while size <= 0:
			print("Error: Size must be a positive integer.")
			size = int(input("Try again. Enter the size of the Set: "))
			
		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect Set elements
		items = get_set_elements(size, debug)

		# Iterating through Set
		print("\nSet Elements with Iteration: ")
		for i in items:
			print(i)
			if debug:
				print(f"[DEBUG] Iterating element: {i}")

		# # Reverse Iteration
		# print("\nSet Elements in Reverse Order (via List Conversion):")
		# reversed_items = list(items)[::-1]
		# for elem in reversed_items:
		# 	print(elem)

		# Total Element Count
		print(f"\nTotal number of elements: {len(items)}")

	except ValueError:
		print("Error: Please enter a valid integer for the set size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
