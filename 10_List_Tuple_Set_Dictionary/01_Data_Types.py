# Write a program that displays different data types (List, Tuple, Set, Dictionary) 

def main():
	# Initializing different data types
	alist = [10, 20, 30, 40]
	atuple = (10, 20, 30, 40)
	aset = {10, 20, 30, 40}
	adictionary = {"A": 10, "B": 20, "C": 30, "D": 40}

	# Displaying each data type with its representation and type
	print(f"List: {alist} | Data Type: {type(alist)}")
	print(f"Tuple: {atuple} | Data Type: {type(atuple)}")
	print(f"Set: {aset} | Data Type: {type(aset)}")
	print(f"Dictionary: {adictionary} | Data Type: {type(adictionary)}")


if __name__ == "__main__":
	main()
