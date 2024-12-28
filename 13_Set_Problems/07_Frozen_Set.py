# Frozen Set: Demonstrate the usage of a frozen set by creating one and trying to modify it.

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
		else:
			elements.add(element)
			if debug:
				print(f"[DEBUG] Current Set: {elements}")

	return elements

def demonstrate_frozen_set(original_set, debug=False):
	"""
	Converts a set to a frozen set and demonstrates immutability.

	Parameters:
		original_set (set): The original mutable set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	# Convert to frozen set
	fixed_set = frozenset(original_set)
	print(f"\nFrozen Set: {fixed_set}")

	# Demonstrate immutability
	try:
		if debug:
			print("[DEBUG] Attempting to add an element to the frozen set.")
		fixed_set.add("new_element")  # This should raise an exception
	except AttributeError as e:
		print(f"\nError: Cannot modify Frozen Set - {e}")

def main():
	"""
	Main function to demonstrate the usage of Frozen Set.
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

		# Demonstrate frozen set
		demonstrate_frozen_set(items, debug)

	except ValueError:
		print("Error: Please enter a valid integer for the set size.")

# Entry Point of the Program
if __name__ == "__main__":
	main()
