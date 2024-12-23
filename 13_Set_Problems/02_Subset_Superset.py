# Subset and Superset: Check if one set is a subset or superset of another set

def get_set_elements(size, debug=False):
	"""
	Collects elements for a set from user input.

	Parameters:
		size (int): Number of elements in the set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		set: A set containing unique user-provided elements.
	"""
	elements = set()
	print(f"\nEnter {size} unique elements for the set:")

	for _ in range(size):
		element = input(f"Enter element {_ + 1}: ")
		elements.add(element)
		if debug:
			print(f"[DEBUG] Current Set: {elements}")

	return elements

def set_operations(set_one, set_two, debug=False):
	"""
	Performs subset and superset checks between two sets.

	Parameters:
		set_one (set): First set.
		set_two (set): Second set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Results of subset and superset checks (bool, bool).
	"""
	sub = set_one.issubset(set_two)
	sup = set_one.issuperset(set_two)

	if debug:
		print(f"[DEBUG] {set_one} is a subset of {set_two}: {sub}")
		print(f"[DEBUG] {set_one} is a superset of {set_two}: {sup}")

	return sub, sup

def main():
	"""
	Main function to demonstrate subset and superset checks between two sets.
	"""
	try:
		# Input: Sizes of the sets
		size_one = int(input("Enter the size of the First Set: "))
		size_two = int(input("Enter the size of the Second Set: "))

		while size_one <= 0 or size_two <= 0:
			print("Error: Sizes must be positive integers.")
			if size_one <= 0:
				size_one = int(input("Enter the size of the First Set: "))
			if size_two <= 0:
				size_two = int(input("Enter the size of the Second Set: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect set elements
		set_one = get_set_elements(size_one, debug)
		set_two = get_set_elements(size_two, debug)

		# Perform set operations
		subset_one, superset_one = set_operations(set_one, set_two, debug)
		subset_two, superset_two = set_operations(set_two, set_one, debug)

		# Display results
		print(f"\nFor Sets: {set_one} & {set_two}:")
		print(f"Set One is a subset of Set Two: {subset_one}")
		print(f"Set One is a superset of Set Two: {superset_one}")
		print(f"Set Two is a subset of Set One: {subset_two}")
		print(f"Set Two is a superset of Set One: {superset_two}")

		if subset_one and superset_one:
			print("Set One is equal to Set Two.")

	except ValueError:
		print("Error: Please enter valid integers for the set sizes.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
