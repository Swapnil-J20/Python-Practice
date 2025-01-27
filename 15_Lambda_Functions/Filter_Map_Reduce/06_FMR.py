from functools import reduce

# Lambda functions for functional programming
is_even = lambda no: (no % 2 == 0)
double = lambda no: no * 2
add = lambda a, b: a + b  

def main():
	"""
	Main function to take user input, filter even numbers, double them, and find their sum.
	"""
	try:
		iSize = int(input("Enter the number of elements: "))

		if iSize <= 0:
			print("Error: Please enter a positive integer.")
			return

		# Collect user input
		data_input = []
		print("Enter the numbers:")
		for _ in range(iSize):
			while True:
				try:
					value = int(input())
					data_input.append(value)
					break
				except ValueError:
					print("Invalid input. Please enter an integer.")

		print("\nOriginal Data:", data_input)

		# Functional processing
		data_filter = list(filter(is_even, data_input))
		print("Data after filter (Even numbers):", data_filter)

		data_map = list(map(double, data_filter))
		print("Data after map (Doubled values):", data_map)

		if data_map:
			output = reduce(add, data_map)
			print("Final Result after reduce (Sum):", output)
		else:
			print("No even numbers to process.")

	except ValueError:
		print("Error: Please enter a valid integer.")

if __name__ == "__main__":
	main()
