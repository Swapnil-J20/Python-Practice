# List of values 
values = [10, 20, 30, 40, 50]

# Displays the list
print(values)

# Displays the data type
print(type(values))

# Displays the length of the list
print(f"Length of the list is: {len(values)}")

# Printing elements of list
print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[4])

# Data type of element of list
print(type(values[0]))

# Inserts & replaces value in the list at particular position
values.insert(2, 11)
print(values)

# Beyond the range in insert adds value at the end
values.insert(15, 60)
print(f"Size of list is now: {len(values)}")
print(f"Data after insert is: {values} ")

# Adds element at the end of the list
values.append(70)
print(f"Data after append is: {values}")

# Removes the value in the list. Will throw error if value isn't in list
values.remove(11)
print(f"Data after remove is: {values}")

# List supports multiple data types / Heterogeneous
values.append(80.1)
values.append("Ninety")
values.append(True)
print(values)

# Removes and returns an item from a list for particular index. Removes last if no index provided
removed_item = values.pop(0)
print(removed_item)