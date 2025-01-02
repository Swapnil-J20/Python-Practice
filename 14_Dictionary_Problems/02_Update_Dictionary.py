# Update Dictionary: Add a new key-value pair to a dictionary and modify an existing key's value

def get_dict_elements(limit, debug=False):
	"""
	Collects elements for a Dictionary from user input.
	
	Parameters:
		limit (int): Size of the Dictionary.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary with Keys and Values.
	"""
	elements = {}

	print("\nProvide key-value pairs for the dictionary:")
	for i in range(limit):
		element_key = input(f"Enter Key {i + 1}: ")
		element_value = input(f"Enter Value {i + 1}: ")
		elements[element_key] = element_value

		if debug:
			print(f"[DEBUG] Current Dictionary: {elements}")

	return elements


def dict_update(data, debug=False):
	"""
	Updates a dictionary by adding a new key-value pair and modifying an existing key.

	Parameters:
		data (dict): Dictionary to update.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Updated dictionary.
	"""
	# Create a copy of the dictionary to avoid modifying the original
	updated_data = data.copy()

	# Add a new key-value pair
	new_key = input("Enter a new key to add: ")
	new_value = input("Enter the value for the new key: ")
	updated_data[new_key] = new_value

	if debug:
		print(f"[DEBUG] Added New Key-Value Pair: {new_key}: {new_value}")
		print(f"[DEBUG] Dictionary after addition: {updated_data}")

	# Modify an existing key
	existing_key = input("Enter an existing key to modify: ")
	while existing_key not in updated_data:
		print(f"Error: '{existing_key}' does not exist in the dictionary.")
		existing_key = input("Enter an existing key to modify: ")

	update_value = input(f"Enter the new value for Key '{existing_key}': ")
	updated_data[existing_key] = update_value

	if debug:
		print(f"[DEBUG] Updated Key '{existing_key}' with New Value: {update_value}")
		print(f"[DEBUG] Dictionary after modification: {updated_data}")

	return updated_data


def main():
	"""
	Main function to gather input, create a dictionary, and update its elements.
	"""
	try:
		# Input: Size of the dictionary
		size = int(input("Enter the size of the dictionary: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the dictionary: "))

		# Enable Debug Mode
		debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect dictionary elements
		items = get_dict_elements(size, debug)

		print(f"\nCurrent Dictionary: {items}")

		# Update dictionary
		updated_items = dict_update(items, debug)

		# Display results
		print(f"\nOriginal Dictionary: {items}")
		print(f"Updated Dictionary: {updated_items}")

	except ValueError:
		print("Error: Please enter a valid positive integer for the size of the dictionary.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
