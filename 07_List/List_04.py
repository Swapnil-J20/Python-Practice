
# List creation
arr = [10, 20, 30, 40, 50]

def main():

	print(arr[0])
	print(arr[1])
	print(arr[2])
	print(arr[3])
	print(arr[4])

	print("---------------------")

	# using length of the loop
	for i in range(len(arr)):
		print(arr[i])

	print("---------------------")

	# using elements of the loop
	for val in arr:
		print(val)
		

if __name__ == "__main__":
	main()
