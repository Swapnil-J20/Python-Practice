def divisors(val):

	"""
    Finds all the divisors of a given number.

    Parameters:
        val (int): The number whose divisors are to be found.

    Returns:
        list: A list of all divisors of the number.
    """

	# Negative numbers don't have divisors
	if val < 0:
		return "Input Error: Enter a valid integer"

	if val == 0:
		return [1]

	result = []
	i = 1
	limit = (val//2) + 1

	while i < limit:

		if val % i == 0:
			result.append(i)
		i = i + 1

	result.append(val)

	return result

