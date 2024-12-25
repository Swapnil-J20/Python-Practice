# Set Membership: Write a program to check if an element exists in a set.

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
		elements.add(element)
		if debug:
			print(f"[DEBUG] Current Set: {elements}")

	return elements


def set_search(data, value, debug=False):
	"""
	Checks if a value exists in the set.

	Parameters:
		data (set): The set to search.
		value (str): The value to search for.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		bool: True if the value exists in the set, False otherwise.
	"""
	if debug:
		print(f"[DEBUG] Checking if '{value}' is in {data}")
	return value in data


def main():
	"""
	Main function to demonstrate set membership.
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

		# Input: Value to search
		value = input("\nEnter the value you want to search in the Set: ")

		# Perform Search
		result = set_search(items, value, debug)

		# Display Results
		print(f"\nOriginal Set: {items}")
		if result:
			print(f"Value '{value}' is present in the Set.")
		else:
			print(f"Value '{value}' is not in the Set.")

	except ValueError:
		print("Error: Please enter a valid integer for the set size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
