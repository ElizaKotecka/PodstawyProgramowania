import csv

try:
    with open('clothing.csv', 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if float(row["Price"]) < 60 and int(row['Stock_Quantity']) < 40:
                print(f"Product ID: {row['Product_ID']}, Name: {row['Product_Name']}, Category: {row['Category']}, Size: {row['Size']}, Color: {row['Color']}, Price: {row['Price']}, Stock: {row['Stock_Quantity']}")

except Exception as e:
    print(f"An error occurred: {e}")