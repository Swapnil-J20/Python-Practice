# Write a program to check if a given year is a leap year

def leap_year(value):
	'''
	Function to calculate if year is leap year

	Parameters: value (int)

	Returns: string - "a leap year", "not a leap year"
	'''

	if value <= 0:
		return "not a valid year"

	if value % 4 == 0 and (value % 400 == 0 or value % 100 != 0):
		return "a leap year"

	else:
		return "not a leap year"


def main():

	# Main function to execute the program

	try:
		# Accept input and convert to an integer
		year = int(input("Enter the year to check if it is a leap year: "))

		# Calculate if year is leap or not
		ans = leap_year(year)

		# Display the result
		if ans == "not a valid year":
			print(f"{year} is {ans}. Please enter a positive year.")
        
		else:
			print(f"The year {year} is {ans}.")

	except ValueError:
		print("Invalid input. Please enter a valid integer for year")

# Entry point of the program
if __name__ == "__main__":
	main()