import csv

try:

    with open('it_company.csv','r') as file:
        reader = csv.DictReader(file) #first row as the keys and each subsequent row is dictionary
        
        print("GRAPHIC DESIGNERS")
        print("=================")
        
        for row in reader: #row to dict
            if row['Job Title'] == 'Graphic Designer':
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")

except Exception as e:
    print(f"An error occurred: {e}")