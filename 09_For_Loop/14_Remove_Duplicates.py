# Write a program to remove duplicates from a list using a loop. Example: Input: [1, 2, 2, 3, 4, 4, 5] → Output: [1, 2, 3, 4, 5]

def remove_dups(data, debug=False):
	"""
	Removes duplicates from a list using a loop.

	Parameters:
		data (list): The input list containing potential duplicates.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A new list with duplicates removed.
	"""
	unique_items = []

	for i, item in enumerate(data):
		if item not in unique_items:
			unique_items.append(item)
			if debug:
				print(f"Step {i + 1}: Added {item} to unique list: {unique_items}")
		else:
			if debug:
				print(f"Step {i + 1}: {item} is a duplicate. Skipping...")

	return unique_items


def main():
	"""
	Main function to handle user input and remove duplicates from the list.
	"""
	try:
		# Input the size of the list
		size = int(input("Enter the number of elements in the list (+ve INT): "))

		if size <= 0:
			print("Please enter a positive integer for the number of elements.")
			return

		print(f"Enter {size} elements for the list:")

		items = []
		for _ in range(size):
			item = input()
			items.append(item)

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Remove duplicates
		result = remove_dups(items, debug)

		# Print the result
		print(f"Original list: {items}")
		print(f"List without duplicates: {result}")

	except ValueError:
		print("Input Error: Please enter a valid positive integer for the list size.")


# Entry Point of the program
if __name__ == "__main__":
	main()
