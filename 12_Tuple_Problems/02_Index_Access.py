# Access by Index: Access and print specific elements from a tuple using indexing.

def access_by_index(data, debug=False):
	"""
	Allows users to access specific elements of a tuple by their indices.

	Parameters:
		data (tuple): The tuple to access elements from.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	print("\nEnter the indices of the elements you want to access (Enter -1 to stop):")

	while True:
		try:
			index = int(input("Enter an index: "))

			# Stop the loop if user enters -1
			if index == -1:
				print("Exiting index access.")
				break

			# Validate index range
			if 0 <= index < len(data):
				value = data[index]
				print(f"Element at index {index}: {value}")
				if debug:
					print(f"[DEBUG] Accessed Element: Index {index}, Value: {value}")
			else:
				print(f"Error: Index {index} is out of range. Please try again.")

		except ValueError:
			print("Invalid input. Please enter a valid integer index.")


def main():
	"""
	Main function to demonstrate tuple indexing.
	"""
	try:
		# Input the size of the tuple
		size = int(input("Enter the size of the tuple: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the tuple: "))

		# Input elements for the tuple
		items = []
		print("\nEnter elements for the tuple:")

		for i in range(size):
			item = input(f"Enter element {i + 1}: ")
			items.append(item)

		# Convert the list to a tuple
		data = tuple(items)

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Access elements by index
		access_by_index(data, debug)

	except ValueError:
		print("Error: Please enter a valid number for the size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
