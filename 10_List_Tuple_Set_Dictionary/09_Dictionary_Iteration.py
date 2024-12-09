# Write a program to show different ways to iterate a Dictionary

"""
For Loop: Yes
For Loop with Index: No (Dictionaries are not indexed)
While Loop with Index: No
List Comprehension: Yes
Enumerate: Yes
Reverse Iteration: No (Conversion to list of keys required)
"""

def main():
	data = {
		"Name": "Alice",
		"Age": 28,
		"Is_Student": False,
		"Subjects": ["Math", "Science", "English"],
		"Grades": {"Math": "A", "Science": "B", "English": "A"}
	}

	# Step 1: Using For Loop
	print("Step 1: Output using For Loop:")
	for key in data:
		print(f"Key: {key}, Value: {data[key]}")
	print("\n" + "_" * 60)

	# Step 2: For Loop with Index (Not Applicable)
	print("Step 2: For Loop with Index is not applicable to Dictionaries:")
	try:
		for i in range(len(data)):
			print(data[i])  # Attempt to access via index
	except KeyError as er:
		print(f"   Error: {er}")
	print("_" * 60)

	# Step 3: While Loop with Index (Not Applicable)
	print("Step 3: While Loop with Index is not applicable to Dictionaries:")
	try:
		i = 0
		length = len(data)
		while i < length:
			print(data[i])  # Attempt to access via index
			i = i + 1
	except KeyError as err:
		print(f"   Error: {err}")
	print("_" * 60)

	# Step 4: Using List Comprehension
	print("Step 4: Using List Comprehension:")
	[print(f"Key: {key}, Value: {value}") for key, value in data.items()]
	print("_" * 60)

	# Step 5: Using Enumerate
	print("Step 5: Using Enumerate:")
	for i, (key, value) in enumerate(data.items()):
		print(f"Index: {i}, Key: {key}, Value: {value}")
	print("_" * 60)

	# Step 6: Reverse Iteration (Not Directly Possible)
	print("Step 6: Reverse Iteration (Using Reversed Keys):")
	keys = list(data.keys())  # Convert keys to a list to reverse
	for key in reversed(keys):
		print(f"Key: {key}, Value: {data[key]}")
	print("_" * 60)


if __name__ == "__main__":
	main()

