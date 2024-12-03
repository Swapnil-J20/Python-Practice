"""
	Print a pyramid pattern: Example: Input: rows = 3
	
	  *
	 ***
	*****
"""

def pattern_pyramid(val, debug=False):
	"""
	Prints a Pyramid of stars for a given number of rows.

	Parameters:
		val (int): Number of rows for the pyramid.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	stars = 1  # Number of stars in the first row
	spaces = val - 1  # Number of spaces before the stars in the first row

	for i in range(1, val + 1):
		if debug:
			print(f"Step {i}: Spaces = {spaces}, Stars = {stars}")
		# Print spaces followed by stars
		print(" " * spaces + "*" * stars)
		# Update spaces and stars for the next row
		spaces = spaces - 1
		stars = stars + 2


def main():
	"""
	Main function to handle user input and print the pyramid pattern.
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
		pattern_pyramid(num, debug)

	except ValueError:
		print("Input Error: Please enter a valid positive integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
