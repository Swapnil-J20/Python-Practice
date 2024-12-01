# Write a program to print the Fibonacci series up to n terms using a loop. Example: Input: n = 5 → Output: 0, 1, 1, 2, 3

def fibonacci(val, debug=False):
	"""
	Prints the Fibonacci series up to n terms using a loop.

	Parameters:
		val (int): Number of terms in the Fibonacci series.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""
	if val <= 0:
		print("Enter a number greater than zero.")
		return

	i = 0
	j = 1

	for step in range(val):
		print(i, end=" ")  # Print the current Fibonacci number

		# Update Fibonacci variables
		if debug:
			print(f"\nStep {step + 1}: Before update - i = {i}, j = {j}")

		i, j = j, i + j  # Update i to j, and j to the next Fibonacci number

		if debug:
			print(f"Step {step + 1}: After update - i = {i}, j = {j}")


def main():
	"""
	Main function to handle user input and print the Fibonacci series.
	"""
	try:
		# Input from the user
		num = int(input("Enter the number of terms for the Fibonacci series: "))

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == 'yes'

		# Print the Fibonacci series
		fibonacci(num, debug)

	except ValueError:
		print("Input Error: Please enter a valid positive integer.")


# Entry Point of the program
if __name__ == "__main__":
	main()
