# Write a program that takes a number from the user and prints if it is positive, negative, or zero

def positive_negative(val):

	'''
	Compares if value is greater than or less than or equal to zero
	
	Parameters:
        val (int): Any integer

    Returns:
        str: "Positive", "Negative", or "Zero"
	'''

	if val > 0:
		return "Positive"
	
	elif val < 0:
		return "Negative"
	
	else:
		return "Zero"

# Main function to execute the program
def main():

	try:
		num = float(input("Enter a number: "))

		ans = positive_negative(num)

		print(f"{num} is {ans}")

	except ValueError:
		print("Error: Invalid input! Please enter a valid number")

# Entry point of the program
if __name__ == "__main__":
	main()