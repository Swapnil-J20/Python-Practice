import My_Module

def main():
	print("Value of __name__ from main is:", __name__)

	num1 = int(input("Enter the first number: "))

	num2 = int(input("Enter the second number: "))

	sum = My_Module.Addition(num1, num2)

	print(f"\nAddition of {num1} and {num2} is {sum}")


if __name__ == "__main__":
	main()