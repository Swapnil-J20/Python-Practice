# Write a program highlighting different features of a list

def main():
	# Example of a Heterogeneous List
	alist = [11, 90.8, True, "Hello"]
	print(f"1. Lists can store heterogeneous data types: {alist}")
	print(f"2. Lists are ordered, so the elements remain in the order they were added: {alist}")
	print(f"3. Accessing data by index (element at index 2): {alist[2]}")

	# Example of Duplicate Elements and Mutability
	blist = [11, 21, 205, 311, 21]
	print(f"\n4. Lists can contain duplicate elements: {blist}")

	print(f"5. Lists are mutable:")
	# Demonstrating Append
	blist.append(999)
	print(f"   After appending 999: {blist}")

	# Demonstrating Pop
	blist.pop()
	print(f"   After popping the last element: {blist}")

	# Demonstrating Index Replacement
	blist[2] = True
	print(f"   After replacing the element at index 2 with True: {blist}")


if __name__ == "__main__":
	main()
