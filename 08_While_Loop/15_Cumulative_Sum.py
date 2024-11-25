# Write a program to calculate the cumulative sum of a list

def cumulative_sum(data):
    """
    Calculates the cumulative sum of a list.

    Parameters:
        data (list): A list of integers.

    Returns:
        list: A list where each element is the cumulative sum up to that index.
    """
    j = 0
    cumulative = 0
    result = []

    while j < len(data):
        cumulative = cumulative + data[j]
        result.append(cumulative)
        # Debug print to show the computation step-by-step
        # print(f"Step {j + 1}: cumulative = {cumulative}, current element = {data[j]}")
        j = j + 1

    return result


def main():
    try:
        # Input length of the list
        length = int(input("What should be the length of the list? : "))

        if length <= 0:
            print("Enter a positive integer for length.")
            return

        # Input list items
        items = []
        print("Add items to the list: ")

        for _ in range(length):
            item = int(input())
            items.append(item)

        # Calculate cumulative sum
        output = cumulative_sum(items)

        # Display the result
        print(f"The cumulative sum of the list {items} is: {output}")

    except ValueError:
        print("Error: Please enter valid integers for the list and its length.")


# Entry Point of the program
if __name__ == "__main__":
    main()
