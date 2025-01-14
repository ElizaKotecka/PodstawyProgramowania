import json

product = {}

# Read product data from the keyboard
product["name"] = input("Enter the product name: ")
product["price"] = float(input("Enter the product price (e.g., 19.99): "))
paid = input("Do you paid for the product? (Y/N): ")

if paid == "Y":
    product["paid"] = True
elif paid == "N":
    product["paid"] = False
else:
    print("Invalid input for 'paid'. Please enter 'Y' or 'N'.")
    exit()  # Exit the program if the input is invalid


# Save product data to json file
file_name = "product.json"
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(product, file, indent=4, ensure_ascii=False)

print("Product added to", file_name)
