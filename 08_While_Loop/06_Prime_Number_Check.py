# Write a program to check if a number is prime using a loop.

def prime(val):
	"""
    Checks if a number is prime using a while loop.

    Parameters:
        val (int): The number to check.

    Returns:
        str: "Prime Number" if the number is prime, otherwise "Not a Prime Number".
    """

	if val < 2:
		return "Not a Prime Number"  # Numbers less than 2 are not prime

	i = 2
	while i * i <= val:  # Check divisors up to the square root of val
		if val % i == 0:
			return "Not a Prime Number"
		i += 1

	return "Prime Number"


# Main function where the program starts
def main():

	# Take user input
	num = input("Enter a number: ")

	try:
		num = int(num)

		# Check if the number is prime
		status = prime(num)

		# Output the result
		print(f"{num} is {status}")

	except ValueError:
		print("Enter a valid integer")




if __name__ == "__main__":
	main()