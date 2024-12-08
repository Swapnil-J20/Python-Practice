# Write a program to show different ways to iterate a Tuple

"""
For Loop: Yes
For Loop with Index: No
While Loop with Index: No
"""

def main():

	data = {11, 37, 69, 83, 105, 37, 11, 69}

	# Using For Loop
	print("Step 1: Output using For Loop: ")
	
	for item in data:
		print(item, end = " ")

	print("\n" + "_" * 60)

	# For Loop with Index doesn't execute with Set due to Unordered nature
	print("\nStep 2: For Loop with Index doesn't apply to Set")
	
	try:
		for i in range(len(data)):
			print(data[i])

	except TypeError as er:
		print(f"	Error: {er}", end = " ")

	print("\n" + "_" * 60)

	# While Loop with Index doesn't execute with Set due to its Unordered nature
	print("\nStep 3: While Loop with Index doesn't apply to Set")

	try:
		i = 0
		length = len(data)

		while i < length:
			print(data[i])
	except TypeError as err:
		print(f"	Error: {err}", end = " ")

	print("\n" + "_" * 60)

	# Using List Comprehension for Iteration
	print("\nStep 4: Using List Comprehension")

	[print(item, end = " ") for item in data]

	print("\n" + "_" * 60)

	# Using Enumerate for Index and Value
	print("\nStep 5: Using Index and Value")

	for i, item in enumerate(data):
		print(f"Index {i}: Value: {item}")

	print("\n" + "_" * 60)


if __name__ == "__main__":
	main()