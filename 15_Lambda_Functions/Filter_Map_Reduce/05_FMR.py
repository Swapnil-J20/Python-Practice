# Lambda functions for operations
CheckEven = lambda No: (No % 2 == 0)  # Returns True if the number is even
Doubles = lambda No: No * 2  # Doubles the given number
Sum = lambda A, B: A + B  # Returns sum of two numbers

def reduceX(Helper_Function, Data):
	"""
	Custom implementation of the reduce function.
	Iteratively applies the Helper_Function to elements in Data.

	Parameters:
		Helper_Function (function): A function that takes two arguments and performs an operation.
		Data (list): A list of elements to be reduced.

	Returns:
		int: The final reduced value after applying the Helper_Function iteratively.
	"""
	Ans = 0  # Initialize accumulator
	for No in Data:
		Ans = Helper_Function(Ans, No)  # Apply function iteratively

	return Ans  # Return final computed value

def filterX(Helper_Function, Data):
	"""
	Custom implementation of the filter function.
	Filters elements from Data based on Helper_Function.

	Parameters:
		Helper_Function (function): A function that returns True or False for each element.
		Data (list): A list of elements to be filtered.

	Returns:
		list: A list of elements that satisfy the condition in Helper_Function.
	"""
	Result = []  # Initialize result list
	for No in Data:
		if Helper_Function(No):  # If condition is met, add to result
			Result.append(No)

	return Result  # Return filtered list

def mapX(Helper_Function, Data):
	"""
	Custom implementation of the map function.
	Applies Helper_Function to each element in Data.

	Parameters:
		Helper_Function (function): A function that modifies each element.
		Data (list): A list of elements to be mapped.

	Returns:
		list: A list of transformed elements.
	"""
	Result = []  # Initialize result list
	for No in Data:
		Value = Helper_Function(No)  # Apply transformation
		Result.append(Value)

	return Result  # Return modified list

def main():
	"""
	Main function to demonstrate functional programming concepts.
	Uses custom implementations of map, filter, and reduce.
	"""
	try:
		# Get number of elements from user
		print("Enter number of elements you want to enter: ")
		iSize = int(input())

		# Validate input size
		if iSize <= 0:
			print("Error: Please enter a positive integer.")
			return

		# Accept user input for list elements
		Data_Input = []
		print("Please enter the data: ")
		for _ in range(iSize):
			Value = int(input())  # Convert input to integer
			Data_Input.append(Value)

		print("\nOriginal Data: ", Data_Input)

		# Step 1: Filter (Extract even numbers)
		Data_Filter = filterX(CheckEven, Data_Input)
		print("Data after filter (Even Numbers): ", Data_Filter)

		# Step 2: Map (Double the even numbers)
		Data_Map = mapX(Doubles, Data_Filter)
		print("Data after map (Doubled): ", Data_Map)

		# Step 3: Reduce (Sum the doubled values)
		Output = reduceX(Sum, Data_Map)
		print("Result after reduce (Sum): ", Output)

	except ValueError:
		print("Error: Please enter valid integer values.")  # Handle invalid input errors

# Entry Point
if __name__ == "__main__":
	main()
