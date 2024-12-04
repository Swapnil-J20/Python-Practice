
def divisors(val, debug=False):
	"""
	Finds all divisors of a given number.

	Parameters:
		val (int): The number for which divisors are to be found.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		list: A list of all divisors of the given number.
	"""
	if val <= 0:
		return "Error: Divisors are only defined for positive integers."

	output = [1]  # 1 is always a divisor
	limit = (val // 2) + 1  # Check divisors up to half of the number

	# Find divisors using a loop
	for i in range(2, limit):
		if val % i == 0:
			output.append(i)
			if debug:
				print(f"Step {i - 1}: Found divisor {i}, Current Divisors: {output}")

	# Add the number itself as a divisor
	output.append(val)

	return output
