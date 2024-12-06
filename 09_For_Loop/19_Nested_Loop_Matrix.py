# Write a program to calculate the sum of all elements in a 2D list using nested loops. Example: Input: [[1, 2], [3, 4]] → Output: 10

def sum_2d_list(data, debug = False):
	"""
	Calculates the sum of all elements in a 2D list using nested loops.

	Parameters:
		data (list): A 2D list of integers
		debug (bool): Whether to display debug prints (default is False)

	Returns:
	int: Sum of all elements in 2D list
	"""
	total = 0
	row_index = 0

	for row in data:
		col_index = 0
		for element in row:
			total = total + element
			if debug:
				print(f"Processing element at row {row_index}, Column {col_index}: {element}")
				print(f"Current total: {total}")
			col_index = col_index + 1
		row_index = row_index + 1

	return total

def main():
	"""
	Main function to handle user input and check if a number is an Armstrong number.
	"""
	try:
		# Input size of 2D list
		rows = int(input("Enter the number of rows for 2D list: "))

		if rows <= 0:
			print("Number should be a Positive Integer")
			return

		# Input the 2d list
		data = []
		print("Enter elements for each row, separated by spaces: ")

		i = 0

		for _ in range(rows):

			row_input = input(f"Row {i + 1}: ").strip()
			row = list(map(int, row_input.split()))
			data.append(row)
			i = i + 1

		# Ask if user wants to enable debug mode
		debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"			

		# Calculate sum of all elements
		result = sum_2d_list(data, debug = debug)

		print(f"Sum of all elements in 2D list is: {result}")


	except ValueError:
		print("Input Error: Enter a valid integers")


# Entry Point of the program
if __name__ == "__main__":
	main()