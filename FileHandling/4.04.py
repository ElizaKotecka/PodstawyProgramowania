try:
    with open('it_company.csv', 'r') as file:
        lines = file.readlines()
        index = 1

        while index < len(lines):
            print(lines[index])
            if index % 5 == 0: 
                input('Press Enter key...')
                print()
            index += 1

except Exception as e:
    print(f"An error occurred: {e}")