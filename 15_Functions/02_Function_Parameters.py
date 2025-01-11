"""
Comprehensive Program Demonstrating Different Function Argument Types
"""

# Function with Positional and Keyword Arguments
def personal_info(name, age, city="Unknown"):
	"""
	Displays personal information.

	Parameters:
		name (str): The name of the person.
		age (int): The age of the person.
		city (str): The city of the person (default is "Unknown").

	Returns:
		None
	"""
	print(f"\nName: {name}")
	print(f"Age: {age}")
	print(f"City: {city}")


# Function with Variable Positional Arguments (*args)
def calculate_sum(*args):
	"""
	Calculates the sum of variable number of arguments.

	Parameters:
		*args: Variable number of arguments.

	Returns:
		int/float: Sum of all the arguments.
	"""
	total = 0
	for index, value in enumerate(args):
		total = total + value
		print(f"Step {index + 1}: Adding {value}, Current Total: {total}")
	return total


# Function with Variable Keyword Arguments (**kwargs)
def display_user_profile(**kwargs):
	"""
	Displays user profile details provided as keyword arguments.

	Parameters:
		**kwargs: Variable number of keyword arguments.

	Returns:
		None
	"""
	print("\nUser Profile:")
	for key, value in kwargs.items():
		print(f"{key}: {value}")


# Function using All Argument Types
def comprehensive_function(name, *scores, country="Unknown", **extra_info):
	"""
	Comprehensive function demonstrating all argument types.

	Parameters:
		name (str): The name of the user.
		*scores: Variable number of scores.
		country (str): The country of the user (default is "Unknown").
		**extra_info: Additional keyword arguments.

	Returns:
		None
	"""
	print(f"\nName: {name}")
	print(f"Scores: {scores}")
	print(f"Country: {country}")
	if extra_info:
		print("Additional Information:")
		for key, value in extra_info.items():
			print(f"{key}: {value}")


# Main Function
def main():
	"""
	Main function to demonstrate different argument types.
	"""

	# Positional and Keyword Arguments
	print("\n[Positional and Keyword Arguments]")
	personal_info("Alice", 25, city="New York")
	personal_info("Bob", 30)  # Uses default city

	# Variable Positional Arguments
	print("\n[Variable Positional Arguments]")
	sum_result = calculate_sum(10, 20, 30, 40, 50)
	print(f"\nTotal Sum: {sum_result}")

	# Variable Keyword Arguments
	print("\n[Variable Keyword Arguments]")
	display_user_profile(name="Charlie", age=28, city="Los Angeles", profession="Engineer")

	# Comprehensive Function
	print("\n[Comprehensive Function Using All Argument Types]")
	comprehensive_function(
		"David",
		85, 90, 78,
		country="USA",
		hobby="Photography",
		job="Data Scientist"
	)


# Entry Point of the Program
if __name__ == "__main__":
	main()
