# Write a program to count the number of even and odd numbers in a list. Example: Input: [1, 2, 3, 4, 5, 6] → Output: Even: 3, Odd: 3

def count_odd_even(data, debug=False):
	"""
	Counts even and odd numbers in a list using a loop.

	Parameters:
		data (list): List of numbers to be checked.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		tuple: A tuple containing the count of even and odd numbers (even, odd).
	"""
	even = 0
	odd = 0
	counter = 1

	for i in data:
		if i % 2 == 0:
			even = even + 1
			if debug:
				print(f"Step {counter}: Number: {i}, Even Count: {even}, Odd Count: {odd}")
		else:
			odd = odd + 1
			if debug:
				print(f"Step {counter}: Number: {i}, Even Count: {even}, Odd Count: {odd}")
		counter = counter + 1

	return even, odd


def main():
	"""
	Main function to handle user input and count even and odd numbers in the list.
	"""
	try:
		elements = int(input("How many numbers should be in the list? "))

		if elements <= 0:
			print("Number of elements should be a positive integer.")
			return

		numbers = []

		print("Enter the numbers: ")

		for _ in range(elements):
			try:
				num = int(input())
				numbers.append(num)
			except ValueError:
				print("Invalid input. Please enter a valid integer.")

		# Ask if the user wants to enable debug mode
		debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Count even and odd numbers
		even, odd = count_odd_even(numbers, debug)

		# Print the results
		print(f"\nFor List: {numbers}")
		print(f"Even Numbers: {even}")
		print(f"Odd Numbers: {odd}")

	except ValueError:
		print("Input Error: Please enter a valid positive integer for the number of elements.")


# Entry Point of the program
if __name__ == "__main__":
	main()
