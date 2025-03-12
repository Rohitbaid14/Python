def get_words_by_length(filename, length):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            filtered_words = [word.strip('.,!?()[]"') for word in words if len(word.strip('.,!?()[]"')) == length]
            
            if filtered_words:
                print(f"Words with {length} letters:")
                print(', '.join(set(filtered_words)))
            else:
                print(f"No words of length {length} found in the file.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    try:
        word_length = int(input("Enter the word length to search for: "))
        get_words_by_length(filename, word_length)
    except ValueError:
        print("Invalid input. Please enter a valid number.")