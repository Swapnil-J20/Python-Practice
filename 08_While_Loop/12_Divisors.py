# - Write a program to find all the divisors of a number using a loop.

# External Module that 
import Divisors_Module

def main():

	try:
		# Input from the user

		num = input("Enter a number to get its factorials: ")

		num = int(num)

		ans = Divisors_Module.divisors(num)

		print(f"Factorials of {num}: {ans}")

	except ValueError:
		print("Input Error: Enter a valid integer")


# Entry Point of the program
if __name__ == "__main__":
    main()