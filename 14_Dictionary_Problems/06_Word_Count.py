# Word Count: Count the frequency of each word in a given sentence using a dictionary.
# Example: Input: "hello world hello" → Output: {'hello': 2, 'world': 1}

def word_count(data, debug=False):
	"""
	Counts the frequency of each word in the given text.

	Parameters:
		data (str): The input text to be analyzed.
		debug (bool): Whether to display debug prints (default is False).

	Returns:
		dict: A dictionary containing words as keys and their counts as values.
	"""

	output = {}

	# Split the text into words
	words = data.split()
	if debug:
		print(f"[DEBUG] Words List: {words}")

	# Count each word
	for word in words:
		output[word] = output.get(word, 0) + 1
		if debug:
			print(f"[DEBUG] Word: '{word}', Current Count: {output[word]}")

	return output

def main():
	"""
	Main function to handle user input and display word counts.
	"""
	text = input("Enter text to get word count: ").strip().lower()

	# Enable Debug Mode
	debug = input("Enable Debug Mode? (yes/no): ").strip().lower() == "yes"

	# Get word count
	result = word_count(text, debug)

	# Display results
	print(f"\nWord Count for: '{text}'")
	for word, count in result.items():
		print(f"{word}: {count}")

# Entry Point of the Program
if __name__ == "__main__":
	main()

