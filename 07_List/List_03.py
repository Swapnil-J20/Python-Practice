
# Main function to execute the program
def main():
	arr = list() 		# Creates an empty list

	print("Enter values to add to the list (Enter 'q' to quit):")

	for _ in range(100):
		value = input("Enter a value: ")	#Takes input from user

		if value.lower() == 'q':			# exits the loop
			break
		else:
			arr.append(value)				# add value at the end of the list

	# prints the output along with list
	print(f"List created: {arr}")

# Entry point of the program
if __name__ == "__main__":
	main()