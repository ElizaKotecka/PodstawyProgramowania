import re

pattern = r'\.[a-zA-Z]{4}$'

try:
    with open('files.txt', 'r') as file:
        for line in file:
            if re.search(pattern, line):
                print(line)

except Exception as e:
    print(f"An error occurred: {e}")