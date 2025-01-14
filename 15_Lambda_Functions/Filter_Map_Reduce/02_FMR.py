

# Checks if the given number is even
def CheckEven(No):
    return (No % 2 == 0)

# Custom filter function to apply a helper function to a list and return filtered data
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if Helper_Function(No):
            Result.append(No)
    return Result

# Accepts user input, applies filtering, and displays the result
def main():
    print("Enter number of elements you want to enter: ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data:")
    for iCnt in range(iSize):
        Value = int(input())
        Data_Input.append(Value)

    print("Data is:", Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)
    print("Data after filter is:", Data_Filter)

# Entry point of the program
if __name__ == "__main__":
    main()
