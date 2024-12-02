# Write a program to find the maximum and minimum numbers in a list using a loop

def max_min(data, debug=False):
	"""
	Determines the maximum and minimum values in a list using a loop.

	Parameters:
		data (list): List of values to check.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: Maximum and minimum values in the list (maxima, minima).
	"""
	if len(data) == 0:
		return None, None  # Handle empty lists gracefully

	# Initialize maxima and minima to the first element of the list
	maxima = data[0]
	minima = data[0]

	# Loop through the list to find maxima and minima
	for i, num in enumerate(data):
		if num > maxima:
			maxima = num
			if debug:
				print(f"Step {i + 1}: New maxima found: {maxima}")
		if num < minima:
			minima = num
			if debug:
				print(f"Step {i + 1}: New minima found: {minima}")

	return maxima, minima


def main():
	"""
	Main function to handle user input and find maximum and minimum values in a list.
	"""
	try:
		# Input the number of elements
		limit = int(input("Enter the number of values in the list: "))

		if limit <= 0:
			print("The number of values must be a positive integer.")
			return

		series = []

		print("Enter the numbers:")

		# Input list elements
		for _ in range(limit):
			num = float(input())
			series.append(num)

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == 'yes'

		# Find the maximum and minimum values
		max_val, min_val = max_min(series, debug)

		# Print the results
		print(f"\nFor the list {series}:")
		print(f"Maximum number is: {max_val}")
		print(f"Minimum number is: {min_val}")

	except ValueError:
		print("Input Error: Please enter valid numbers.")


# Entry Point of the program
if __name__ == "__main__":
	main()
