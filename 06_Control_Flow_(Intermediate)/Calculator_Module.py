# This is a library that has functions to perform calculations for simple calculator

def addition(val1, val2):
	'''
	Performs addition of two numbers
	
	Parameters: 
				val1 (float)
				val2 (float)
	
	Returns: Output of calculation (float)
	'''
	return val1 + val2

def substraction(val1, val2):
	'''
	Performs subtraction of two numbers
	
	Parameters: 
				val1 (float)
				val2 (float)
	
	Returns: Output of calculation (float)
	'''
	return val1 - val2

def multiplication(val1, val2):
	'''
	Performs multiplication of two numbers
	
	Parameters: 
				val1 (float)
				val2 (float)
	
	Returns: Output of calculation (float)
	'''
	return val1 * val2

def division(val1, val2):
	'''
	Performs multiplication of two numbers
	
	Parameters: 
				val1 (float)
				val2 (float)
	
	Returns: Output of calculation (float), Error when divided by zero
	'''
	if val2 == 0:
		return "Error: Division by zero not allowed"
	else:
		return val1 / val2
		




