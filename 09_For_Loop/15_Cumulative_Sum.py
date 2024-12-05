# Write a program to calculate the cumulative sum of a list. Example: Input: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

def cumulative_sum(data, debug=False):
	"""
	Calculates the cumulative sum of a list using a loop.

	Parameters:
		data (list): The input list of numbers.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A new list containing the cumulative sum of the input list.
	"""
	total = []  # List to store the cumulative sums
	running_sum = 0  # Variable to keep track of the running total

	for i, value in enumerate(data):
		running_sum = running_sum + value  # Add the current value to the running total
		total.append(running_sum)  # Append the running total to the cumulative list
		if debug:
			print(f"Step {i + 1}: Added {value}, Running Sum: {running_sum}, Total List: {total}")

	return total


def main():
	"""
	Main function to handle user input and calculate cumulative sum of a list.
	"""
	try:
		# Input the size of the list
		size = int(input("Enter the number of elements in the list (+ve INT): "))

		if size <= 0:
			print("Please enter a positive integer for the number of elements.")
			return

		print(f"Enter {size} elements for the list:")

		items = []
		for _ in range(size):
			item = int(input())
			items.append(item)

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Calculate the cumulative sum
		result = cumulative_sum(items, debug)

		# Print the result
		print(f"Original list: {items}")
		print(f"Cumulative Sum of values: {result}")

	except ValueError:
		print("Input Error: Please enter a valid positive integer for the list size.")


# Entry Point of the program
if __name__ == "__main__":
	main()
