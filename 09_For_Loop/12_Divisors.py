# Write a program to find all the divisors of a number using a loop. Example: Input: 12 → Output: 1, 2, 3, 4, 6, 12

import Divisors_Module

def main():
	"""
	Main function to handle user input and find divisors of a number.
	"""
	try:
		# Input the number
		num = int(input("Enter a number to find its divisors: "))

		if num <= 0:
			print("Please enter a positive integer.")
			return

		# Enable debug mode if requested
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Call the divisors function from Divisors_Module
		result = Divisors_Module.divisors(num, debug)

		# Print the result
		print(f"Divisors of {num} are: {result}")

	except ValueError:
		print("Input Error: Please enter a valid positive integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
