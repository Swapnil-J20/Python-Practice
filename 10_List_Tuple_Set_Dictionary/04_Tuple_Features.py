# Write a program highlighting different features of a Tuple

def main():
	# Example of a Heterogeneous Tuple
	atuple = (11, 90.8, True, "Hello")
	print(f"1. Tuples can store heterogeneous data types: {atuple}")
	print(f"\n2. Tuples are ordered, so the elements remain in the order they were added: {atuple}")
	print(f"\n3. Accessing data by index (element at index 2): {atuple[2]}")

	# Example of Duplicate Elements
	btuple = (11, 21, 205, 311, 21)
	print(f"\n4. Tuples can contain duplicate elements: {btuple}")

	# Tuples are Immutable
	print("\n5. Tuples are immutable (cannot be changed):")
	try:
		btuple[1] = 99  # Attempt to modify a tuple element
	except TypeError as e:
		print(f"   Error: {e}")

	# Tuples Can Contain Mutable Objects
	print("\n6. Tuples can contain mutable objects:")
	c_tuple = (11, [22, 33], 44)
	print(f"   Original Tuple: {c_tuple}")
	c_tuple[1][0] = 99  # Modifying the list inside the tuple
	print(f"   Modified Tuple: {c_tuple} (Note: The list inside the tuple was modified)")

	# Tuple Packing and Unpacking
	print("\n7. Tuple Packing and Unpacking:")
	packed_tuple = 1, 2, 3  # Packing
	print(f"   Packed Tuple: {packed_tuple}")
	a, b, c = packed_tuple  # Unpacking
	print(f"   Unpacked Values: a = {a}, b = {b}, c = {c}")

	# Single-element Tuple
	print("\n8. Creating a Single-element Tuple:")
	single_element_tuple = (11,)  # Must include a trailing comma
	print(f"   Single-element Tuple: {single_element_tuple}, Type: {type(single_element_tuple)}")

# Entry Point of the Program
if __name__ == "__main__":
	main()