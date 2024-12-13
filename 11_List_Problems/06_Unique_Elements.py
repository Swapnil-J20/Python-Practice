# Unique Elements: Remove duplicate elements from a list without using set()

def unique_elements(data, debug=False):
	"""
	Removes duplicate elements from a list and returns a list with unique elements.

	Parameters:
		data (list): List of elements to be checked.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		result (list): Unique list with no duplicates.
	"""
	unique = []

	for i in data:
		if i not in unique:
			unique.append(i)
		if debug:
			print(f"Checking for element: {i}, Current Unique List: {unique}")

	return unique


def main():
	"""
	Main function to gather input, find unique elements, and display the result.
	"""
	try:
		# Input: Size of the list
		size = int(input("Enter the size of the list: "))

		while size <= 0:
			print("Error: Enter a Positive Integer.")
			size = int(input("Try again. Enter the size of the list: "))

		# Input: List elements
		items = []
		print("\nEnter elements for the list:")

		for i in range(size):
			item = input(f"Enter element {i + 1}: ")
			items.append(item)

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Find unique elements
		output = unique_elements(items, debug)

		# Output: Display results
		print(f"\nOriginal List: {items}")
		print(f"Unique List: {output}")

	except ValueError:
		print("Error: Please enter a valid number for the list size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
