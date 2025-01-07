# Nested Dictionary: Create a nested dictionary to store student names as keys and their marks as values


def get_student_data(limit, debug=False):
	"""
	Collects student data to create a nested dictionary.
	
	Parameters:
		limit (int): Number of students.
		debug (bool): Whether to display debug prints (default is False).
	
	Returns:
		dict: Nested dictionary with student names as keys and subject marks as values.
	"""
	students = {}

	for i in range(limit):
		# Get student name
		student_name = input(f"Enter the name of Student {i + 1}: ").strip()
		
		# Get the number of subjects for the student
		num_subjects = int(input(f"Enter the number of subjects for {student_name}: "))
		
		# Initialize an inner dictionary for subject marks
		subjects = {}
		
		# Collect subject marks
		for j in range(num_subjects):
			subject_name = input(f"Enter the name of Subject {j + 1}: ").strip()
			mark = float(input(f"Enter marks for {subject_name}: "))
			subjects[subject_name] = mark
			
			if debug:
				print(f"[DEBUG] {student_name} - {subject_name}: {mark}")
		
		# Add the inner dictionary to the main dictionary
		students[student_name] = subjects

		if debug:
			print(f"[DEBUG] Current Student Data: {students}")

	return students


def display_student_data(data, debug=False):
	"""
	Displays the student data in a structured format.
	
	Parameters:
		data (dict): Nested dictionary with student names and their marks.
		debug (bool): Whether to display debug prints (default is False).
	"""
	print("\n--- Student Data ---")
	for student, subjects in data.items():
		print(f"\nStudent: {student}")
		for subject, mark in subjects.items():
			print(f"  {subject}: {mark}")
		if debug:
			print(f"[DEBUG] Displayed data for {student}")


def main():
	"""
	Main function to gather input, create a nested dictionary, and display the student data.
	"""
	try:
		# Input: Number of students
		num_students = int(input("Enter the number of students: "))
		
		while num_students <= 0:
			print("Error: Enter a positive integer for the number of students.")
			num_students = int(input("Try again. Enter the number of students: "))
		
		# Enable Debug Mode
		debug = input("\nEnable Debug Mode? (yes/no): ").strip().lower() == "yes"

		# Collect student data
		student_data = get_student_data(num_students, debug)

		# Display the collected data
		display_student_data(student_data, debug)

	except ValueError:
		print("Error: Please enter a valid positive integer for the number of students.")


# Entry Point of the Program
if __name__ == "__main__":
	main()

