# Concatenate two tuples and print the result

def get_tuple_elements(size, name, debug = False):
	"""
	Collects elements for Tuple from user input

	Parameters:
		size (int): Number of elements in Tuple
		name (str): Name of Tuple for display in Prompts
		debug (bool): Whether to display debug prints (default is False)

	Returns:
		tuple: Tuple containing the user provided elements
	"""
	elements = []

	print(f"\nEnter {size} elements for {name}:")

	for i in range(size):
		element = input(f"Enter element {i + 1}: ")
		elements.append(element)

	if debug:
		print(f"[DEBUG] Elements for {name}: {elements}")

	return tuple(elements)

def concatenate(data_one, data_two, debug = False):
	"""
	Concatenates two Tuples and returns the result

	Parameters:
		data_one (tuple): First Tuple
		data_two (tuple): Second Tuple
		debug (bool): Whether to display debug prints (default is False)

	Returns:
		tuple: Concatenated Tuple
	"""

	result = data_one + data_two

	if debug:
		print(f"[DEBUG] Concatenating {data_one} and {data_two}")
		print(f"[DEBUG] Result: {result}")

	return result

def main():
	"""
	Main function to collect inputs, concatenate tuples, and display the result
	"""
	try:
		# Input the size of the tuple
		first_size = int(input("Enter the size of the First Tuple: "))
		second_size = int(input("Enter the size of the Second Tuple: "))

		while first_size <= 0 or second_size <= 0:
			print("Error: Tuple sizes must be positive integers")
			if first_size <= 0:
				first_size = int(input("Try again. Enter the size of the First Tuple: "))
			if second_size <= 0:
				second_size = int(input("Try again. Enter the size of the Second Tuple: "))

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect Tuple Elements
		first_tuple = get_tuple_elements(first_size, "First Tuple", debug)
		second_tuple = get_tuple_elements(second_size, "Second Tuple", debug)

		# Concatenate Tuples
		result = concatenate(first_tuple, second_tuple, debug)

		# Display the results
		print(f"First Tuple: {first_tuple}")
		print(f"Second Tuple: {second_tuple}")
		print(f"Concatenated Tuple: {result}")

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()