# Lambda function to check if a number is even
check_even = lambda val: val % 2 == 0

def main():
	"""
	Main function to take user input and check if the number is even or odd using a lambda function.
	"""
	try:
		num = int(input("Enter a number to check if it's Even: "))
		result = check_even(num)

		if result:
			print(f"\nNumber {num} is Even")
		else:
			print(f"\nNumber {num} is Odd")

	except ValueError:
		print("Error: Please enter a valid integer.")

if __name__ == "__main__":
	main()
