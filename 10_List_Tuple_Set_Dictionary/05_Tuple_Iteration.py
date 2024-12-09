# Write a program to show different ways to iterate a Tuple

"""
For Loop: Yes
For Loop with Index: Yes
While Loop with Index: Yes
List Comprehension: Yes
Enumerate: Yes
Reverse Iteration: Yes
"""

def main():
	data = (11, 25, 69, 101, 999)  # Sample tuple

	# Using a For Loop
	print("Step 1: Output using For Loop:")
	for item in data:
		print(item, end=" ")
	print("\n" + "_" * 60)

	# Using a For Loop with Index
	print("Step 2: Output using For Loop with Index:")
	for i in range(len(data)):
		print(data[i], end=" ")
	print("\n" + "_" * 60)

	# Using a While Loop with Index
	print("Step 3: Output using While Loop with Index:")
	length = len(data)
	i = 0
	while i < length:
		print(data[i], end=" ")
		i += 1
	print("\n" + "_" * 60)

	# Using List Comprehension
	print("Step 4: Output using List Comprehension:")
	[print(item, end=" ") for item in data]
	print("\n" + "_" * 60)

	# Using Enumerate for Index and Value
	print("Step 5: Using Enumerate (Index and Value):")
	for index, value in enumerate(data):
		print(f"Index {index}: Value: {value}")
	print("\n" + "_" * 60)

	# Using Reversed Iteration
	print("Step 6: Output using Reversed Iteration:")
	for item in reversed(data):
		print(item, end=" ")
	print("\n" + "_" * 60)


# Entry Point of the Program
if __name__ == "__main__":
	main()
