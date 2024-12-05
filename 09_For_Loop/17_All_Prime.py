# Write a program to print all prime numbers between 1 and user input using a loop

def all_prime(val, debug=False):
	"""
	Finds all prime numbers between 1 and the given value.

	Parameters:
		val (int): The upper limit for finding prime numbers.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A list of all prime numbers up to the given value.
	"""
	output = []  # List to store prime numbers

	for i in range(2, val + 1):  # Start from 2, as 1 is not prime
		is_prime = True

		# Check divisors up to sqrt(i)
		for j in range(2, int(i**0.5) + 1):
			if i % j == 0:
				is_prime = False
				if debug:
					print(f"{i} is divisible by {j}. Not a prime.")
				break

		if is_prime:
			output.append(i)
			if debug:
				print(f"{i} is a prime number.")

	return output


def main():
	"""
	Main function to handle user input and provide all prime numbers between 1 and user input number.
	"""
	try:
		# Input the upper limit
		num = int(input("Enter the number to display all primes up to that number: "))

		if num < 2:
			print("There are no prime numbers less than 2.")
			return

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Get all prime numbers
		result = all_prime(num, debug)

		# Print the result
		print(f"All prime numbers up to {num} are: {result}")

	except ValueError:
		print("Input Error: Please enter a valid number.")


# Entry Point of the program
if __name__ == "__main__":
	main()
