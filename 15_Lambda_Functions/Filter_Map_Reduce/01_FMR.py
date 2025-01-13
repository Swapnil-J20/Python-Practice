# Write a program demonstrating the concept of Filter, Map, Reduced using Normal Functions


def is_even(num):
	"""
	Checks if a number is even.

	Parameters:
		num (int): The number to check.

	Returns:
		bool: True if the number is even, False otherwise.
	"""
	return num % 2 == 0


def increment_by_2(num):
	"""
	Increments the given number by 2.

	Parameters:
		num (int): The number to increment.

	Returns:
		int: The incremented value.
	"""
	return num + 2


def filterX(arr, function):
	"""
	Filters elements from the list based on the given function.

	Parameters:
		arr (list): The list of elements to filter.
		function (function): The function to apply to each element.

	Returns:
		list: A list of elements that satisfy the condition.
	"""
	result = []
	for num in arr:
		if function(num):
			result.append(num)
	return result


def mapX(arr, function):
	"""
	Maps each element in the list to a new value based on the given function.

	Parameters:
		arr (list): The list of elements to map.
		function (function): The function to apply to each element.

	Returns:
		list: A list of transformed elements.
	"""
	result = []
	for num in arr:
		result.append(function(num))
	return result


def reduceX(arr, function):
	"""
	Reduces the list to a single value using the given function.

	Parameters:
		arr (list): The list of elements to reduce.
		function (function): The function to apply to the elements.

	Returns:
		int: The reduced value.
	"""
	result = arr[0]
	for num in arr[1:]:
		result = function(result, num)
	return result


def add(x, y):
	"""
	Adds two numbers.

	Parameters:
		x (int): The first number.
		y (int): The second number.

	Returns:
		int: The sum of x and y.
	"""
	return x + y


def main():
	"""
	Main function to demonstrate filter, map, and reduce using normal functions.
	"""
	data = [2, 3, 1, 6, 4, 5, 11, 16, 20]
	print("Original Data:", data)

	# Filter
	filtered_data = filterX(data, is_even)
	print("\nData after Filter:", filtered_data)

	# Map
	mapped_data = mapX(filtered_data, increment_by_2)
	print("\nData after Map:", mapped_data)

	# Reduce
	reduced_result = reduceX(mapped_data, add)
	print("\nData after Reduce:", reduced_result)


# Entry point of the program
if __name__ == "__main__":
	main()
