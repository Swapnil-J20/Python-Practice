# Even Numbers: Create a list of numbers and extract only the even numbers into a new list.

def even_num(data, debug=False):
	"""
	Extracts even numbers from the provided list.

	Parameters:
		data (list): A list of numbers to check for evenness.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		output (list): A list of even numbers.
	"""
	output = []
	for index, i in enumerate(data):
		if i % 2 == 0:
			output.append(int(i))
			if debug:
				print(f"Step {index + 1}: {i} is divisible by 2, adding to even numbers list {output}")
	return output


def main():
	"""
	Main function to gather input, find even numbers, and display the result.
	"""
	try:
		# Input: List size
		size = int(input("Enter the size of the list: "))
		while size <= 0:
			print("Enter a positive integer for the list size.")
			size = int(input("Try again: "))

		# Input: List elements
		items = []
		print(f"Enter {size} numbers:")
		while len(items) < size:
			num = input(f"Enter number {len(items) + 1}: ")
			try:
				num = int(num)  # Accepts integers
				items.append(num)
			except ValueError:
				print("Invalid input! Please enter an Integer.")

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Find even numbers
		result = even_num(items, debug)

		# Output
		print(f"\nOriginal list: {items}")
		print(f"Even numbers: {result}")

	except ValueError:
		print("Error: Please enter a valid number for the list size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
