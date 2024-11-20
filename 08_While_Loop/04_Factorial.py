# Write a program to calculate the factorial of a number using a loop

def factorial(val):
	'''
	Takes an input and provides the factorial
	
	Parameters: 
				val (int): number for factorial calculation (Must be non-negative)
	
	Returns: ans (int): 5! = 120
	'''

	# returns an error if the input is less than 0
	if val < 0:
		return ("#Error: Factorial is not defined for negative numbers")

	ans = 1

	while val != 0:
		ans = ans * val
		val = val - 1

	return ans


def main():

	try:
		# Takes a valid input from user

		num = int(input("Enter a number to get the factorial: "))

		# calculate the factorial
		result = factorial(num)

		# prints the output
		print(f"Factorial of {num} is {result}")

	except ValueError:
		print("Error: Enter a valid number")

# Entry point of the program
if __name__ == "__main__":
	main()