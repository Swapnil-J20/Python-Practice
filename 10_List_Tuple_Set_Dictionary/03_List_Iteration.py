# Write a program to show different ways to iterate a list

"""
For Loop: Yes
For Loop with Index: Yes
While Loop with Index: Yes
List Comprehension: Yes
Enumerate: Yes
Reverse Iteration: Yes
"""

def main():
	data = [77, 21, 69, -8, 999]  # Sample list

	# Step 1: Using a For Loop
	print("Step 1: Output using For Loop:")
	for item in data:
		print(item, end=" ")
	print("\n" + "_" * 60)

	# Step 2: Using a For Loop with Index
	print("Step 2: Output using For Loop with Index:")
	for i in range(len(data)):
		print(data[i], end=" ")
	print("\n" + "_" * 60)

	# Step 3: Using a While Loop with Index
	print("Step 3: Output using While Loop with Index:")
	length = len(data)
	i = 0
	while i < length:
		print(data[i], end=" ")
		i += 1
	print("\n" + "_" * 60)

	# Step 4: Using List Comprehension
	print("Step 4: Output using List Comprehension:")
	[print(item, end=" ") for item in data]
	print("\n" + "_" * 60)

	# Step 5: Using Enumerate
	print("Step 5: Using Enumerate (Index and Value):")
	for i, item in enumerate(data):
		print(f"Index {i}: Value: {item}")
	print("\n" + "_" * 60)

	# Step 6: Reverse Iteration
	print("Step 6: Output using Reverse Iteration:")
	for item in reversed(data):
		print(item, end=" ")
	print("\n" + "_" * 60)


if __name__ == "__main__":
	main()
