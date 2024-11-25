# Write a program to remove duplicates from a list using a loop

def duplicate_removal(data):
	"""
    Removes duplicates from a list using a loop.

    Parameters:
        data (list): The input list containing potential duplicates.

    Returns:
        list: A new list with duplicates removed.
    """

	unique_items = []  # List to store unique elements

	for item in data:
		if item not in unique_items:
			unique_items.append(item)

	return unique_items

def main():

	try: 
		# Input length of the list
		length = int(input("What should be the length of the list? : "))

		if length <= 0:
			print("Enter a positive integer for length.")
			return

		# Input list items
		items = []
		i = 0

		print("Add items to the list: ")

		while i < length:
			item = input()
			items.append(item)
			i = i + 1 

		# Remove duplicates
		output = duplicate_removal(items)

		# Print the result
		print(f"Original list: {items}")
		print(f"List after removing duplicates: {output}")

	except ValueError:
		print("Enter a positive integer for length")

# Entry Point of the program
if __name__ == "__main__":
    main()