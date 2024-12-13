with open('pets.txt', 'r') as file:
    words = 0
    for line in file:
        line_split = line.split()
        words += (len(line_split))

print(words)


    