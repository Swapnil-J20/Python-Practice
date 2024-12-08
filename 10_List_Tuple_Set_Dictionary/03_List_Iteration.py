# Write a program to show different ways to iterate a list

def main():
	data = [77, 21, 69, -8, 999]  # Sample list

	# Using a For Loop
	print("Step 1: Output using For Loop: ")
	for item in data:
		print(item, end=" ")
	print("\n" + "_" * 20)

	# Using a For Loop with Index
	print("Step 2: Output using For Loop with Index: ")
	for i in range(len(data)):
		print(data[i], end=" ")
	print("\n" + "_" * 20)

	# Using a While Loop with Index
	print("Step 3: Output using While Loop with Index: ")
	length = len(data)
	i = 0
	while i < length:
		print(data[i], end=" ")
		i = i + 1
	print("\n" + "_" * 20)

	# Using List Comprehension for Iteration
	print("Step 4: Output using List Comprehension: ")
	[print(item, end=" ") for item in data]
	print("\n" + "_" * 20)


if __name__ == "__main__":
	main()