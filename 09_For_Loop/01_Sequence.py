# Write a program to print numbers from 1 to 10 using a loop

# Main function where the program starts
def main():
    """
    Prints numbers from 1 to 10 using a loop.
    Includes optional debug prints to show loop execution.
    """
    print("This program prints a sequence of numbers from 1 to 10 using a for loop.")

    # Ask if the user wants to enable debug mode
    debug = input("Enable debug mode? (yes/no): ").strip().lower() == "yes"

    # Loop to print numbers from 1 to 10
    for i in range(1, 11):
        if debug:
            print(f"Debug: Current value of i = {i}")
        print(i)


# Entry Point of the program
if __name__ == "__main__":
    main()