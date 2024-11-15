# Function to add two integers and returns their sum
def Addition(value1, value2):
	ans = value1 + value2
	return ans

# Main function that executes the program
def main():
	print("Enter the first number:")
	num1 = int(input())

	print("Enter the second number:")
	num2 = int(input())

	sum = Addition(num1, num2)

	print("The addition is:", sum)

# Program starts here
if __name__ == "__main__":
	main()