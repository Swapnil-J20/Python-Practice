# Write a program that takes a score (0-100) and prints the grade

# Hardcoded score & grades
Grade_A = 90
Grade_B = 80
Grade_C = 70
Grade_D = 60



def result(marks):
	
	"""
    Determine the grade based on the score.

    Parameters:
        marks (int): Score between 0 and 100.

    Returns:
        str: Grade ('A', 'B', 'C', 'D', 'F') or an error message for invalid scores.
    """


	if 0 > marks or marks > 100:
		return "Invalid score! Please enter a score between 0 and 100."
	
	elif marks >= Grade_A:
		return "A"
	
	elif marks >= Grade_B:
		return "B"
	
	elif marks >= Grade_C:
		return "C"
	
	elif marks >= Grade_D:
		return "D"
	
	else:
		return "F"

# Main function to execute the program
def main():
	score = input("Enter the score: ")

	try:
		score = int(score)
		grade = result(score)

		print(f"Your grade is: {grade}")
	
	except ValueError:
		print("Please enter an integer")

	

# Entry point of the program
if __name__ == "__main__":
	main()