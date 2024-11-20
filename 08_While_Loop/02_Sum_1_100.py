#     Write a program to calculate the sum of numbers from 1 to 100 using a loop.

# Main function where the program starts
def main():
	
	i = 100 		# Variable with set value
	sum = 0

	# while loop that reverses the numbers
	while i != 0:
		
		sum = sum + i

		i = i - 1

	# Output that displays the sum
	print(f"Sum of numbers from 1 to 100 is: {sum}")

# Entry point function
if __name__ == "__main__":
	main()