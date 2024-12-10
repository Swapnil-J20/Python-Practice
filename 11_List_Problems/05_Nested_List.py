# Create a nested list representing a matrix and calculate the sum of each row

def input_matrix(rows, cols, debug = False):
	"""
	Takes user input to construct a matrix of given dimensions.

	Parameters:
		rows (int): Number of rows in the matrix.
		cols (int): Number of columns in the matrix.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		matrix (list of list): The constructed matrix.
	"""
	matrix = []
	print(f"\nEnter the elements row by row (total: {rows} rows, {cols} columns):")
	for i in range(rows):
		row = []
		print(f"Enter {cols} elements for row {i + 1}:")
		for j in range(cols):
			while True:
				try:
					element = float(input(f"Enter element {j + 1} for row {i + 1}: "))
					row.append(element)
					if debug:
						print(f"Debug: Added {element} to row {i + 1}")
					break
				except ValueError:
					print("Invalid input! Please enter a valid number.")
		matrix.append(row)
		if debug:
			print(f"Debug: Current matrix state: {matrix}")
	return matrix


def calculate_row_sums(matrix, debug=False):
	"""
	Calculates the sum of each row in a matrix.

	Parameters:
		matrix (list of list): The matrix for which row sums are to be calculated.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		row_sums (list): List of sums of each row.
	"""
	row_sums = []
	for i, row in enumerate(matrix):
		row_sum = 0
		for value in row:
			row_sum = row_sum + value
			if debug:
				print(f"Debug: Adding {value}, Current row sum: {row_sum}")
		row_sums.append(row_sum)
		if debug:
			print(f"Debug: Completed row {i + 1}, Row sum: {row_sum}")
	return row_sums


def main():
	"""
	Main function to gather input, create a matrix, and display the sum of each row.
	"""
	try:
		# Input: Matrix dimensions
		rows = int(input("Enter the number of rows for the matrix: "))
		
		while rows <= 0:
			print("\nError: Enter a positive number for rows.")
			rows = int(input("Try again. Enter the number of rows: "))

		cols = int(input("Enter the number of columns for the matrix: "))
		
		while cols <= 0:
			print("\nError: Enter a positive number for columns.")
			cols = int(input("Try again. Enter the number of columns: "))

		# Debug mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Input: Matrix
		matrix = input_matrix(rows, cols, debug)

		# Output: Matrix
		print("\nMatrix:")
		for row in matrix:
			print(row)

		# Calculate and Display Row Sums
		row_sums = calculate_row_sums(matrix, debug)
		print("\nSum of Each Row:")
		for i, row_sum in enumerate(row_sums):
			print(f"Row {i + 1}: Sum = {row_sum}")

	except ValueError:
		print("Error: Please enter valid numbers for rows and columns.")


# Entry Point of the Program
if __name__ == "__main__":
	main()








