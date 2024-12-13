# Rotation: Rotate the elements of a list to the right by k positions. Example: Input: [1, 2, 3, 4, 5], k = 2 → Output: [4, 5, 1, 2, 3]

def rotation(data, rotate, debug=False):
	"""
	Rotates elements in a list to the right by k positions.

	Parameters:
		data (list): List of elements to be rotated.
		rotate (int): Number of positions to shift.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		result (list): Rotated list.
	"""
	length = len(data)

	# Ensure rotation is within bounds
	rotate = rotate % length

	if debug:
		print(f"Rotating by {rotate} positions.")

	# Rotate the list
	result = [0] * length
	for i, value in enumerate(data):
		new_position = (i + rotate) % length
		result[new_position] = value

		if debug:
			print(f"Element {value} at index {i} moved to index {new_position}.")

	return result


def main():
	"""
	Main function to gather input, rotate list elements, and display the result.
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

		# Input: Rotation count
		rotate = int(input("Enter the number of positions to rotate: "))

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Rotate the list
		output = rotation(items, rotate, debug)

		# Output: Display results
		print(f"\nOriginal List: {items}")
		print(f"Rotated List: {output}")

	except ValueError:
		print("Error: Please enter valid integers for list size and rotation count.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
