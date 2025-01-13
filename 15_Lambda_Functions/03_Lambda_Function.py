# Write a program to depict comparison between normal function and lambda function

# Normal Function: A traditional function with a defined name and body
def add_function(num1, num2):
    """
    Adds two numbers using a normal function.

    Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2


# Lambda Function: An anonymous function that can take any number of arguments but only has a single expression
add_lambda = lambda val1, val2: val1 + val2


def main():
    """
    Main function to demonstrate the comparison between normal and lambda functions.
    """
    # Using the normal function
    ans1 = add_function(10, 7)

    # Using the lambda function
    ans2 = add_lambda(10, 7)

    print(f"Addition using Normal Function: {ans1}")
    print(f"Addition using Lambda Function: {ans2}")
    print(f"Data type of Lambda Function: {type(add_lambda)}")

# Entry Point of the Program
if __name__ == "__main__":
    main()
