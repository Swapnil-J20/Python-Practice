# Write a program to check if a number is prime using a loop

def prime_number_check(val, debug=False):
	"""
	Checks if a value is prime using a loop.

	Parameters:
		val (int): Number to be checked.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		str: Returns whether the number is "a Prime Number" or "not a Prime Number".
	"""
	if val < 2:
		return "not a Prime Number"

	limit = int(val**0.5) + 1  # Only check divisors up to √val
	for i in range(2, limit):
		if val % i == 0:
			if debug:
				print(f"Step {i - 1}: {val} / {i} = {val % i} (remainder)")
			return "not a Prime Number"
		
	return "a Prime Number"


def main():
	"""
	Main function to handle user input and check if the number is prime.
	"""
	try:
		# Input from the user
		num = int(input("Enter a number to check if it is prime: "))

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == 'yes'

		# Check if the number is prime
		result = prime_number_check(num, debug)

		# Print the result
		print(f"{num} is {result}")

	except ValueError:
		print("Input Error: Please enter a valid integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
