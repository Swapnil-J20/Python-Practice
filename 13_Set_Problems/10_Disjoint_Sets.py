# Disjoint Sets: Check if two sets are disjoint.

def get_set_elements(limit, debug=False):
	"""
	Collects elements for a set from user input.

	Parameters:
		limit (int): Number of elements in the set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		set: Set containing unique user-provided elements.
	"""
	elements = set()
	print(f"Enter {limit} unique elements for the set:")

	while len(elements) < limit:
		element = input(f"Enter element {len(elements) + 1}: ")
		if element in elements:
			print(f"[INFO] Element '{element}' is already in the set and will not be added.")
		else:
			elements.add(element)
		if debug:
			print(f"[DEBUG] Current Set: {elements}")

	return elements

def check_disjoint(set_one, set_two, debug=False):
	"""
	Checks if two sets are disjoint or not.

	Parameters:
		set_one (set): First set.
		set_two (set): Second set.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		bool: True if the sets are disjoint, otherwise False.
	"""
	output = set_one.isdisjoint(set_two)
	if debug and not output:
		intersection = set_one & set_two
		print(f"[DEBUG] Intersection of Sets: {intersection}")
	return output

def main():
	"""
	Main function to gather input, demonstrate disjoint checks, and display results.
	"""
	try:
		# Input: Sizes of the sets
		size_one = int(input("Enter the size of the first set: "))
		size_two = int(input("Enter the size of the second set: "))

		while size_one <= 0 or size_two <= 0:
			print("Error: Sizes must be positive integers.")
			if size_one <= 0:
				size_one = int(input("Enter the size of the first set: "))
			if size_two <= 0:
				size_two = int(input("Enter the size of the second set: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect set elements
		set_one = get_set_elements(size_one, debug)
		set_two = get_set_elements(size_two, debug)

		# Display warnings for ignored duplicates
		if len(set_one) < size_one:
			print(f"Warning: Only {len(set_one)} unique elements were added to Set One.")
		if len(set_two) < size_two:
			print(f"Warning: Only {len(set_two)} unique elements were added to Set Two.")

		# Perform set operations
		result = check_disjoint(set_one, set_two, debug)

		# Display results
		print(f"\nSet One: {set_one}")
		print(f"Set Two: {set_two}")
		
		if result:
			print("\nSets are Disjoint")
		else:
			print("\nSets are not Disjoint")

	except ValueError:
		print("Error: Please enter valid integers for set sizes.")


# Entry Point of the Program
if __name__ == "__main__":
	main()

