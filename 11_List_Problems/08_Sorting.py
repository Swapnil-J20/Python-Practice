# Sorting: Write your own function to sort a list of integers in ascending order without using the sort() method

def sorting(data, debug = False):
	"""
	Sorts the elements in a list and returns new sorted list.

	Parameters:
		data (list): List of elements to be sorted.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		result (list): Sorted list.
	"""
	
	length = len(data)

	for i in range(length):
		if debug:
			print(f"Pass {i + 1}: Starting with list: {data}")

		# Compare adjacent elements and swap if necessary
		for j in range(length - i - 1):
			if data[j] > data[j + 1]:
				# Swap elements
				data[j], data[j + 1] = data[j + 1], data[j]

				if debug:
					print(f"Swapped {data[j + 1]} and {data[j]}: {data}")

		if debug:
			print(f"Pass {i + 1}: Resulting list: {data}")

	return data


def main():
	"""
	Main function to gather input, sort list elements, and display the result.
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
			item = int(input(f"Enter element {i + 1}: "))
			items.append(item)

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Rotate the list
		output = sorting(items, debug)

		# Output: Display results
		print(f"\nOriginal List: {items}")
		print(f"Sorted List: {output}")

	except ValueError:
		print("Error: Please enter valid integers for list size")


if __name__ == "__main__":
	main()