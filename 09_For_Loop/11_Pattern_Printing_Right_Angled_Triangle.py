"""
Print a right-angled triangle of stars for a given number of rows: 
Example: Input: rows = 4
	*
	**
	***
	****
""" 

def pattern_right_angled(val, debug=False):
	"""
	Prints a right-angled triangle of stars for a given number of rows.

	Parameters:
		val (int): Number of rows for the triangle.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	for i in range(1, val + 1):
		if debug:
			print(f"Step {i}: Printing {i} star(s)")
		print("*" * i)


def main():
	"""
	Main function to handle user input and print the right-angled triangle star pattern.
	"""
	try:
		# Input the number of rows
		num = int(input("Enter the number of rows: "))

		if num <= 0:
			print("Enter a positive integer for the number of rows.")
			return

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Print the pattern
		pattern_right_angled(num, debug)

	except ValueError:
		print("Input Error: Please enter a valid positive integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
