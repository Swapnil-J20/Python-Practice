# Write a program highlighting different features of a Set
"""
Set Features -
1. Data : Heterogeneous
2. Ordered : No
3. Indexed : No
4. Mutable : Yes (Set itself is Mutable, Elements immutable)
5. Duplicates : No
"""

def main():
	data1 = {11, 20, 66, 89, 107, 20}  # Example with duplicates
	data = {11, 97.98, True, "Text"}   # Example with heterogeneous data

	# Feature 1: Heterogeneous Data
	print(f"1. Sets can store heterogeneous data types: {data}")

	# Feature 2: Not Ordered
	print(f"\n2. Sets are not ordered, so the elements don't remain in the order they were added: {data}")

	# Feature 3: No Indexing
	print(f"\n3. Since Sets are unordered, they can't be accessed by index.")
	try:
		print(f"Accessing data by index (element at index 2): {data[1]}")  # Attempt to access using index
	except TypeError as e:
		print(f"   Error: {e}")

	# Feature 4: Mutability of Set
	print(f"\n4. Sets are mutable (elements can be added or removed):")
	try:
		data.add("New Element")  # Adding an element
		print(f"   After adding an element: {data}")
		data.remove(97.98)  # Removing an element
		print(f"   After removing an element: {data}")
	except TypeError as er:
		print(f"   Error: {er}")

	# Feature 5: No Duplicates
	print(f"\n5. Sets cannot have duplicates; they automatically remove them: {data1}")


# Entry Point of the Program
if __name__ == "__main__":
	main()
