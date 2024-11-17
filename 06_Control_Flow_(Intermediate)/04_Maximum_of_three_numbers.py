# Write a program to take three numbers as input and print the largest of them

def maximum(val1, val2, val3):
	'''
	Function to compare three values and find the maximum value

    Parameters:
        val1 (float): First number
        val2 (float): Second number
        val3 (float): Third number

    Returns:
        float: The largest of the three values
	'''

	max_val = val1  # Assume the first value is the largest initially

	if val2 > max_val:  # Update if val2 is greater
		max_val = val2

	if val3 > max_val:  # Update if val3 is greater
		max_val = val3

	return max_val

	# Alternatively, in-built max(val1, val2, val3) can also be used

def main():

	"""Main function to execute the program."""

	try:
	
		# Accept three inputs and convert them to floats
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		num3 = float(input("Enter the third number: "))

		# Find the largest number
		ans = maximum(num1, num2, num3)

		# Display the result
		print(f"The largest number is {ans}")

	except ValueError:
		print("Error: Invalid input! Please enter valid numbers.")

# Entry point of the program
if __name__ == "__main__":
	main()