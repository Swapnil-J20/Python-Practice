# Write a program to check if a number is an Armstrong number

def armstrong_number(val, debug = False):
	"""
	Checks if a given number is an Armstrong number.

	Parameters:
		val (int): The number to check.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		str: "Armstrong Number" if the number is an Armstrong number,
			 otherwise "not an Armstrong Number".
	"""
	counter = str(val)  # Convert the number to a string to access digits
	length = len(counter)  # Find the number of digits
	check = 0  # Variable to calculate the sum of powers of digits

	for i, digit in enumerate(counter):
		digit = int(digit)  # Convert character to integer
		check = check + digit**length  # Add the digit raised to the power of the length
		if debug:
			print(f"Step {i + 1}: Digit = {digit}, Power = {digit**length}, Running Total = {check}")

	# Check if the calculated sum equals the original number
	if check == val:
		return "Armstrong Number"
	else:
		return "not an Armstrong Number"


def main():
	"""
	Main function to handle user input and check if a number is an Armstrong number.
	"""
	try:
		# Input the number to check
		num = int(input("Enter the number to check if it's an Armstrong Number: "))

		if num < 0:
			print("No Armstrong numbers less than 0.")
			return

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").lower().strip() == 'yes'

		# Check if the number is an Armstrong number
		result = armstrong_number(num, debug)

		# Print the result
		print(f"{num} is: {result}")

	except ValueError:
		print("Input Error: Please enter a valid number.")


# Entry Point of the program
if __name__ == "__main__":
	main()
