def file_details(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            num_lines = len(lines)

            num_chars = 0
            for line in lines:
                num_chars += len(line)
            
            num_words = 0
            for line in lines:
                words = line.split()
                num_words += len(words)
            
            return num_lines, num_chars, num_words
            
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return None

def main():
    file_name = input("Enter the name of the file: ")
    
    result = file_details(file_name)
    
    if result:
        print(f"File name: {file_name}")
        print(f"Number of lines: {result[0]}")
        print(f"Number of characters: {result[1]}")
        print(f"Number of words: {result[2]}")

if __name__ == "__main__":
    main()