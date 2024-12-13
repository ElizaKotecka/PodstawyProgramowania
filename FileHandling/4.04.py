try:
    with open('it_company.csv', 'r') as file:
        lines = file.readlines()
        index = 1

        while index < len(lines):
            for i in range(index, min(index+5, len(lines))): #stop without error when end of file reached
                print(lines[i])
            
            input('Press Enter key...')

            index += 5

except Exception as e:
    print(f"An error occurred: {e}")



