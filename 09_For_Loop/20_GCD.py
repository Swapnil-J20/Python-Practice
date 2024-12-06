# Write a program to find the greatest common divisor (GCD) of two numbers using a loop

def gcd(val1, val2, debug=False):
	"""
	Finds the greatest common divisor (GCD) of two numbers using the Euclidean Algorithm.

	Parameters:
		val1 (int): The first number.
		val2 (int): The second number.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		int: The GCD of the two numbers.
	"""
	while val2 != 0:
		if debug:
			print(f"Calculating GCD: val1 = {val1}, val2 = {val2}")
		val1, val2 = val2, val1 % val2  # Update values for the next iteration

	if debug:
		print(f"Final GCD: {val1}")
	return val1


def main():
	"""
	Main function to handle user input and find the GCD of two numbers.
	"""
	try:
		# Input two positive integers
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))

		if num1 <= 0 or num2 <= 0:
			print("Please enter positive integers only.")
			return

		# Enable debug mode if the user requests it
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Calculate the GCD
		result = gcd(num1, num2, debug)

		# Display the result
		print(f"The GCD of {num1} and {num2} is: {result}")

	except ValueError:
		print("Input Error: Please enter valid positive integers.")


# Entry Point of the program
if __name__ == "__main__":
	main()
