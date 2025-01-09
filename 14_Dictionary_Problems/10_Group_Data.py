# Group Data: Group elements of a list into a dictionary based on a condition.
# Input: [1, 2, 3, 4, 5, 6] → Output: { "Even": [2, 4, 6], "Odd": [1, 3, 5] }

def get_list_elements(limit, debug=False):
	"""
	Gathers input to create a list.

	Parameters:
		limit (int): Size of the list.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: List of integers provided by the user.
	"""
	elements = []
	print(f"\nEnter {limit} numbers to divide them into Even-Odd.")

	for index in range(limit):
		while True:
			try:
				element = int(input(f"Enter Element {index + 1}: "))
				elements.append(element)
				if debug:
					print(f"Step {index + 1}: Added {element}. Current List: {elements}")
				break
			except ValueError:
				print("Error: Enter a valid number.")

	return elements


def even_odd_check(data, debug=False):
	"""
	Groups elements of a list into a dictionary based on whether they are even or odd.

	Parameters:
		data (list): List of integers to be grouped.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: Dictionary with two keys, "Even" and "Odd", containing respective numbers.
	"""
	output = {"Even": [], "Odd": []}

	for index, number in enumerate(data):
		if number % 2 == 0:
			output["Even"].append(number)
			if debug:
				print(f"Step {index + 1}: Number {number} is Even. Current Even Numbers: {output['Even']}")
		else:
			output["Odd"].append(number)
			if debug:
				print(f"Step {index + 1}: Number {number} is Odd. Current Odd Numbers: {output['Odd']}")

	return output


def main():
	"""
	Main function to gather input, group numbers into even/odd, and display the result.
	"""
	try:
		size = int(input("Enter the size of the list: "))

		while size <= 0:
			print("Error: Enter a positive integer for the size.")
			size = int(input("Try again. Enter the size of the list: "))

		debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

		items = get_list_elements(size, debug)
		result = even_odd_check(items, debug)

		print(f"\nOriginal List of Numbers: {items}")
		print(f"Dictionary of Even and Odd Numbers: {result}")

	except ValueError:
		print("Error: Please enter a valid positive integer for the size of the list.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
