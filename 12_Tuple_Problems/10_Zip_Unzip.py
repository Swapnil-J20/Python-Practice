# Zipping and Unzipping: Zip two tuples into a tuple of pairs, and then unzip it back

def get_input(limit, debug=False):
	"""
	Collects elements for a tuple from user input.

	Parameters:
		limit (int): Number of elements in the tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Tuple containing the user-provided elements.
	"""
	elements = []
	for i in range(limit):
		element = input(f"Enter element {i + 1}: ")
		elements.append(element)
		if debug:
			print(f"[DEBUG] Added element: {element}")

	data = tuple(elements)
	if debug:
		print(f"[DEBUG] Final Tuple: {data}")
	return data

def zip_tuples(data_one, data_two, debug=False):
	"""
	Zips two tuples into a tuple of pairs.

	Parameters:
		data_one (tuple): First tuple of elements.
		data_two (tuple): Second tuple of elements.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Zipped tuple of pairs.
	"""
	min_length = min(len(data_one), len(data_two))
	zipped_list = []

	for i in range(min_length):
		pair = (data_one[i], data_two[i])
		zipped_list.append(pair)
		if debug:
			print(f"[DEBUG] Zipping Pair {i + 1}: {pair}")

	zipped_data = tuple(zipped_list)
	if debug:
		print(f"[DEBUG] Zipped Tuple: {zipped_data}")
	return zipped_data

def unzip_tuples(zipped_data, debug=False):
	"""
	Unzips a tuple of pairs back into two separate tuples.

	Parameters:
		zipped_data (tuple): Zipped tuple of pairs.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Two tuples extracted from the zipped tuple.
	"""
	one = []
	two = []

	for index, (x, y) in enumerate(zipped_data):
		one.append(x)
		two.append(y)
		if debug:
			print(f"[DEBUG] Unzipping Pair {index + 1}: ({x}, {y})")

	unzipped_one = tuple(one)
	unzipped_two = tuple(two)
	if debug:
		print(f"[DEBUG] Unzipped Tuple 1: {unzipped_one}")
		print(f"[DEBUG] Unzipped Tuple 2: {unzipped_two}")
	return unzipped_one, unzipped_two

def main():
	"""
	Main function to demonstrate zipping and unzipping of tuples.
	"""
	try:
		# Input: Sizes of the tuples
		size_one = int(input("Enter the size of the first tuple: "))
		size_two = int(input("Enter the size of the second tuple: "))

		while size_one <= 0 or size_two <= 0:
			print("Error: Enter positive integers for the sizes.")
			if size_one <= 0:
				size_one = int(input("Try again. Enter the size of the first tuple: "))
			if size_two <= 0:
				size_two = int(input("Try again. Enter the size of the second tuple: "))

		# Debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect tuple elements
		items_one = get_input(size_one, debug)
		items_two = get_input(size_two, debug)

		# Zip the tuples
		zipped_result = zip_tuples(items_one, items_two, debug)

		# Unzip the tuples
		unzipped_one, unzipped_two = unzip_tuples(zipped_result, debug)

		# Display results
		print(f"\nOriginal Tuples:\n  Tuple 1: {items_one}\n  Tuple 2: {items_two}")
		print(f"Zipped Tuple: {zipped_result}")
		print(f"Unzipped Tuples:\n  Tuple 1: {unzipped_one}\n  Tuple 2: {unzipped_two}")

	except ValueError:
		print("Error: Please enter valid numbers for the tuple sizes.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
