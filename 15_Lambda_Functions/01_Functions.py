"""
Write a program demonstrating different types of functions.
"""

# Function that accepts nothing and returns nothing
def func1():
	"""
	Function Type: Accepts Nothing, Returns Nothing
	"""
	print("Inside Func1")


# Function that accepts one parameter and returns nothing
def func2(text):
	"""
	Function Type: Accepts One Parameter, Returns Nothing

	Parameters:
		num (str): A string value to be printed.
	"""
	print(f"\nInside Func2 with Argument: {text}")


# Function that accepts one parameter and returns one value
def func3(num):
	"""
	Function Type: Accepts One Parameter, Returns One Value

	Parameters:
		num (int): An integer value to be incremented.

	Returns:
		int: The input number incremented by 2.
	"""
	print(f"\nInside Func3 with Argument: {num}")
	return num + 2


# Function that accepts two parameters and returns one value
def func4(val1, val2):
	"""
	Function Type: Accepts Two Parameters, Returns One Value

	Parameters:
		val1 (int): The first integer value.
		val2 (int): The second integer value.

	Returns:
		int: The sum of the two input values.
	"""
	print(f"\nInside Func4 with Arguments: {val1}, {val2}")
	return val1 + val2


# Function that accepts two parameters and returns two values
def func5(val1, val2):
	"""
	Function Type: Accepts Two Parameters, Returns Two Values

	Parameters:
		val1 (int): The first integer value.
		val2 (int): The second integer value.

	Returns:
		tuple: A tuple containing the sum and difference of the two input values.
	"""
	print(f"\nInside Func5 with Arguments: {val1}, {val2}")
	add = val1 + val2
	subtract = val1 - val2
	return add, subtract


def main():
	"""
	Main function to demonstrate different function types.
	"""
	# Function Type 1: Accepts Nothing, Returns Nothing
	func1()

	# Function Type 2: Accepts One Parameter, Returns Nothing
	func2("Hello")

	# Function Type 3: Accepts One Parameter, Returns One Value
	result = func3(8)
	print(f"Return Value of Func3: {result}")

	# Function Type 4: Accepts Two Parameters, Returns One Value
	result = func4(8, 7)
	print(f"Return Value of Func4: {result}")

	# Function Type 5: Accepts Two Parameters, Returns Two Values
	result1, result2 = func5(8, 7)
	print(f"Return Values of Func5: {result1}, {result2}")


# Entry Point of the Program
if __name__ == "__main__":
	main()
