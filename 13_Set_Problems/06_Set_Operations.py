"""
	Set Operations: Given two sets, write a program to:
	- Find their symmetric difference.
	- Remove all elements from the first set that are not present in the second set
"""

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
	Performs Set Operations: Symmetric Difference and Difference Update

	Parameters:
		set_one (set): First set
		set_two (set): Second set
		debug (bool): Whether to display debug prints (default is False). 

	Returns:
		diff (set): Symmetric Difference between two sets
		updated_set_one (set): Updated first set after difference update
	"""

	# Symmetric Difference
	diff = set_one.symmetric_difference(set_two)
	if debug:
		print(f"[DEBUG] Symmetric Difference: {diff}")

	# Difference Update
	set_one.difference_update(set_two)
	if debug:
		print(f"[DEBUG] First Set after Difference Update: {set_one}")

	return diff, set_one


def main():
	"""
	Main function to gather Set data and demonstrate Set Operations
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

		print(f"\nOriginal Sets:")
		print(f"Set One: {set_one} & Set Two: {set_two}")

		# Perform operations
		set_diff, updated_set_one = set_operations(set_one, set_two, debug)
		
		# Display results
		print(f"\nSymmetric Difference between Sets: {set_diff}")
		print(f"\nSet One after Difference Update: {updated_set_one}")

	except ValueError:
		print("Error: Please enter valid integers for the set sizes.")


# Entry Point of the Program
if __name__ == "__main__":
	main()

