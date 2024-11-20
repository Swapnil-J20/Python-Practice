# Write a program to reverse a given string using a loop.

def reversal(phrase):
	'''
	Takes an input and provides the reverse of input
	
	Parameters: 
				phrase (str): String to be reversed
	
	Returns: reversed_string (str): Reversed Output
	'''

	reversed_string = "" 			#Empty string
	length = len(phrase)			#Length of the input

	
	while length > 0:
		reversed_string = reversed_string + phrase[length - 1]  # Append the last character
		length = length - 1  # Decrease the index

	return reversed_string 

# Main function where the program starts
def main():
	# Takes input string from user & stores it in a variable
	text = input("Enter a text to reverse it: ")

	ans = reversal(text)

	print(ans) 					# Displays Output

# Entry point of the program
if __name__ == "__main__":
	main()