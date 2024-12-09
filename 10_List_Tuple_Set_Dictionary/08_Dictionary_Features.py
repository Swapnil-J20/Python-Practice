# Write a program highlighting different features of a Dictionary

"""
Features of a Dictionary:
1. Data: Key-Value pairs (Keys must be immutable)
2. Ordered: Yes (Python 3.7+)
3. Indexed: Accessed via Keys
4. Mutable: Yes
5. Duplicates: Keys - No, Values - Yes
6. Dictionary Methods: keys(), values(), items(), copy()
"""

def main():
	# Step 1: Creating a Dictionary
	data = {
		"Name": "Alice",
		"Age": 28,
		"Is_Student": False,
		"Subjects": ["Math", "Science", "English"],
		"Grades": {"Math": "A", "Science": "B", "English": "A"}
	}
	print("Step 1: Sample Dictionary:")
	print(data)
	print("_" * 60)

	# Step 2: Dictionary is Ordered
	print(f"\n2. Dictionary is ordered, so the elements remain in the order they were added: {data}")
	print("_" * 60)

	# Step 3: Accessing Data by Keys
	print("Step 3: Accessing Data by Keys:")
	print(f"Name: {data['Name']}")
	print(f"Age: {data['Age']}")
	print(f"Subjects: {data['Subjects']}")
	print("_" * 60)

	# Step 4: Modifying Values (Mutability)
	print("Step 4: Modifying Values (Mutability):")
	data["Age"] = 29  # Updating Age
	data["City"] = "New York"  # Adding a new Key-Value pair
	print("Modified Dictionary:")
	print(data)
	print("_" * 60)

	# Step 5: Handling Duplicate Keys
	print("Step 5: Handling Duplicate Keys (Only the Last Key is Retained):")
	data_duplicate = {"Key": 1, "Key": 2}
	print(data_duplicate)
	print("_" * 60)


	# Step 6: Dictionary-Specific Methods
	print("Step 6: Demonstrating Dictionary-Specific Methods:")
	
	keys = data.keys()
	values = data.values()
	items = data.items()
	print(f"Keys: {keys}")
	print(f"Values: {values}")
	print(f"Items: {items}")
	copied_data = data.copy()
	print(f"Copied Dictionary: {copied_data}")
	data.pop("Is_Student")
	print(f"After Removing 'Is_Student': {data}")
	print("_" * 60)


if __name__ == "__main__":
	main()
