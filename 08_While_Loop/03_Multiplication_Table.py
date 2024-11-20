# Write a program to print the multiplication table of a given number n

def multiplication_table(val):
	ans = 1
	count = 1

	while count < 11:
		ans = val * count
		print(f"{val} x {count} = {ans}")
		count = count + 1

def main():

	num = int(input("Enter a number to get multiplication table: "))

	multiplication_table(num)

# Entry point function
if __name__ == "__main__":
	main()