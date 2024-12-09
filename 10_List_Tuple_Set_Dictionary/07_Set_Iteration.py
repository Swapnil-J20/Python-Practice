# Write a program to show different ways to iterate a Tuple

"""
For Loop: Yes
For Loop with Index: No
While Loop with Index: No
List Comprehension: Yes
Enumerate: Yes
Reverse Iteration: No (Conversion to list required)
"""

def main():
	data = {11, 37, 69, 83, 105, 37, 11, 69}  # Sample set with duplicates

	# Step 1: Using For Loop
	print("Step 1: Output using For Loop:")
	for item in data:
		print(item, end=" ")
	print("\n" + "_" * 60)

	# Step 2: For Loop with Index (Not Applicable)
	print("Step 2: For Loop with Index is not applicable to Sets (Unordered nature):")
	try:
		for i in range(len(data)):
			print(data[i])  # Attempt to access via index
	except TypeError as er:
		print(f"   Error: {er}")
	print("_" * 60)

	# Step 3: While Loop with Index (Not Applicable)
	print("Step 3: While Loop with Index is not applicable to Sets (Unordered nature):")
	try:
		i = 0
		length = len(data)
		while i < length:
			print(data[i])  # Attempt to access via index
			i += 1
	except TypeError as err:
		print(f"   Error: {err}")
	print("_" * 60)

	# Step 4: Using List Comprehension
	print("Step 4: Using List Comprehension:")
	[print(item, end=" ") for item in data]
	print("\n" + "_" * 60)

	# Step 5: Using Enumerate
	print("Step 5: Using Enumerate (Index and Value):")
	for i, item in enumerate(data):
		print(f"Index {i}: Value: {item}")
	print("_" * 60)

	# Step 6: Reverse Iteration (Not Directly Possible)
	print("Step 6: Reverse Iteration (Not Directly Possible):")
	try:
		for item in reversed(data):  # Attempting reverse iteration directly
			print(item, end=" ")
	except TypeError as err:
		print(f"   Error: {err}")
	print("_" * 60)


if __name__ == "__main__":
	main()
