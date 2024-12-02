# Write a program to find the sum of digits of a number using a loop. Example: Input: 123 → Output: 6 (because 1 + 2 + 3 = 6)

def digit_sum(val, debug=False):
	"""
	Determines the sum of digits in a number using a loop.

	Parameters:
		val (int): Number of which sum of digits is to be determined.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		int: Sum of the digits.
	"""
	result = 0

	# Convert the number to a string to iterate over digits
	for i, digit in enumerate(str(val)):
		digit = int(digit)  # Convert character to integer
		result = result + digit  # Add the digit to the result
		if debug:
			print(f"Step {i + 1}: Adding {digit}, Current Sum: {result}")

	return result


def main():
	"""
	Main function to handle user input and print the sum of digits.
	"""
	try:
		# Input from the user
		num = int(input("Enter the number: "))

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == 'yes'

		# Calculate the sum of digits
		output = digit_sum(num, debug)

		# Print the result
		print(f"Sum of digits of {num} is: {output}")

	except ValueError:
		print("Input Error: Please enter a valid integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
