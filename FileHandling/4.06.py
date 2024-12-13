def file_details(file_name):
    try:
        with open(file_name, 'r') as file:
            txt = file.read()
            
            num_lines = len(txt.splitlines())

            num_chars = len(txt) #with enters
            
            num_words = len(txt.split())
            
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