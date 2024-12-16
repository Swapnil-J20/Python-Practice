# Packing and Unpacking: Create a tuple with mixed data types and demonstrate tuple packing and unpacking.

def get_input(data_type, debug=False):
	"""
	Collects and validates input based on the specified data type.

	Parameters:
		data_type (str): The type of data to collect (e.g., 'Integer', 'Float', etc.).
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		value: The collected and validated value of the specified data type.
	"""
	while True:
		try:
			if data_type == "Integer":
				value = int(input(f"Enter an {data_type}: "))
			elif data_type == "Float":
				value = float(input(f"Enter a {data_type}: "))
			elif data_type == "String":
				value = input(f"Enter a {data_type}: ")
			elif data_type == "Bool":
				val = input(f"Enter a {data_type} (True/False): ").strip().lower()
				if val in ["true", "t", "1"]:
					value = True
				elif val in ["false", "f", "0"]:
					value = False
				else:
					raise ValueError("Invalid Boolean Value")
			else:
				raise ValueError("Unsupported Data Type")
			
			if debug:
				print(f"Collected {data_type}: {value}")
			return value

		except ValueError as e:
			print(f"Error: {e}. Please try again.")


def packing_unpacking(data_types, debug=False):
	"""
	Demonstrates packing and unpacking of a tuple with mixed data types.

	Parameters:
		data_types (list): A list of data types to include in the tuple.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		result (tuple): The packed tuple of mixed data types.
	"""
	values = []

	# Collect input for each data type
	for data_type in data_types:
		value = get_input(data_type, debug)
		values.append(value)

	# Packing the tuple
	result = tuple(values)
	if debug:
		print(f"Packed Tuple: {result}")

	return result


def main():
	"""
	Main function to demonstrate tuple packing and unpacking.
	"""
	print("Creating a Tuple with mixed data types:")

	# Define the types for the tuple
	data_types = ["Integer", "Float", "String", "Bool"]

	# Enable debug mode
	debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

	# Perform packing
	packed_tuple = packing_unpacking(data_types, debug)

	# Output packed tuple
	print(f"\nPacked Tuple: {packed_tuple}")

	# Perform unpacking
	print("\nUnpacking Tuple:")
	for index, value in enumerate(packed_tuple):
		print(f"Element {index + 1}: {value} ({type(value).__name__})")


# Entry Point of the Program
if __name__ == "__main__":
	main()
