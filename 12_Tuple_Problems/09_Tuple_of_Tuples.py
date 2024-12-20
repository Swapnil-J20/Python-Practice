# Tuple of Tuples: Create a tuple of tuples and calculate the sum of each inner tuple.

def get_inner_tuple(size, debug=False):
	"""
	Collects elements for an inner tuple from user input.

	Parameters:
		size (int): Number of elements in the inner tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Tuple containing the user-provided elements for one inner tuple.
	"""
	elements = []
	for i in range(size):
		while True:
			try:
				element = int(input(f"Enter element {i + 1}: "))
				elements.append(element)
				if debug:
					print(f"[DEBUG] Added element: {element}")
				break
			except ValueError:
				print("Error: Please enter a valid integer.")

	inner_tuple = tuple(elements)
	if debug:
		print(f"[DEBUG] Final Inner Tuple: {inner_tuple}")
	return inner_tuple


def get_tuple_of_tuples(rows, cols, debug=False):
	"""
	Collects a tuple of tuples based on user input.

	Parameters:
		rows (int): Number of inner tuples.
		cols (int): Number of elements in each inner tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Tuple of tuples provided by the user.
	"""
	tuple_of_tuples = []
	for row in range(rows):
		print(f"\nEntering elements for tuple {row + 1}:")
		inner_tuple = get_inner_tuple(cols, debug)
		tuple_of_tuples.append(inner_tuple)

	result = tuple(tuple_of_tuples)
	if debug:
		print(f"[DEBUG] Final Tuple of Tuples: {result}")
	return result


def calculate_sums(tuple_of_tuples, debug=False):
	"""
	Calculates the sum of each inner tuple in the tuple of tuples.

	Parameters:
		tuple_of_tuples (tuple): Tuple of tuples to process.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: List of sums for each inner tuple.
	"""
	sums = []
	for index, inner_tuple in enumerate(tuple_of_tuples):
		tuple_sum = sum(inner_tuple)
		sums.append(tuple_sum)
		if debug:
			print(f"[DEBUG] Tuple {index + 1}: {inner_tuple}, Sum: {tuple_sum}")

	return sums


def main():
	"""
	Main function to create a tuple of tuples and calculate the sum of each inner tuple.
	"""
	try:
		# Input: Number of inner tuples and their sizes
		rows = int(input("Enter the number of tuples (rows): "))
		cols = int(input("Enter the size of each tuple (columns): "))

		if rows <= 0 or cols <= 0:
			print("Error: Both rows and columns must be positive integers.")
			return

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect tuple of tuples
		tuple_of_tuples = get_tuple_of_tuples(rows, cols, debug)

		# Calculate sums
		sums = calculate_sums(tuple_of_tuples, debug)

		# Display results
		print(f"\nTuple of Tuples: {tuple_of_tuples}")
		print(f"Sums of Each Tuple: {sums}")

	except ValueError:
		print("Error: Please enter valid integers for rows and columns.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
