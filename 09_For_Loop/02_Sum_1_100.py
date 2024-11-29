# Write a program to calculate the sum of numbers from 1 to 100 using a loop

# Main function where the program starts
def main():
	"""
	Calculates the sum of numbers from 1 to 100 using a 'for' loop.
	Includes optional debug prints to show loop execution.
	"""
	print("This program calculates the sum of all numbers from 1 to 100.")

	# Ask if the user wants to enable debug mode
	debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

	i = 1  # Loop counter
	total = 0  # Variable to store the running total

	# Loop from 1 to 100 (inclusive)
	for i in range(1, 101):
		total = total + i

		# Debug print to show current state
		if debug:
			print(f"Step {i}: Current value of i = {i}")
			print(f"Step {i}: Current value of total = {total}")

	# Output the final sum
	print(f"Sum of numbers from 1 to 100 is: {total}")


# Entry Point of the program
if __name__ == "__main__":
    main()
