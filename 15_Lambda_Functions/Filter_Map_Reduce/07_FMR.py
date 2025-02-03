from functools import reduce  # Importing reduce function from functools

# Lambda function to check if a number is even
CheckEven = lambda No: (No % 2 == 0)

# Lambda function to double a number
Doubles = lambda No: No * 2

# Lambda function to sum two numbers
Sum = lambda A, B: A + B 

def main():
    print("Enter number of elements you want to enter: ")
    iSize = int(input())  # Taking input for the number of elements

    Data_Input = []
    print("Please enter the data ")
    for iCnt in range(0, iSize, 1):
        Value = int(input())  # Taking integer input
        Data_Input.append(Value)  # Adding input to the list

    print("Data is:", Data_Input)

    # Filtering even numbers from the input data
    Data_Filter = list(filter(CheckEven, Data_Input))
    print("Data after filter is:", Data_Filter)

    # Mapping: Doubling each even number
    Data_Map = list(map(Doubles, Data_Filter))
    print("Data after map is:", Data_Map)

    # Reducing: Summing up all doubled values
    Output = reduce(Sum, Data_Map)
    print("Result after reduce is:", Output)

if __name__ == "__main__":
    main()  # Entry point of the program
