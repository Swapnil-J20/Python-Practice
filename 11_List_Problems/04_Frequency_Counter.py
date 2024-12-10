# Count the frequency of each element in a list

def frequency_counter(data, debug=False):
	"""
	Returns count of elements in the list.

	Parameters:
		data (list): A list with elements to be counted.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		counter (dict): A dictionary with element counts.
	"""
	counter = {}

	for index, value in enumerate(data):
		if value in counter:
			counter[value] = counter[value] + 1
		else:
			counter[value] = 1

		if debug:
			print(f"Step {index + 1}: Element: {value}, Current stats: {counter}")

	return counter


def main():
	"""
	Main function to gather input, count the frequency, and display the count result.
	"""
	try:
		# Input: List size
		size = int(input("Enter the size of the list: "))
		while size <= 0:
			print("Error: Enter a positive integer for list size.")
			size = int(input("Try again: "))

		# Input: List elements
		items = []
		print(f"\nEnter {size} elements: ")
		while len(items) < size:
			element = input(f"Enter element {len(items) + 1}: ")
			items.append(element)

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Process: Calculate frequencies
		result = frequency_counter(items, debug)

		# Output: Display results
		print(f"\nFrequency Count for List {items}:")
		for key, count in result.items():
			print(f"Element: {key}, Count: {count}")

	except ValueError:
		print("Error: Please enter a valid integer for list size.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
