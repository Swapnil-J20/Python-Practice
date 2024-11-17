# Create a program that takes two numbers and an operator ( +, -, *, /) as input and performs the corresponding operation. Handle invalid operators.

# Created a library that will do the calculation
import Calculator_Module


def main():

	try:
		# Gets input from the user
		num1 = float(input("Enter the first number: "))
		num2 = float(input("Enter the second number: "))
		operator = input("Enter an operator from (+, -, *, /): ").strip()

		# Checks if correct operator is provided
		if operator not in ("+", "-", "*", "/"):
			print("Enter a valid operator")

		else:
			if operator == "+":
				ans = Calculator_Module.addition(num1, num2)
			elif operator == "-":
				ans = Calculator_Module.substraction(num1, num2)
			elif operator == "*":
				ans = Calculator_Module.multiplication(num1, num2)
			else:
				ans = Calculator_Module.division(num1, num2)

			# prints the final output
			print(f"Output of calculation is: {ans}")

	except ValueError:
		print("Please enter a valid number")

# Entry Point Function
if __name__ == "__main__":
	main()