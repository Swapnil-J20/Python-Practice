# Function to check if a number is even
def CheckEven(No):
    return (No % 2 == 0)

# Function to double a number
def Doubles(No):
    return No * 2

# Custom implementation of filter function
def filterX(Helper_Function, Data):
    Result = []
    for No in Data:
        if Helper_Function(No):  # If condition is met, add to Result
            Result.append(No)
    return Result

# Custom implementation of map function
def mapX(Helper_Function, Data):
    Result = []
    for No in Data:
        Value = Helper_Function(No)  # Apply function and store result
        Result.append(Value)
    return Result    

def main():
    print("Enter number of elements you want to enter: ")
    iSize = int(input())

    Data_Input = []
    print("Please enter the data: ")
    for iCnt in range(iSize):
        Value = int(input())  # Read integer input
        Data_Input.append(Value)

    print("Data is:", Data_Input)
    
    Data_Filter = filterX(CheckEven, Data_Input)  # Filter even numbers
    print("Data after filter is:", Data_Filter)

    Data_Map = mapX(Doubles, Data_Filter)  # Double the filtered values
    print("Data after map is:", Data_Map)

# Entry Point of the Program
if __name__ == "__main__":
	main()