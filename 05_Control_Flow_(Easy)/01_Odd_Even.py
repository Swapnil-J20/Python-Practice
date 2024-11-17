''' Write a program to take an integer input from user and
print whether the number is odd or even '''

# Takes one integer and returns "Even" or "Odd" if its divisible by 2
def even_odd(val):
	if val % 2 == 0:
		return "Even"
	else:
		return "Odd"

# Main function where the program begins & executes
def main():
	num = int(input("Enter the number: "))

	ans = even_odd(num)

	print(f"{num} is {ans}")

# Starter & Function call
if __name__ == "__main__":
	main()