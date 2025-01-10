"""
Student Records:
	- Use a list of dictionaries to store student records:

students = [
    {"Name": "Alice", "Age": 25, "Subjects": {"Math": "A", "Science": "B"}},
    {"Name": "Bob", "Age": 22, "Subjects": {"Math": "B", "Science": "C"}},
]


Perform operations like:
	- Find the average age of students.
	- Print all students who scored "A" in Math.
"""

def get_input_elements(limit, debug=False):
	"""
	Collects student records as a list of dictionaries.

	Parameters:
		limit (int): Number of student records to collect.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A list of dictionaries containing student records.
	"""
	students = []

	for i in range(limit):
		try:
			name = input(f"\nEnter the name of student {i + 1}: ")
			age = int(input(f"Enter the age of {name}: "))
			math_grade = input(f"What is {name}'s grade in Math (A-F): ").upper()
			science_grade = input(f"What is {name}'s grade in Science (A-F): ").upper()

			student = {
				"Name": name,
				"Age": age,
				"Subjects": {
					"Math": math_grade,
					"Science": science_grade,
				}
			}

			students.append(student)

			if debug:
				print(f"\n[DEBUG] Added Student: {student}")

		except ValueError:
			print("Error: Enter a valid positive integer for Age.")

	return students


def data_operations(data, debug=False):
	"""
	Performs operations on student data:
		1. Calculate the average age of students.
		2. Print all students who scored 'A' in Math.

	Parameters:
		data (list): List of dictionaries containing student records.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		None
	"""

	# 1. Calculate Average Age
	print("\nStep 1: Calculating the average age of students.")
	total_age = 0

	for i, student in enumerate(data):
		total_age = total_age + student["Age"]
		if debug:
			print(f"[DEBUG] Student {i + 1}: {student['Name']} - Age: {student['Age']}")

	average_age = total_age / len(data)
	print(f"Average age of students is: {average_age:.2f}")

	# 2. Find Students Who Scored 'A' in Math
	print("\nStep 2: Finding students who scored 'A' in Math.")
	math_scorers = []

	for i, student in enumerate(data):
		if student["Subjects"]["Math"] == "A":
			math_scorers.append(student["Name"])
			if debug:
				print(f"[DEBUG] Student {i + 1}: {student['Name']} scored 'A' in Math.")

	if math_scorers:
		print("\nStudents who scored 'A' in Math:")
		for name in math_scorers:
			print(f"- {name}")
	else:
		print("\nNo student scored 'A' in Math.")


def main():
	"""
	Main function to gather input, store student records, and perform data operations.
	"""
	try:
		size = int(input("How many students are in the class? "))

		while size <= 0:
			print("Error: Enter a positive integer.")
			size = int(input("Try again. How many students are in the class? "))

		debug = input("\nEnable Debug Mode? (yes/no): ").lower().strip() == "yes"

		# Collect student records
		items = get_input_elements(size, debug)

		# Perform operations on student data
		data_operations(items, debug)

	except ValueError:
		print("Error: Please enter a valid positive integer.")


# Entry Point of the Program
if __name__ == "__main__":
	main()
